"""
GenTar Product report extractor module
    This module takes care of extracting the data from the GenTar products report.
"""
import luigi
from luigi.contrib.spark import PySparkTask
from pyspark import SparkContext
from pyspark.sql import SparkSession

from impc_etl.jobs.extract.imits_extractor import extract_gentar_tsv
from impc_etl.workflow.config import ImpcConfig


class ProductReportExtractor(PySparkTask):
    """
    PySpark Task class to extract GenTar Product report data.
    """

    #: Name of the Spark task
    name: str = "IMPC_Gentar_Product_Report_Extractor"

    #: Type of experiment can be "specimen_level" or "line_level"
    product_report_tsv_path: luigi.Parameter = luigi.Parameter()

    #: Path of the output directory where the new parquet file will be generated.
    output_path: luigi.Parameter = luigi.Parameter()

    def output(self):
        """
        Returns the full parquet path as an output for the Luigi Task
        (e.g. impc/dr15.2/parquet/product_report_parquet)
        """
        return ImpcConfig().get_target(f"{self.output_path}product_report_raw_parquet")

    def app_options(self):
        """
        Generates the options pass to the PySpark job
        """
        return [
            self.product_report_tsv_path,
            self.output().path,
        ]

    def main(self, sc: SparkContext, *args):
        """
        Takes in a SparkContext and the list of arguments generated by `app_options` and executes the PySpark job.
        """
        spark = SparkSession(sc)

        # Parsing app options
        product_report_tsv_path = args[0]
        output_path = args[1]

        product_df = extract_gentar_tsv(spark, product_report_tsv_path, "Product")
        product_df.write.mode("overwrite").parquet(output_path)
