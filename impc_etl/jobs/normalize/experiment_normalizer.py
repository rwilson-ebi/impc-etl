import sys
from pyspark.sql import SparkSession
from impc_etl.jobs.normalize.dcc_transformations.experiments import *


def normalize_experiments(spark_session: SparkSession,
                          experiment_parquet_path: str,
                          mouse_parquet_path: str,
                          embryo_parquet_path: str,
                          pipeline_parquet_path: str) -> DataFrame:
    """
    DCC experiment normalizer

    :param pipeline_parquet_path:
    :param embryo_parquet_path:
    :param mouse_parquet_path:
    :param experiment_parquet_path:
    :param SparkSession spark_session: PySpark session object
    :return: a normalized specimen parquet file
    :rtype: DataFrame
    """
    experiment_df = spark_session.read.parquet(experiment_parquet_path)
    mouse_df = spark_session.read.parquet(mouse_parquet_path)
    embryo_df = spark_session.read.parquet(embryo_parquet_path)
    pipeline_df = spark_session.read.parquet(pipeline_parquet_path)

    specimen_cols = ['_centreID', '_specimenID', '_colonyID',
                     '_isBaseline', '_productionCentre', '_phenotypingCentre',
                     'phenotyping_consortium']

    mouse_specimen_df = mouse_df.select(*specimen_cols)
    embryo_specimen_df = embryo_df.select(*specimen_cols)
    specimen_df = mouse_specimen_df.union(embryo_specimen_df)

    experiment_df = drop_null_colony_id(experiment_df, specimen_df)
    experiment_df = re_map_europhenome_experiments(experiment_df, specimen_df)
    experiment_df = generate_metadata_group(experiment_df, pipeline_df, specimen_df)
    experiment_df = generate_metadata(experiment_df, pipeline_df, specimen_df)
    experiment_df = get_associated_body_weight(experiment_df, mouse_df)
    experiment_df = generate_age_information(experiment_df, mouse_df)
    experiment_df = get_derived_parameters(spark_session, experiment_df, pipeline_df)
    return experiment_df


def main(argv):
    experiment_parquet_path = argv[1]
    mouse_parquet_path = argv[2]
    embryo_parquet_path = argv[3]
    pipeline_parquet_path = argv[4]
    output_path = argv[5]
    spark = SparkSession.builder.getOrCreate()
    experiment_normalized_df = normalize_experiments(spark, experiment_parquet_path,
                                                     mouse_parquet_path, embryo_parquet_path,
                                                     pipeline_parquet_path)
    experiment_normalized_df.write.mode('overwrite').parquet(output_path)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
