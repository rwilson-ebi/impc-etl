"""
    Module to hold Luigi task that calculates the derived parameters on experimental data.

    The general process is:

    - Takes in a set of experiments and the information coming from IMPReSS.
    - Gets the derived parameter list from IMPReSS for IMPC parameters
    and some EuroPhenome derivations from a constant list.
    - Checks for each experiment that all the input values for the derivation formula are present
    - Generates a string value containing the derivation formula and the input values
    - Applies the derivation using the parameter derivation JAR application provided by the DCC.
    - Adds the resulting derived parameter values to the original experiments as new parameter values.
"""
import copy
import json
from typing import Any

import luigi
from luigi.contrib.spark import PySparkTask
from pyspark import SparkContext, Row
from pyspark.sql import SparkSession

from impc_etl.jobs.transform.line_experiment_cross_ref import (
    LineLevelExperimentCrossRef,
)
from impc_etl.jobs.transform.specimen_experiment_cross_ref import (
    SpecimenLevelExperimentCrossRef,
)
from impc_etl.workflow.config import ImpcConfig


class ParameterDerivator(PySparkTask):
    """
    PySpark task that takes in a set of experiments and computes all the derived parameters.

    This tasks depends on:

    - `impc_etl.jobs.transform.specimen_experiment_cross_ref.SpecimenLevelExperimentCrossRef` for
    specimen level experiments or
    `impc_etl.jobs.transform.line_experiment_cross_ref.LineLevelExperimentCrossRef` for line level
     experiments
     - `impc_etl.jobs.extract.impress_extractor.ImpressExtractor`
    """

    #: Name of the Spark task
    name = "IMPC_Experiment_Parameter_Derivator"

    #: Experimental level of the data (can be 'specimen_level' or 'line_level')
    experiment_level = luigi.Parameter()

    #: Path to the Europhenome parquet derivations
    europhenome_derived_data_path = luigi.Parameter()

    #: Path of the output directory where the new parquet file will be generated.
    output_path = luigi.Parameter()

    def output(self):
        """
        Returns the full parquet path as an output for the Luigi Task
        (e.g. impc/dr15.2/parquet/specimen_level_experiment_derived_parquet)
        """
        return ImpcConfig().get_target(
            f"{self.output_path}{self.experiment_level}_experiment_derived_parquet"
        )

    def requires(self):
        """
        Defines the luigi  task dependencies
        """
        experiment_dependency = (
            SpecimenLevelExperimentCrossRef()
            if self.experiment_level == "specimen_level"
            else LineLevelExperimentCrossRef()
        )
        return [experiment_dependency]

    def app_options(self):
        """
        Generates the options pass to the PySpark job
        """
        return [self.input()[0].path, self.experiment_level, self.europhenome_derived_data_path, self.output().path]

    def computeHash(self, elem):
        if not elem['_pipeline']:
            return None
        if not elem['_procedureID']:
            return None
        if not elem['_project']:
            return None
        if not elem['_sequenceID']:
            return None
        if not elem['specimenID']:
            return None
        if not elem['_experimentID']:
            return None
        if not elem['_dataSource']:
            return None
        if not elem['_centreID']:
            return None

        return elem['_pipeline'] + '#' + elem['_procedureID'] + '#' + elem['_project'] + '#' + elem[
            '_sequenceID'] + '#' + elem['specimenID'] + '#' + elem['_experimentID'] + '#' + elem['_dataSource'] + '#' + \
               elem['_centreID']

    def shuffleElem(self, simpleParameterList):
        result = []
        for elem in simpleParameterList:
            result.append({
                '_parameterID': elem['_parameterID'],
                '_sequenceID': elem['_sequenceID'] if '_sequenceID' in elem else None,
                '_unit': elem['_unit'],
                'parameterStatus': elem['parameterStatus'] if 'parameterStatus' in elem else None,
                'value': elem['value']
            })
        return result

    def main(self, sc: SparkContext, *args: Any):
        """
        Takes in a set of experiments and the information coming from IMPReSS.
        Gets the derived parameter list from IMPReSS for IMPC parameters and
        some EuroPhenome derivations from a constant list.
        Applies the derivations to all the experiments and adds the derived parameter values to each experiment.
        """
        spark = SparkSession(sc)
        experiment_parquet_path = args[0]
        experiment_level = args[1]
        europhenome_derived_data_path = args[2]
        output_path = args[3]
        experiment_df = spark.read.parquet(experiment_parquet_path)

        if experiment_level == 'line_level':
            experiment_df.write.parquet(output_path)
        else:
            jsonData = spark.read.option("multiline", "true").json(europhenome_derived_data_path)
            data = jsonData.toJSON().map(json.loads).collect()

            print('Experiment initial [COUNT]: {}'.format(experiment_df.count()))
            print('Experiment initial [COLS]: {}'.format(len(experiment_df.columns)))

            hashedData = {}
            for elem in data:
                hsh = self.computeHash(elem)
                elem['simpleParameter'] = self.shuffleElem(elem['simpleParameter'])
                hashedData[hsh] = elem

            _schema = copy.deepcopy(experiment_df.schema)

            dataCollect = experiment_df.rdd.toLocalIterator()
            europhenomeList = []
            count = 1
            for row in dataCollect:
                if count % 100000 == 0:
                    print(' - Count: {} of {}'.format(count, experiment_df.count()))
                count += 1

                rowHash = self.computeHash(row)
                if not rowHash:
                    continue

                if rowHash in hashedData:
                    dataDict = row.asDict()
                    europhenomeData = hashedData[rowHash]
                    euroList = []
                    for element in europhenomeData['simpleParameter']:
                        if not 'parameterStatus' in element:
                            element['parameterStatus'] = None
                        if not '_sequenceID' in element:
                            element['_sequenceID'] = None
                        euroRow = Row(**element)
                        euroList.append(euroRow)
                    euroList.extend(dataDict['simpleParameter'])
                    dataDict['simpleParameter'] = euroList
                    newRow = Row(**dataDict)
                    europhenomeList.append(newRow)

                    experiment_df = experiment_df.filter(
                        (~(
                                (experiment_df['_pipeline'] == europhenomeData['_pipeline']) &
                                (experiment_df['_procedureID'] == europhenomeData['_procedureID']) &
                                (experiment_df['_project'] == europhenomeData['_project']) &
                                (experiment_df['_sequenceID'] == europhenomeData['_sequenceID']) &
                                (experiment_df['specimenID'] == europhenomeData['specimenID']) &
                                (experiment_df['_experimentID'] == europhenomeData['_experimentID']) &
                                (experiment_df['_dataSource'] == europhenomeData['_dataSource']) &
                                (experiment_df['_centreID'] == europhenomeData['_centreID'])
                        ))
                    )

            europhenome_df = spark.createDataFrame(europhenomeList, schema=_schema)

            print('Experiment after [COUNT]: {}'.format(experiment_df.count()))
            print('Experiment after [COLS]: {}'.format(len(experiment_df.columns)))
            print('EUROPHENOME after [COUNT]: {}'.format(europhenome_df.count()))
            print('EUROPHENOME after [COUNT]: {}'.format(len(europhenome_df.columns)))
            experiment_df = experiment_df.union(europhenome_df)
            print('---')
            print('Experiment merge [COUNT]: {}'.format(experiment_df.count()))
            print('Experiment merge [COLS]: {}'.format(len(experiment_df.columns)))
            experiment_df.write.parquet(output_path)


class SpecimenLevelExperimentParameterDerivator(ParameterDerivator):
    name = "IMPC_Specimen_Level_Experiment_Parameter_Derivator"
    experiment_level = "specimen_level"


class LineLevelExperimentParameterDerivator(ParameterDerivator):
    name = "IMPC_Line_Level_Experiment_Parameter_Derivator"
    experiment_level = "line_level"
