import luigi

from impc_etl.jobs.load.impc_api.impc_gene_bundle_mapper import ImpcGeneBundleMapper
from impc_etl.jobs.load.impc_images_mapper import ImagesPipelineInputGenerator
from impc_etl.jobs.load.mp_chooser_mapper import MPChooserGenerator
from impc_etl.jobs.load.solr.gene_mapper import GeneLoader
from impc_etl.jobs.load.solr.genotype_phenotype_mapper import GenotypePhenotypeLoader
from impc_etl.jobs.load.solr.impc_images_mapper import ImpcImagesLoader
from impc_etl.jobs.load.solr.mp_mapper import MpLoader
from impc_etl.jobs.load.solr.pipeline_mapper import ImpressToParameterMapper
from impc_etl.jobs.load.solr.stats_results_mapper import StatsResultsMapper
from impc_etl.jobs.load.stats_pipeline_input_mapper import StatsPipelineInputMapper


class ImpcPreStatisticalAnalysis(luigi.Task):
    def requires(self):
        return [
            StatsPipelineInputMapper(),
            ImagesPipelineInputGenerator(),
            MPChooserGenerator(),
            ImpcImagesLoader(),
        ]


class ImpcPostStatisticalAnalysis(luigi.Task):
    def requires(self):
        return [
            ImpressToParameterMapper(),
            StatsResultsMapper(),
            GenotypePhenotypeLoader(),
            GeneLoader(),
            MpLoader(),
        ]


class ImpcApi(luigi.Task):
    def requires(self):
        return [ImpcGeneBundleMapper()]


