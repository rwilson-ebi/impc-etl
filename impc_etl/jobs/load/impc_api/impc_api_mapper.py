from typing import List, Dict

import luigi
from luigi.contrib.spark import PySparkTask
from pyspark.sql import SparkSession
from pyspark.sql.functions import arrays_zip
from impc_etl.workflow.config import ImpcConfig
from impc_etl.workflow.load import ObservationsMapper


class ApiMapper(PySparkTask):
    name = "IMPC_Api_Mapper"
    output_entity_name = ""
    primary_dependency: luigi.Task = None
    column_select: List[str] = []
    column_renaming: Dict = {}
    extra_transformations = {}
    output_path = luigi.Parameter()

    def requires(self):
        return [self.primary_dependency]

    def output(self):
        return ImpcConfig().get_target(
            f"{self.output_path}_{self.output_entity_name}_api_parquet"
        )

    def app_options(self):
        return [
            self.input()[0],
            self.output().path,
        ]

    def main(self, sc, *args):
        spark = SparkSession(sc)
        input_parquet_path = args[0]
        output_path = args[1]

        source_df = spark.read.parquet(input_parquet_path)
        impc_api_df = source_df.select(self.column_select).distinct()

        for col_name, new_col_name in self.column_renaming.items():
            impc_api_df = impc_api_df.withColumnRenamed(col_name, new_col_name)

        for col_name, transformation in self.extra_transformations.items():
            impc_api_df = impc_api_df.withColumn(col_name, transformation)

        impc_api_df.write.parquet(output_path)


class ApiSpecimenMapper(ApiMapper):
    output_entity_name = "specimen"
    primary_dependency = ObservationsMapper()
    column_select = [
        "specimen_id",
        "external_sample_id",
        "colony_id",
        "strain_accession_id",
        "genetic_background",
        "strain_name",
        "zygosity",
        "production_center",
        "phenotyping_center",
        "project",
        "litter_id",
        "biological_sample_group",
        "sex",
        "pipeline_stable_id",
        "developmental_stage_name",
        "developmental_stage_acc",
        "date_of_birth",
    ]
    column_renaming = {
        "external_sample_id": "source_id",
        "biological_sample_group": "sample_group",
    }


class ApiExperimentMapper(ApiMapper):
    output_entity_name = "experiment"
    primary_dependency = ObservationsMapper()
    column_select = [
        "experiment_id",
        "specimen_id",
        "experiment_source_id",
        "phenotyping_center",
        "pipeline_stable_id",
        "procedure_stable_id",
        "date_of_experiment",
        "metadata",
        "metadata_group",
        "procedure_sequence_id",
        "age_in_days",
        "age_in_weeks",
        "weight",
        "weight_date",
        "weight_days_old",
    ]
    column_renaming = {
        "experiment_source_id": "source_id",
        "age_in_days": "specimen_age_in_days",
        "age_in_weeks": "specimen_age_in_weeks",
        "weight": "specimen_weight",
        "weight_date": "specimen_weight_date",
        "weight_days_old": "specimen_weight_age_in_days",
    }


class ApiObservationMapper(ApiMapper):
    output_entity_name = "observation"
    primary_dependency = ObservationsMapper()
    column_select = [
        "observation_id",
        "experiment_id",
        "parameter_stable_id",
        "observation_type",
        "sequence_id",
        "data_point",
        "category",
        "text",
        "time_point",
        "discrete_point",
        "increment_value",
        "subterm_id",
        "sub_term_name",
        "sub_term_description",
    ]
    column_renaming = {
        "sequence_id": "parameter_sequence_id",
        "subterm_id": "ontology_term_id",
        "subterm_name": "ontology_term_name",
        "sub_term_description": "ontology_term_description",
    }
    extra_transformations = {
        "ontology_terms": arrays_zip(
            "ontology_term_id", "ontology_term_name", "ontology_term_description"
        )
    }
