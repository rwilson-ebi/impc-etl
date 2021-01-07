"""
Config file
"""
from pyspark.sql.types import StringType, ArrayType


class SparkConfig:
    SPARK_JAR_PACKAGES = "com.databricks:spark-xml_2.11:0.7.0"


class OntologySchema:
    LABEL_ANNOTATION = ""
    ALT_ID = ""
    X_REF = ""
    REPLACEMENT = ""
    CONSIDER = ""
    TERM_REPLACED_BY = ""
    IS_OBSOLETE = ""
    SYNONYM_ANNOTATIONS = [
        "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym",
        "http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym",
    ]
    DEFINITION_ANNOTATION = "http://purl.obolibrary.org/obo/IAO_0000115"
    PART_OF = ""


class Constants:
    SKIPPED_PROCEDURES = {
        "SLM_SLM",
        "SLM_AGS",
        "TRC_TRC",
        "DSS_DSS",
        "MGP_ANA",
        "MGP_BCI",
        "MGP_BMI",
        "MGP_EEI",
        "MGP_MLN",
        "MGP_PBI",
        "MGP_IMM",
    }
    VALID_PROJECT_IDS = {
        "BaSH",
        "DTCC",
        "EUMODIC",
        "EUCOMM-EUMODIC",
        "Helmholtz GMC",
        "JAX",
        "NING",
        "MARC",
        "MGP",
        "MGP Legacy",
        "MRC",
        "NorCOMM2",
        "Phenomin",
        "RIKEN BRC",
        "KMPC",
        "Kmpc",
        "3i",
        "IMPC",
    }
    EUROPHENOME_VALID_COLONIES = {
        "EPD0013_1_G11_10613",
        "EPD0019_1_A05_10494",
        "EPD0023_1_F07_10481",
        "EPD0033_3_F04_10955",
        "EPD0037_1_E07_10471",
        "EPD0037_3_G01_10533",
        "EPD0039_1_B01_10470",
        "EPD0057_2_C02_10474",
        "EPD0065_2_E04_10968",
        "EPD0089_4_F11_10538",
        "EPD0100_4_A06_10472",
        "EPD0135_1_A05_10967",
        "EPD0156_1_B01_10970",
        "EPD0242_4_B03_10958",
        "EPD0011_3_B08_10331",
        "EPD0017_3_E02_71",
        "EPD0019_1_A05_10574",
        "EPD0023_1_F07_10553",
        "EPD0033_3_F04_10514",
        "EPD0037_1_B03_10395",
        "EPD0037_1_E07_10554",
        "EPD0038_2_B10_10557",
        "EPD0057_1_H01_10556",
        "EPD0057_2_C02_10549",
        "EPD0065_2_E04_10515",
        "EPD0065_5_A04_10523",
        "EPD0089_4_F11_320",
        "EPD0100_4_A06_10380",
        "EPD0135_1_A05_10581",
        "EPD0145_4_B09_10343",
        "EPD0156_1_B01_10099",
        "EPD0242_4_B03_10521",
        "EPD0023_1_F07_10594",
        "EPD0037_1_B03_10632",
        "EPD0037_1_E07_10595",
        "EPD0038_2_B10_10026",
        "EPD0046_2_F02_216",
        "EPD0057_1_H01_134",
        "EPD0057_2_C02_10630",
        "EPD0065_2_E04_10028",
        "EPD0065_5_A04_141",
        "EPD0089_4_F11_10578",
        "EPD0100_4_A06_10519",
        "EPD0135_1_A05_10631",
        "EPD0156_1_B01_10517",
        "EPD0242_4_B03_10579",
        "EPD0011_3_B08_28",
        "EPD0013_1_G11_10560",
        "EPD0017_3_E02_10220",
        "EPD0019_1_A05_73",
        "EPD0033_3_F04_10232",
        "EPD0037_1_B03_10234",
        "EPD0037_3_G01_10649",
        "EPD0039_1_B01_157",
        "EPD0046_2_F02_10658",
        "EPD0135_1_A05_10562",
        "EPD0145_4_B09_10826",
        "EPD0242_4_B03_10233",
        "Dll1_C3H_113",
        "Dll1_C3H_10333",
        "EPD0059_2_C08_10660",
    }

    WEIGHT_PARAMETERS = [
        "BCMLA_ABR_001_001",
        "BCMLA_DXA_001_001",
        "BCMLA_GRS_003_001",
        "BCMLA_PAT_049_002",
        "BCMLA_HWT_007_001",
        "BCMLA_CAL_001_001",
        "BCMLA_IPG_001_001",
        "BCMLA_OWT_001_001",
        "IMPC_ABR_001_001",
        "IMPC_DXA_001_001",
        "IMPC_CHL_001_001",
        "IMPC_GRS_003_001",
        "IMPC_PAT_049_002",
        "IMPC_HWT_007_001",
        "IMPC_CAL_001_001",
        "IMPC_IPG_001_001",
        "IMPC_OWT_001_001",
        "CCP_LFO_001_001",
        "IMPC_PAT_049_001",
        "HMGU_ROT_004_001",
        "HMGULA_DXA_001_001",
        "HMGULA_DYS_067_001",
        "HMGULA_GRS_003_001",
        "HMGULA_PAT_049_002",
        "HMGULA_HWT_007_001",
        "HMGULA_CAL_001_001",
        "HMGULA_OWT_001_001",
        "HMGULA_ROT_004_001",
        "HMGULA_SHI_001_001",
        "HMGULA_VDR_004_001",
        "HRWL_HOT_001_001",
        "HRWLLA_DXA_001_001",
        "HRWLLA_GRS_003_001",
        "HRWLLA_PAT_049_002",
        "HRWLLA_IPG_001_001",
        "HRWLLA_HWT_007_001",
        "ICS_HOT_002_001",
        "ICS_ROT_004_001",
        "ICSLA_ABR_001_001",
        "ICSLA_DXA_001_001",
        "ICSLA_GRS_003_001",
        "ICSLA_PAT_049_002",
        "ICSLA_HWT_007_001",
        "ICSLA_HOT_002_001",
        "ICSLA_CAL_001_001",
        "ICSLA_IPG_001_001",
        "ICSLA_ROT_004_001",
        "JAXLA_DXA_001_001",
        "JAXLA_GRS_003_001",
        "JAXLA_PAT_049_002",
        "JAXLA_HWT_007_001",
        "JAXLA_IPG_001_001",
        "KMPCLA_ABR_001_001",
        "KMPCLA_DXA_001_001",
        "KMPCLA_GRS_003_001",
        "KMPCLA_PAT_049_002",
        "KMPCLA_HWT_007_001",
        "KMPCLA_CAL_001_001",
        "KMPCLA_IPG_001_001",
        "MGP_IPG_001_001",
        "NINGLA_ABR_001_001",
        "NINGLA_DXA_001_001",
        "NINGLA_GRS_003_001",
        "NINGLA_PAT_049_002",
        "NINGLA_HWT_007_001",
        "NINGLA_CAL_001_001",
        "NINGLA_IPG_001_001",
        "RBRCIP_ABR_001_001",
        "RBRCLA_ABR_001_001",
        "RBRCLA_DXA_001_001",
        "RBRCLA_GRS_003_001",
        "RBRCLA_PAT_049_002",
        "RBRCLA_HWT_007_001",
        "RBRCLA_CAL_001_001",
        "RBRCLA_IPG_001_001",
        "RBRCLA_OWT_001_001",
        "TCPIP_GRS_003_001",
        "TCPLA_DXA_001_001",
        "TCPLA_GRS_003_001",
        "TCPLA_PAT_049_002",
        "TCPLA_HWT_007_001",
        "TCPLA_IPG_001_001",
        "TCP_CHL_001_001",
        "UCDIP_GRS_003_001",
        "UCDLA_DXA_001_001",
        "UCDLA_GRS_003_001",
        "UCDLA_PAT_049_002",
        "UCDLA_HWT_007_001",
        "UCDLA_IPG_001_001",
        "UCD_OWT_001_001",
        "ESLIM_001_001_001",
        "ESLIM_002_001_001",
        "ESLIM_003_001_001",
        "ESLIM_004_001_001",
        "ESLIM_005_001_001",
        "ESLIM_009_001_003",
        "ESLIM_010_001_003",
        "ESLIM_011_001_011",
        "ESLIM_012_001_005",
        "ESLIM_013_001_018",
        "ESLIM_020_001_001",
        "ESLIM_022_001_001",
        "GMC_900_001_001",
        "GMC_902_001_003",
        "GMC_908_001_001",
        "GMC_909_001_002",
        "GMC_912_001_018",
        "GMC_914_001_001",
        "GMC_916_001_022",
        "GMC_917_001_001",
        "GMC_920_001_001",
        "GMC_921_001_002",
        "GMC_922_001_002",
        "GMC_923_001_001",
        "GMC_926_001_003",
        "M-G-P_003_001_001",
        "M-G-P_004_001_001",
        "M-G-P_005_001_001",
        "M-G-P_009_001_003",
        "M-G-P_012_001_005",
        "M-G-P_013_001_018",
        "M-G-P_020_001_001",
        "M-G-P_022_001_001",
    ]

    BODY_WEIGHT_CURVE_PARAMETERS = {
        "IMPC_BWT_008_001": {
            "parameters": [
                "IMPC_GRS_003_001",
                "IMPC_CAL_001_001",
                "IMPC_DXA_001_001",
                "IMPC_HWT_007_001",
                "IMPC_PAT_049_001",
                "IMPC_BWT_001_001",
                "IMPC_ABR_001_001",
                "IMPC_CHL_001_001",
                "TCP_CHL_001_001",
                "HMGU_ROT_004_001",
            ],
            "procedure_stable_id": "IMPC_BWT_001",
            "procedure_group": "IMPC_BWT",
            "procedure_name": "Body Weight",
            "parameter_name": "Body weight curve",
        },
        "ESLIM_022_001_701": {
            # "parameters": [
            #     "ESLIM_022_001_703",
            #     "ESLIM_022_001_704",
            #     "ESLIM_022_001_705",
            #     "ESLIM_022_001_706",
            #     "ESLIM_022_001_707",
            #     "ESLIM_022_001_708",
            # ],
            "parameters": [
                "ESLIM_001_001_001",
                "ESLIM_002_001_001",
                "ESLIM_003_001_001",
                "ESLIM_004_001_001",
                "ESLIM_005_001_001",
                "ESLIM_020_001_001",
            ],
            "procedure_stable_id": "ESLIM_022_001",
            "procedure_group": "ESLIM_022",
            "procedure_name": "Body Weight",
            "parameter_name": "Body Weight Curve Pipeline One",
        },
        "ESLIM_022_001_702": {
            # "parameters": [
            #     "ESLIM_022_001_709",
            #     "ESLIM_022_001_710",
            #     "ESLIM_022_001_711",
            #     "ESLIM_022_001_712",
            #     "ESLIM_022_001_713",
            #     "ESLIM_022_001_001",
            # ],
            "parameters": [
                "ESLIM_009_001_003",
                "ESLIM_010_001_003",
                "ESLIM_011_001_011",
                "ESLIM_012_001_005",
                "ESLIM_013_001_018",
                "ESLIM_022_001_001",
            ],
            "procedure_stable_id": "ESLIM_022_001",
            "procedure_group": "ESLIM_022",
            "procedure_name": "Body Weight",
            "parameter_name": "Body Weight Curve Pipeline Two",
        },
    }

    # IMPC_BWT_008_001
    IMPC_BWT_BODY_WEIGHT_CURVE_PARAMETERS = [
        "IMPC_GRS_003_001",
        "IMPC_CAL_001_001",
        "IMPC_DXA_001_001",
        "IMPC_HWT_007_001",
        "IMPC_PAT_049_001",
        "IMPC_BWT_001_001",
        "IMPC_ABR_001_001",
        "IMPC_CHL_001_001",
        "TCP_CHL_001_001",
        "HMGU_ROT_004_001",
    ]

    # ESLIM_022_001_701
    ESLIM_701_BODY_WEIGHT_CURVE_PARAMETERS = [
        "ESLIM_001_001_001",
        "ESLIM_002_001_001",
        "ESLIM_003_001_001",
        "ESLIM_004_001_001",
        "ESLIM_005_001_001",
        "ESLIM_020_001_001",
    ]

    # ESLIM_022_001_702
    ESLIM_702_BODY_WEIGHT_CURVE_PARAMETERS = [
        "ESLIM_009_001_003",
        "ESLIM_010_001_003",
        "ESLIM_011_001_011",
        "ESLIM_012_001_005",
        "ESLIM_013_001_018",
        "ESLIM_022_001_001",
    ]

    CENTRE_ID_MAP = {
        "bcm": "BCM",
        "gmc": "HMGU",
        "h": "MRC Harwell",
        "harwell": "MRC Harwell",
        "hmgu": "HMGU",
        "ics": "ICS",
        "j": "JAX",
        "jax": "JAX",
        "ncom": "CMHD",
        "norcomm": "CMHD",
        "ning": "MARC",
        "marc": "MARC",
        "rbrc": "RBRC",
        "tcp": "TCP",
        "ucd": "UC Davis",
        "wtsi": "WTSI",
        "wsi": "WTSI",
        "kmpc": "KMPC",
        "biat": "BIAT",
        "ph": "PH",
        "cdta": "CDTA",
        "crl": "Crl",
        "riken brc": "RBRC",
        "ccp-img": "CCP-IMG",
        "ccpcz": "CCP-IMG",
        "ccp": "CCP-IMG",
        "monterotondo": "Monterotondo",
        "narlabs": "NARLabs",
    }

    PROJECT_ID_MAP = {
        "bash": "BaSH",
        "dtcc": "DTCC",
        "eumodic": "EUMODIC",
        "eucomm-eumodic": "EUMODIC",
        "eucomm-eucomm-eumodic": "EUMODIC",
        "helmholtz gmc": "Helmholtz GMC",
        "jax": "JAX",
        "ning": "MARC",
        "marc": "MARC",
        "mgp": "MGP",
        "mgp legacy": "MGP Legacy",
        "mrc": "MRC",
        "norcomm2": "NorCOMM2",
        "phenomin": "Phenomin",
        "riken brc": "RBRC",
        "kmpc": "KMPC",
        "3i": "3i",
        "impc": "IMPC",
        "ccp-img": "CCP-IMG",
        "norcomm": "NorCOMM",
        "ucd-komp": "UC Davis",
        "eucommtoolscre": "EUCOMMToolsCre",
        "monterotondo": "Monterotondo",
        "infrafrontier-i3": "Infrafrontier-I3",
        "komp": "KOMP",
        "narlabs": "NARLabs",
        "ccpcz": "CCP-IMG",
        "ccp": "CCP-IMG",
        "tobeloadedfromimits": "tobeloadedfromimits",
    }

    EXPERIMENTER_IDS = {
        "LHl": "131",
        "OH": "132",
        "jiangman, wangchenhao": "jiangman,wangchenhao",
        "jiangman wangchenhao": "jiangman,wangchenhao",
        "jianman  wangchenhao": "jiangman,wangchenhao",
        "JMC_301_304": "JMC301,JMC304",
        "JMC601,JMC602JMC603": "JMC601,JMC602,JMC603",
        "JCM601,JCM602,JCM603": "JMC601,JMC602,JMC603",
        "JCM601,JCM603": "JMC601,JMC603",
        "JMC601,JCM603": "JMC601,JMC603",
        "JCM602,JCM603": "JMC602,JMC603",
        "JMC602,JCM603": "JMC602,JMC603",
        "JCM603": "JMC603",
        "qixin;jiangman": "qixin,jiangman",
        "Chenhao Wang": "wangchenhao",
        "wangchenhao  jiangman": "wangchenhao,jiangman",
    }

    EFO_EMBRYONIC_STAGES = {
        "0": "EFO:0XXXXXX",
        "8.25": "EFO:0002561",
        "8.5": "EFO:85XXXXXX",
        "9": "EFO:0002561",
        "9.5": "EFO:0007641",
        "10.5": "EFO:0007643",
        "11.5": "EFO:0002562",
        "12": "EFO:0007640",
        "12.5": "EFO:0002563",
        "13": "EFO:0007642",
        "13.5": "EFO:0002564",
        "14.5": "EFO:0002565",
        "15.5": "EFO:0002566",
        "16.5": "EFO:0002567",
        "17.5": "EFO:0002568",
        "18": "EFO:0002569",
        "18.5": "EFO:0002570",
    }

    EXPERIMENT_TO_OBSERVATION_MAP = {
        "project_name": "experiment._project",
        "age_in_days": "experiment.ageInDays",
        "age_in_weeks": "experiment.ageInWeeks",
        "date_of_experiment": "experiment._dateOfExperiment",
        "metadata_group": "experiment.metadataGroup",
        "procedure_sequence_id": "experiment._sequenceID",
        "experiment_source_id": "experiment._experimentID",
        "external_sample_id": "specimen._specimenID",
        "sex": "specimen._gender",
        "allelic_composition": "specimen.allelicComposition",
        "production_center": "specimen._productionCentre",
        "phenotyping_center": "specimen._phenotypingCentre",
        "phenotyping_cons": "colony.phenotyping_consortium",
        "litter_id": "specimen._litterId",
        "date_of_birth": "specimen._DOB",
        "strain_accession_id": "strain.mgiStrainID",  ## Fallback to Imits
    }

    LINE_TO_OBSERVATION_MAP = {
        "project_name": "_project",
        "age_in_days": None,
        "age_in_weeks": None,
        "developmental_stage_name": None,
        "developmental_stage_acc": None,
        "date_of_experiment": None,
        "metadata_group": "metadataGroup",
        "procedure_sequence_id": None,
        "experiment_source_id": "_experimentID",
        "external_sample_id": None,
        "sex": None,
        "allelic_composition": "allelicComposition",
        "production_center": None,
        "phenotyping_center": "colony.phenotyping_centre",
        "phenotyping_cons": "colony.phenotyping_consortium",
        "litter_id": None,
        "date_of_birth": None,
        "specimen_source_file": None,
        "strain_accession_id": "strain.mgiStrainID",
        "strain_name": "colony.colony_background_strain",
        "allele_symbol": "colony.allele_symbol",
        "gene_symbol": "colony.marker_symbol",
        "gene_accession_id": "colony.mgi_accession_id",
        "genetic_background": "colony.genetic_background",
        "colony_id": "_colonyID",
        "weight": None,
        "weight_date": None,
        "weight_days_old": None,
        "weight_parameter_stable_id": None,
    }

    OBSERVATION_COLUMNS = [
        "experiment_source_file",
        "specimen_source_file",
        "experiment_id",
        "specimen_id",
        "observation_id",
        "allele_accession_id",
        "gene_accession_id",
        "project_name",
        "strain_accession_id",
        "litter_id",
        "phenotyping_center",
        "phenotyping_cons",
        "external_sample_id",
        "developmental_stage_name",
        "developmental_stage_acc",
        "datasource_name",
        "age_in_days",
        "date_of_birth",
        "metadata",
        "metadata_group",
        "procedure_sequence_id",
        "sequence_id",
        "experiment_source_id",
        "gene_symbol",
        "biological_sample_group",
        "sex",
        "allele_symbol",
        "production_center",
        "age_in_weeks",
        "weight",
        "weight_date",
        "weight_days_old",
        "weight_parameter_stable_id",
        "colony_id",
        "zygosity",
        "allelic_composition",
        "pipeline_name",
        "pipeline_stable_id",
        "procedure_name",
        "procedure_stable_id",
        "procedure_group",
        "parameter_name",
        "parameter_stable_id",
        "parameter_status",
        "observation_type",
        "data_point",
        "text_value",
        "category",
        "strain_name",
        "genetic_background",
        "date_of_experiment",
        "sub_term_name",
        "sub_term_id",
        "sub_term_description",
        "discrete_point",
        "time_point",
        "download_file_path",
        "file_type",
        "image_link",
        "increment_value",
        "parameter_association_stable_id",
        "parameter_association_sequence_id",
        "parameter_association_name",
        "parameter_association_value",
    ]

    PARAMETER_SPECIFIC_FIELDS = {
        "data_point": StringType(),
        "text_value": StringType(),
        "category": StringType(),
        "sequence_id": StringType(),
        "sub_term_name": ArrayType(StringType()),
        "sub_term_id": ArrayType(StringType()),
        "sub_term_description": ArrayType(StringType()),
        "discrete_point": StringType(),
        "time_point": StringType(),
        "download_file_path": StringType(),
        "image_link": StringType(),
        "file_type": StringType(),
        "increment_value": StringType(),
        "parameter_association_stable_id": ArrayType(StringType()),
        "parameter_association_sequence_id": ArrayType(StringType()),
        "parameter_association_name": ArrayType(StringType()),
        "parameter_association_value": ArrayType(StringType()),
    }

    DATE_FORMATS = [
        "yyyy-MM-dd'T'HH:mm:ssXXX",
        "yyyy-MM-dd'T'HH:mm:ssX",
        "yyyy-MM-dd'T'HH:mm:ssZ",
        "yyyy-MM-dd' 'HH:mm:ssZ",
        "yyyy-MM-dd'T'HH:mm:ss'Z'",
        "yyyy-MM-dd' 'HH:mm:ss'Z'",
        "yyyy-MM-dd'T'HH:mm:ss",
        "yyyy-MM-dd' 'HH:mm:ss",
        "yyyy-MM-dd' 'HH:mm",
    ]

    FEMALE_LINE_PARAMETERS = [
        "IMPC_FER_019_001",
        "IMPC_FER_011_001",
        "IMPC_FER_010_001",
        "IMPC_FER_012_001",
        "IMPC_FER_013_001",
        "IMPC_VIA_026_001",
        "IMPC_VIA_036_001",
        "IMPC_VIA_038_001",
        "IMPC_VIA_039_001",
        "IMPC_VIA_042_001",
        "IMPC_VIA_044_001",
        "IMPC_VIA_046_001",
        "IMPC_VIA_048_001",
        "IMPC_VIA_050_001",
        "IMPC_VIA_052_001",
        "IMPC_VIA_054_001",
        "IMPC_VIA_056_001",
        "IMPC_VIA_062_001",
        "IMPC_VIA_064_001",
    ]

    MALE_LINE_PARAMETERS = [
        "IMPC_FER_001_001",
        "IMPC_FER_007_001",
        "IMPC_FER_006_001",
        "IMPC_FER_008_001",
        "IMPC_FER_009_001",
        "IMPC_VIA_035_001",
        "IMPC_VIA_037_001",
        "IMPC_VIA_041_001",
        "IMPC_VIA_043_001",
        "IMPC_VIA_045_001",
        "IMPC_VIA_047_001",
        "IMPC_VIA_061_001",
        "IMPC_VIA_049_001",
        "IMPC_VIA_051_001",
        "IMPC_VIA_053_001",
        "IMPC_VIA_055_001",
        "IMPC_VIA_061_001",
        "IMPC_VIA_063_001",
        "IMPC_VIA_065_001",
    ]

    HET_LINE_PARAMETERS = [
        "IMPC_VIA_043_001",
        "IMPC_VIA_044_001",
        "IMPC_VIA_051_001",
        "IMPC_VIA_052_001",
        "IMPC_VIA_059_001",
        "IMPC_VIA_066_001",
    ]

    HOM_LINE_PARAMETERS = [
        "IMPC_VIA_045_001",
        "IMPC_VIA_046_001",
        "IMPC_VIA_053_001",
        "IMPC_VIA_054_001",
        "IMPC_VIA_060_001",
        "IMPC_VIA_063_001",
        "IMPC_VIA_064_001",
        "IMPC_VIA_067_001",
    ]

    HEM_LINE_PARAMETERS = ["IMPC_VIA_047_001", "IMPC_VIA_055_001", "IMPC_VIA_065_001"]

    ANZ_LINE_PARAMETERS = ["IMPC_VIA_048_001", "IMPC_VIA_056_001"]

    ZYG_NA_LINE_PARAMETERS = [
        "IMPC_VIA_057_001",
        "IMPC_VIA_061_001",
        "IMPC_VIA_062_001",
    ]

    EUROPHENOME_DERIVATIONS = [
        # ESLIM_011 derivations
        {
            "europhenomeParameter": "ESLIM_011_001_701",
            "europhenomeDerivation": "mul(div(sub('ESLIM_011_001_006', 'ESLIM_011_001_007'), 'ESLIM_011_001_006'), 100)",
        },
        {
            "europhenomeParameter": "ESLIM_011_001_702",
            "europhenomeDerivation": "mul(div(sub('ESLIM_011_001_006', 'ESLIM_011_001_008'), 'ESLIM_011_001_006'), 100)",
        },
        {
            "europhenomeParameter": "ESLIM_011_001_703",
            "europhenomeDerivation": "mul(div(sub('ESLIM_011_001_006', 'ESLIM_011_001_009'), 'ESLIM_011_001_006'), 100)",
        },
        {
            "europhenomeParameter": "ESLIM_011_001_704",
            "europhenomeDerivation": "mul(div(sub('ESLIM_011_001_006', 'ESLIM_011_001_010'), 'ESLIM_011_001_006'), 100)",
        },
        {
            "europhenomeParameter": "ESLIM_011_001_705",
            "europhenomeDerivation": "mul(div(sub('ESLIM_011_001_006', div(sum('ESLIM_011_001_007','ESLIM_011_001_008','ESLIM_011_001_009','ESLIM_011_001_010'),4)),'ESLIM_011_001_006'),100)",
        },
        # ESLIM_009 derivations
        {
            "europhenomeParameter": "ESLIM_009_001_701",
            "europhenomeDerivation": "meanOfIncrements('ESLIM_009_001_001')",
        },
        {
            "europhenomeParameter": "ESLIM_009_001_702",
            "europhenomeDerivation": "meanOfIncrements('ESLIM_009_001_002')",
        },
        {
            "europhenomeParameter": "ESLIM_009_001_703",
            "europhenomeDerivation": "div(meanOfIncrements('ESLIM_009_001_001'), 'ESLIM_009_001_003')",
        },
        {
            "europhenomeParameter": "ESLIM_009_001_704",
            "europhenomeDerivation": "div(meanOfIncrements('ESLIM_009_001_002'), 'ESLIM_009_001_003')",
        },
        # ESLIM_005 derivations
        {
            "europhenomeParameter": "ESLIM_005_001_701",
            "europhenomeDerivation": "div('ESLIM_005_001_005', 'ESLIM_005_001_001')",
        },
        {
            "europhenomeParameter": "ESLIM_005_001_702",
            "europhenomeDerivation": "div('ESLIM_005_001_003', 'ESLIM_005_001_001')",
        },
        {
            "europhenomeParameter": "ESLIM_005_001_703",
            "europhenomeDerivation": "div('ESLIM_005_001_002', 'ESLIM_005_001_001')",
        },
        {
            "europhenomeParameter": "ESLIM_005_001_704",
            "europhenomeDerivation": "div('ESLIM_005_001_005', 'ESLIM_005_001_004')",
        },
        # ESLIM_004 derivations
        {
            "europhenomeParameter": "ESLIM_004_001_701",
            "europhenomeDerivation": "areaUnderCurve('ESLIM_004_001_002')",
        },
    ]

    PROCEDURE_LIFE_STAGE_MAPPER = [
        {
            "lifeStage": "E9.5",
            "lifeStageAcc": "IMPCLS:0001",
            "procedures": ["GEL_", "EVL_", "HPL_", "EOL_", "EML_", "HEL_", "GPL_"],
        },
        {
            "lifeStage": "E12.5",
            "lifeStageAcc": "IMPCLS:0002",
            "procedures": ["GEM_", "ELZ_", "GPM_", "EVM_"],
        },
        {
            "lifeStage": "E15.5",
            "lifeStageAcc": "IMPCLS:0003",
            "procedures": ["EVO", "GPO", "MAA_", "EMO_", "GEO_"],
        },
        {
            "lifeStage": "E18.5",
            "lifeStageAcc": "IMPCLS:0004",
            "procedures": ["EVP", "EMA", "GEP_", "GPP_"],
        },
        {
            "lifeStage": "Middle aged adult",
            "lifeStageAcc": "IMPCLS:0006",
            "procedures": ["IP_"],
        },
        {
            "lifeStage": "Late adult",
            "lifeStageAcc": "IMPCLS:0007",
            "procedures": ["LA_"],
        },
    ]

    UMASS_GENES = [
        "4933427D14Rik",
        "Actr8",
        "Alg14",
        "Ap2s1",
        "Atp2b1",
        "B4gat1",
        "Bc052040",
        "Bcs1l",
        "Borcs6",
        "Casc3",
        "Ccdc59",
        "Cenpo",
        "Clpx",
        "Dbr1",
        "Dctn6",
        "Ddx59",
        "Dnaaf2",
        "Dolk",
        "Elof1",
        "Exoc2",
        "Fastkd6",
        "Glrx3",
        "Hlcs",
        "Ipo11",
        "Isca1",
        "mars2",
        "Mcrs1",
        "med20",
        "Mepce",
        "Mrm3",
        "Mrpl22",
        "Mrpl3",
        "Mrpl44",
        "Mrps18c",
        "Mrps22",
        "Mrps25",
        "mtpap",
        "Nars2",
        "Ndufa9",
        "Ndufs8",
        "Orc6",
        "Pmpcb",
        "Pold2",
        "Polr1a",
        "Polr1d",
        "Ppp1r35",
        "Prim1",
        "Prpf4b",
        "Rab11a",
        "Ranbp2",
        "Rbbp4",
        "Riok1",
        "Rpain",
        "Sars",
        "Sdhaf2",
        "Ska2",
        "Snapc2",
        "Sptssa",
        "Strn3",
        "Timm22",
        "tmx2",
        "Tpk1",
        "Trit1",
        "Tubgcp4",
        "Ube2m",
        "Washc4",
        "Ylpm1",
        "Zc3h4",
        "Zfp407",
        "Zwint",
    ]

    IDG_GENES = [
        "MGI:1098687",
        "MGI:1197518",
        "MGI:87859",
        "MGI:87860",
        "MGI:1097689",
        "MGI:1891697",
        "MGI:109562",
        "MGI:2181676",
        "MGI:87911",
        "MGI:1338944",
        "MGI:2661081",
        "MGI:102806",
        "MGI:87912",
        "MGI:1338946",
        "MGI:1919363",
        "MGI:1889336",
        "MGI:2679274",
        "MGI:108449",
        "MGI:1277167",
        "MGI:1925810",
        "MGI:1917943",
        "MGI:1933736",
        "MGI:2451244",
        "MGI:2441837",
        "MGI:3041203",
        "MGI:106912",
        "MGI:1347095",
        "MGI:1924846",
        "MGI:2182728",
        "MGI:2685887",
        "MGI:1925499",
        "MGI:2182928",
        "MGI:1340051",
        "MGI:2446854",
        "MGI:1859670",
        "MGI:2685213",
        "MGI:2685955",
        "MGI:1916151",
        "MGI:2441732",
        "MGI:1929461",
        "MGI:2139714",
        "MGI:2441950",
        "MGI:2655562",
        "MGI:1274784",
        "MGI:87930",
        "MGI:99401",
        "MGI:99402",
        "MGI:99403",
        "MGI:1919391",
        "MGI:104773",
        "MGI:104774",
        "MGI:106673",
        "MGI:87934",
        "MGI:87936",
        "MGI:87937",
        "MGI:87938",
        "MGI:87939",
        "MGI:87965",
        "MGI:87964",
        "MGI:87966",
        "MGI:87977",
        "MGI:87978",
        "MGI:1860835",
        "MGI:87979",
        "MGI:2677491",
        "MGI:1916120",
        "MGI:2685080",
        "MGI:87986",
        "MGI:104874",
        "MGI:1345147",
        "MGI:103305",
        "MGI:1918731",
        "MGI:2449492",
        "MGI:2151224",
        "MGI:105062",
        "MGI:3045301",
        "MGI:2142149",
        "MGI:2387214",
        "MGI:2145890",
        "MGI:1346086",
        "MGI:88065",
        "MGI:1194915",
        "MGI:1100867",
        "MGI:2159339",
        "MGI:2652846",
        "MGI:1929259",
        "MGI:107202",
        "MGI:108028",
        "MGI:894678",
        "MGI:107168",
        "MGI:1859216",
        "MGI:1347010",
        "MGI:88123",
        "MGI:1347244",
        "MGI:1276121",
        "MGI:88144",
        "MGI:102845",
        "MGI:1346332",
        "MGI:2387588",
        "MGI:3580298",
    ]

    DERIVED_PARAMETER_BANLIST = []

    BACKGROUND_STRAIN_MAPPER = {
        "B6NTac": "C57BL/6NTac",
        "129/Sv": "129",
        "129S5": "129S5/SvEvBrd",
        "C57BL/6NTacDen": "C57BL/6Dnk",
        "C57BL/6JTyr": "C57BL/6Brd-Tyr<c-Brd>",
        "129P2": "129P2/OlaHsd",
        "B6J.129S2": "129S2",
        "129/SvEv": "129S/SvEv",
        "129SvJ-Iso": "129X1/SvJ",
        "C3H/NHG": "C3H",
        "129/SvPas": "129S2/SvPas",
        "C57BL/6NTac-ICS-USA(ImportedLive)": "C57BL/6NTac",
        "C57BL/6NTac-ICS-Denmark(ImportedLive)": "C57BL/6Dnk",
    }