# class ImpcSolrCores(luigi.Task):
#     openstats_jdbc_connection = luigi.Parameter()
#     openstats_db_user = luigi.Parameter()
#     openstats_db_password = luigi.Parameter()
#     data_release_version = luigi.Parameter()
#     use_cache = luigi.Parameter()
#     dcc_xml_path = luigi.Parameter()
#     imits_colonies_tsv_path = luigi.Parameter()
#     imits_alleles_tsv_path = luigi.Parameter()
#     imits_product_tsv_path = luigi.Parameter()
#     mgi_allele_input_path = luigi.Parameter()
#     mgi_strain_input_path = luigi.Parameter()
#     mgi_gene_pheno_input_path = luigi.Parameter()
#     mgi_homologene_input_path = luigi.Parameter()
#     mgi_mrk_list_input_path = luigi.Parameter()
#     ontology_input_path = luigi.Parameter()
#     emap_emapa_csv_path = luigi.Parameter()
#     emapa_metadata_csv_path = luigi.Parameter()
#     ma_metadata_csv_path = luigi.Parameter()
#     mpath_metadata_csv_path = luigi.Parameter()
#     impc_search_index_csv_path = luigi.Parameter()
#     mp_relation_augmented_metadata_table_csv_path = luigi.Parameter()
#     threei_stats_results_csv = luigi.Parameter()
#     embryo_data_json_path = luigi.Parameter()
#     omero_ids_csv_path = luigi.Parameter()
#     http_proxy = luigi.Parameter()
#     output_path = luigi.Parameter()
#
#     def requires(self):
#         return [
#             PipelineCoreLoader(
#                 dcc_xml_path=self.dcc_xml_path,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 imits_alleles_tsv_path=self.imits_alleles_tsv_path,
#                 output_path=self.output_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 emap_emapa_csv_path=self.emap_emapa_csv_path,
#                 emapa_metadata_csv_path=self.emapa_metadata_csv_path,
#                 ma_metadata_csv_path=self.ma_metadata_csv_path,
#             ),
#             GenotypePhenotypeCoreLoader(
#                 openstats_jdbc_connection=self.openstats_jdbc_connection,
#                 openstats_db_user=self.openstats_db_user,
#                 openstats_db_password=self.openstats_db_password,
#                 data_release_version=self.data_release_version,
#                 use_cache=self.use_cache,
#                 dcc_xml_path=self.dcc_xml_path,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 imits_alleles_tsv_path=self.imits_alleles_tsv_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 emap_emapa_csv_path=self.emap_emapa_csv_path,
#                 emapa_metadata_csv_path=self.emapa_metadata_csv_path,
#                 ma_metadata_csv_path=self.ma_metadata_csv_path,
#                 mpath_metadata_csv_path=self.mpath_metadata_csv_path,
#                 threei_stats_results_csv=self.threei_stats_results_csv,
#                 raw_data_in_output="exclude",
#                 http_proxy=self.http_proxy,
#                 output_path=self.output_path,
#             ),
#             StatsResultsCoreLoader(),
#             MGIPhenotypeCoreLoader(
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 mgi_gene_pheno_input_path=self.mgi_gene_pheno_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 output_path=self.output_path,
#             ),
#             MPCoreLoader(
#                 dcc_xml_path=self.dcc_xml_path,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 imits_alleles_tsv_path=self.imits_alleles_tsv_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 emap_emapa_csv_path=self.emap_emapa_csv_path,
#                 emapa_metadata_csv_path=self.emapa_metadata_csv_path,
#                 ma_metadata_csv_path=self.ma_metadata_csv_path,
#                 impc_search_index_csv_path=self.impc_search_index_csv_path,
#                 mp_relation_augmented_metadata_table_csv_path=self.mp_relation_augmented_metadata_table_csv_path,
#                 output_path=self.output_path,
#             ),
#             GeneCoreLoader(
#                 imits_tsv_path=self.imits_alleles_tsv_path,
#                 embryo_data_json_path=self.embryo_data_json_path,
#                 mgi_homologene_input_path=self.mgi_homologene_input_path,
#                 mgi_mrk_list_input_path=self.mgi_mrk_list_input_path,
#                 output_path=self.output_path,
#                 dcc_xml_path=self.dcc_xml_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 emap_emapa_csv_path=self.emap_emapa_csv_path,
#                 emapa_metadata_csv_path=self.emapa_metadata_csv_path,
#                 ma_metadata_csv_path=self.ma_metadata_csv_path,
#                 mpath_metadata_csv_path=self.mpath_metadata_csv_path,
#                 threei_stats_results_csv=self.threei_stats_results_csv,
#                 openstats_jdbc_connection=self.openstats_jdbc_connection,
#                 openstats_db_user=self.openstats_db_user,
#                 openstats_db_password=self.openstats_db_password,
#                 data_release_version=self.data_release_version,
#                 use_cache=self.use_cache,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 imits_alleles_tsv_path=self.imits_alleles_tsv_path,
#             ),
#             Allele2Extractor(
#                 imits_tsv_path=self.imits_alleles_tsv_path, output_path=self.output_path
#             ),
#             ProductReportExtractor(),
#             ImpcImagesCoreLoader(
#                 omero_ids_csv_path=self.omero_ids_csv_path,
#                 dcc_xml_path=self.dcc_xml_path,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 imits_alleles_tsv_path=self.imits_alleles_tsv_path,
#                 output_path=self.output_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#                 emap_emapa_csv_path=self.emap_emapa_csv_path,
#                 emapa_metadata_csv_path=self.emapa_metadata_csv_path,
#                 ma_metadata_csv_path=self.ma_metadata_csv_path,
#             ),
#         ]
#
#
# class ImpcStatPacketLoader(luigi.Task):
#     openstats_jdbc_connection = luigi.Parameter()
#     openstats_db_user = luigi.Parameter()
#     openstats_db_password = luigi.Parameter()
#     data_release_version = luigi.Parameter()
#     use_cache = luigi.Parameter()
#     dcc_xml_path = luigi.Parameter()
#     imits_colonies_tsv_path = luigi.Parameter()
#     imits_alleles_tsv_path = luigi.Parameter()
#     mgi_allele_input_path = luigi.Parameter()
#     mgi_strain_input_path = luigi.Parameter()
#     ontology_input_path = luigi.Parameter()
#     emap_emapa_csv_path = luigi.Parameter()
#     emapa_metadata_csv_path = luigi.Parameter()
#     ma_metadata_csv_path = luigi.Parameter()
#     mpath_metadata_csv_path = luigi.Parameter()
#     threei_stats_results_csv = luigi.Parameter()
#     http_proxy = luigi.Parameter()
#     output_path = luigi.Parameter()
#
#     def requires(self):
#         return [StatsResultsCoreLoader()]
#
#
# class ImpcWindowedDataLoader(luigi.Task):
#     openstats_jdbc_connection = luigi.Parameter()
#     openstats_db_user = luigi.Parameter()
#     openstats_db_password = luigi.Parameter()
#     data_release_version = luigi.Parameter()
#     use_cache = luigi.Parameter()
#     dcc_xml_path = luigi.Parameter()
#     imits_colonies_tsv_path = luigi.Parameter()
#     imits_alleles_tsv_path = luigi.Parameter()
#     mgi_allele_input_path = luigi.Parameter()
#     mgi_strain_input_path = luigi.Parameter()
#     ontology_input_path = luigi.Parameter()
#     emap_emapa_csv_path = luigi.Parameter()
#     emapa_metadata_csv_path = luigi.Parameter()
#     ma_metadata_csv_path = luigi.Parameter()
#     mpath_metadata_csv_path = luigi.Parameter()
#     threei_stats_results_csv = luigi.Parameter()
#     http_proxy = luigi.Parameter()
#     output_path = luigi.Parameter()
#
#     def requires(self):
#         return [
#             StatsResultsCoreLoader(
#                 raw_data_in_output="include",
#                 extract_windowed_data="true",
#             )
#         ]
#
#
# class ImpcDataDrivenAnnotationLoader(SparkSubmitTask):
#     app = "impc_etl/jobs/load/data_driven_annotation.py"
#     name = "IMPC_Data_Driven_Annotation_Loader"
#     output_path = luigi.Parameter()
#
#     def requires(self):
#         return [
#             ObservationsMapper(
#                 dcc_xml_path=self.dcc_xml_path,
#                 imits_colonies_tsv_path=self.imits_colonies_tsv_path,
#                 output_path=self.output_path,
#                 mgi_strain_input_path=self.mgi_strain_input_path,
#                 mgi_allele_input_path=self.mgi_allele_input_path,
#                 ontology_input_path=self.ontology_input_path,
#             )
#         ]
#
#     def app_options(self):
#         return [self.input()[0].path, self.output().path]
#
#     def output(self):
#         self.output_path = (
#             self.output_path + "/"
#             if not self.output_path.endswith("/")
#             else self.output_path
#         )
#         return ImpcConfig().get_target(
#             f"{self.output_path}annotated_observations_parquet"
#         )
#
#
# class ImpcIndexDaily(luigi.Task):
#     name = "IMPC_Index_Daily"
#     imits_product_tsv_path = luigi.Parameter()
#     parquet_path = luigi.Parameter()
#     solr_path = luigi.Parameter()
#     local_path = luigi.Parameter()
#     remote_host = luigi.Parameter()
#
#     def requires(self):
#         return [
#             ProductReportExtractor(),
#             GeneCoreLoader(),
#         ]
#
#     def run(self):
#         tasks = []
#         for dependency in self.input():
#             tasks.append(
#                 ImpcMergeIndex(
#                     remote_host=self.remote_host,
#                     parquet_path=dependency.path,
#                     solr_path=self.solr_path,
#                     local_path=self.local_path,
#                 )
#             )
#         yield tasks
#
#
# class ImpcCleanDaily(luigi.Task):
#     name = "IMPC_Clean_Daily"
#     imits_product_tsv_path = luigi.Parameter()
#     parquet_path = luigi.Parameter()
#     solr_path = luigi.Parameter()
#     local_path = luigi.Parameter()
#     remote_host = luigi.Parameter()
#
#     def _delele_target_if_exists(
#         self, target: Union[luigi.LocalTarget, HdfsTarget], hdfs=False
#     ):
#         if target.exists():
#             print(target.path)
#             if hdfs:
#                 target.remove(skip_trash=True)
#             else:
#                 target.remove()
#
#     def run(self):
#         index_daily_task = ImpcIndexDaily(
#             imits_product_tsv_path=self.imits_product_tsv_path,
#             remote_host=self.remote_host,
#             parquet_path=self.parquet_path,
#             solr_path=self.solr_path,
#             local_path=self.local_path,
#         )
#         for index_daily_dependency in index_daily_task.requires():
#             impc_merge_index_task = ImpcMergeIndex(
#                 remote_host=self.remote_host,
#                 parquet_path=index_daily_dependency.output().path,
#                 solr_path=self.solr_path,
#                 local_path=self.local_path,
#             )
#             impc_copy_index_task = impc_merge_index_task.requires()[0]
#             impc_parquet_to_solr_task = impc_copy_index_task.requires()[0]
#
#             self._delele_target_if_exists(index_daily_dependency.output(), hdfs=True)
#             self._delele_target_if_exists(impc_merge_index_task.output())
#             self._delele_target_if_exists(impc_copy_index_task.output())
#             self._delele_target_if_exists(impc_parquet_to_solr_task.output(), hdfs=True)
#         self._delele_target_if_exists(Allele2Extractor().output(), hdfs=True)
#         self._delele_target_if_exists(GeneExtractor().output(), hdfs=True)
#         self._delele_target_if_exists(AlleleExtractor().output(), hdfs=True)
#
#
# class ImpcIndexDataRelease(luigi.Task):
#     name = "IMPC_Index_Data_Release"
#     dcc_xml_path = luigi.Parameter()
#     imits_colonies_tsv_path = luigi.Parameter()
#     output_path = luigi.Parameter()
#     mgi_strain_input_path = luigi.Parameter()
#     mgi_allele_input_path = luigi.Parameter()
#     ontology_input_path = luigi.Parameter()
#     parquet_path = luigi.Parameter()
#     solr_path = luigi.Parameter()
#     local_path = luigi.Parameter()
#     remote_host = luigi.Parameter()
#
#     def requires(self):
#         return [
#             ObservationsMapper(),
#             StatsResultsCoreLoader(),
#             GeneCoreLoader(),
#             Allele2Extractor(),
#             GenotypePhenotypeCoreLoader(),
#             MPCoreLoader(),
#             PipelineCoreLoader(),
#             ProductReportExtractor(),
#             MGIPhenotypeCoreLoader(),
#             ImpcImagesCoreLoader(),
#         ]
#
#     def run(self):
#         tasks = []
#         for dependency in self.input():
#             tasks.append(
#                 ImpcMergeIndex(
#                     remote_host=self.remote_host,
#                     parquet_path=dependency.path,
#                     solr_path=self.solr_path,
#                     local_path=self.local_path,
#                 )
#             )
#             if "stats_results" in dependency.path:
#                 tasks.append(
#                     ImpcMergeIndex(
#                         remote_host=self.remote_host,
#                         parquet_path=dependency.path + "_raw_data",
#                         solr_path=self.solr_path,
#                         local_path=self.local_path,
#                     )
#                 )
#         yield tasks
#
#
# class ImpcApiDatasource(luigi.Task):
#     name = "IMPC_Generate_API_Datasource"
#
#     def requires(self):
#         return [ApiPostgreSQLLoader()]
