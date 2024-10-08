env=''
all: default

default: clean devDeps build

# submit-h: clean devDeps build
submit-h: clean build
	source venv/bin/activate && LUIGI_CONFIG_PATH='$(confFile)'  PYTHONPATH='.' PYSPARK_PYTHON=./environment/bin/python luigi --module impc_etl.workflow.main $(task) --workers 3

# submit-h: clean devDeps build
submit-h-daily: clean build createDailyLuigiCfg
	source venv/bin/activate && LUIGI_CONFIG_PATH='luigi-daily.cfg'  PYTHONPATH='.' PYSPARK_PYTHON=python36 luigi --module impc_etl.workflow.main $(task) --workers 3

# submit-h: clean devDeps build
submit-custom:
	source venv/bin/activate && LUIGI_CONFIG_PATH='$(confFile)'  PYTHONPATH='.' PYSPARK_PYTHON=python36 YARN_CONF_DIR=/homes/mi_hadoop/hadoop-yarn-conf/ luigi --module impc_etl.workflow.main $(task) --workers 2

submit-lsf: clean devDeps build
	source venv/bin/activate && LUIGI_CONFIG_PATH='luigi-lsf.cfg'  PYTHONPATH='.' luigi --module impc_etl.workflow.main $(task) --workers 3

submit-dev:
	LUIGI_CONFIG_PATH='luigi-dev.cfg'  PYTHONPATH='.' YARN_CONF_DIR='' luigi --module impc_etl.workflow.main $(task) --workers 2


.venv:          ##@environment Create a venv
	if [ ! -e "venv/bin/activate" ] ; then $(PYTHON) -m venv --clear venv ; fi
	source venv/bin/activate && pip install --upgrade pip

lint:           ##@best_practices Run pylint against the main script and the shared, jobs and test folders
	source .venv/bin/activate && pylint -r n impc_etl/main.py impc_etl/shared/ impc_etl/jobs/ tests/

build: clean        ##@deploy Build to the dist package
#	mkdir ./dist$(env)#
#	zip -x main.py -r ./dist$(env)/impc_etl.zip impc_etl
#	cd ./dist$(env) && mkdir libs
#	source venv/bin/activate && pip install --upgrade pip
#	source venv/bin/activate && pip install -U -r requirements/common.txt -t ./dist$(env)/libs
#	source venv/bin/activate && pip install -U -r requirements/prod.txt -t ./dist$(env)/libs
#	cd ./dist$(env)/libs && zip -r ../libs.zip .
#	cd ./dist$(env) && rm -rf libs
	mkdir ./dist$(env)
	zip -x main.py -r ./dist$(env)/impc_etl.zip impc_etl
	source venv/bin/activate && pip install --upgrade pip
	source venv/bin/activate && pip install -r requirements/common.txt
	source venv/bin/activate && pip install -r requirements/prod.txt
	source venv/bin/activate && pip install venv-pack
	source venv/bin/activate && venv-pack -o ./dist/pyspark_venv.tar.gz

clean: clean-build clean-pyc clean-test           ##@clean Clean all

clean-build:           ##@clean Clean the dist folder
	rm -fr dist$(env)/

clean-pyc:           ##@clean Clean all the python auto generated files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:           ##@clean Clean the pytest cache
	rm -fr .pytest_cache

devDeps: .venv      ##@deps Create a venv and install common and dev dependencies
	source venv/bin/activate && pip install -U -r requirements/common.txt
	source venv/bin/activate && pip install -U -r requirements/dev.txt

prodDeps: .venv      ##@deps Create a venv and install common and prod dependencies
	source venv/bin/activate && pip install -U -r requirements/common.txt
	source venv/bin/activate && pip install -U -r requirements/prod.txt


devEnv: .venv devDeps
##	source .venv/bin/activate && pip install -U pre-commit
##	source .venv/bin/activate && pre-commit install --install-hooks

data:            ##@data Download and structure input data for the ETL. Parameters: staging-path (e.g. /nobackup/staging), dr-tag (e.g. dr15.0), input-data-path (e.g. /impc/), etl-host (e.g. hadoop-host), etl-dir (e.g. /user/impc/)
	cd $(raw-data-path) && mkdir $(dr-tag)
	cd $(raw-data-path)/$(dr-tag) && mkdir raw-data && mkdir solr
	cd $(raw-data-path)/$(dr-tag)/raw-data
	curl -u "ebi-exportdownloader:$(pass)" -X GET https://cloud.mousephenotype.org/remote.php/dav/files/ebi-exportdownloader/Exports/$(zipFile) --output $(raw-data-path)/$(dr-tag)/raw-data/$(zipFile)
	[ -f $(raw-data-path)/$(dr-tag)/raw-data/$(zipFile) ] && echo "$(zipFile) successfully downloaded." || echo "Unable to locate $(zipFile) provided!" && exit
	cd $(input-data-path)/dcc-data-archive && mkdir $(dr-tag)
	cp $(raw-data-path)/$(dr-tag)/raw-data/$(zipFile) $(input-data-path)/dcc-data-archive/$(dr-tag)
	tar xzvf  $(input-data-path)/dcc-data-archive/$(dr-tag)/$(zipFile) --directory $(input-data-path)/dcc-data-archive/$(dr-tag)/
	cd $(raw-data-path)
	chgrp phenomics $(raw-data-path)/$(dr-tag)
	chmod -R g+sw $(raw-data-path)/$(dr-tag)
	cd $(staging-path) && mkdir $(dr-tag)
	cd $(staging-path)/$(dr-tag) && mkdir tracking mgi ontologies xml parquet solr misc
	cd $(staging-path)/$(dr-tag)/xml && mkdir impc 3i europhenome pwg
	chgrp phenomics $(staging-path)/$(dr-tag)
	chmod -R g+sw $(staging-path)/$(dr-tag)
	curl https://www.gentar.org/tracker-api/api/reports/gene_interest > $(staging-path)/$(dr-tag)/tracking/gene_interest.tsv
	curl https://www.gentar.org/tracker-api/api/reports/phenotyping_colonies > $(staging-path)/$(dr-tag)/tracking/phenotyping_colonies.tsv
	cp -r $(input-data-path)/gentar-data-archive/product_reports/gentar-products-latest.tsv $(staging-path)/$(dr-tag)/tracking/gentar-products-latest.tsv
#	cp $(raw-data-path)/prep-area/gentar-products-latest.tsv $(staging-path)/$(dr-tag)/tracking/gentar-products-latest.tsv
	cp -r $(ontologies-path)/*  $(staging-path)/$(dr-tag)/ontologies/
	cp -r $(input-data-path)/ontologies-to-keep/* $(staging-path)/$(dr-tag)/ontologies/
	curl https://raw.githubusercontent.com/obophenotype/mouse-anatomy-ontology/master/emapa.obo > $(staging-path)/$(dr-tag)/ontologies/emapa.obo
	cp -r $(input-data-path)/3i-data-archive/*.xml $(staging-path)/$(dr-tag)/xml/3i/
	cp -r $(input-data-path)/pwg-data-archive/*.xml $(staging-path)/$(dr-tag)/xml/pwg/
	cp -r $(input-data-path)/pwg-data-archive/*.csv $(staging-path)/$(dr-tag)/misc/
	cp $(input-data-path)/3i-data-archive/flow_results_EBIexport_180119.csv $(staging-path)/$(dr-tag)/misc/
	cp -r $(input-data-path)/europhenome-data-archive/*.xml $(staging-path)/$(dr-tag)/xml/europhenome/
	cp -r $(input-data-path)/dcc-data-archive/$(dr-tag)/data/* $(staging-path)/$(dr-tag)/xml/impc/
	cd $(staging-path)/$(dr-tag)/xml/impc/ && find "$$PWD" -type f -name "*.xml" -exec bash -c ' DIR=$$( dirname "{}"  ); mv "{}" "$$DIR"_$$(basename "{}")  ' \;
	cd $(staging-path)/$(dr-tag)/xml/impc/normal && find "$$PWD" -type d -empty -delete
	cd $(staging-path)/$(dr-tag)/xml/impc/finalising && find "$$PWD" -type d -empty -delete
	curl http://www.informatics.jax.org/downloads/reports/MGI_Strain.rpt --output $(staging-path)/$(dr-tag)/mgi/MGI_Strain.rpt
	curl http://www.informatics.jax.org/downloads/reports/MGI_PhenotypicAllele.rpt --output $(staging-path)/$(dr-tag)/mgi/MGI_PhenotypicAllele.rpt
	curl http://www.informatics.jax.org/downloads/reports/MRK_List1.rpt --output $(staging-path)/$(dr-tag)/mgi/MRK_List1.rpt
	curl http://www.informatics.jax.org/downloads/reports/HGNC_AllianceHomology.rpt --output $(staging-path)/$(dr-tag)/mgi/HGNC_AllianceHomology.rpt
	curl http://www.informatics.jax.org/downloads/reports/MGI_GenePheno.rpt --output $(staging-path)/$(dr-tag)/mgi/MGI_GenePheno.rpt
	curl https://www.mousephenotype.org/embryoviewer/rest/ready --output $(staging-path)/$(dr-tag)/misc/embryo_data_og.json
	cd $(staging-path)/$(dr-tag)/misc/ && tr -d '\n' < embryo_data_og.json > embryo_data.json
	cd $(staging-path)/$(dr-tag)/misc/ && rm embryo_data_og.json
	scp -r $(staging-path)/$(dr-tag) $(etl-host):$(etl-dir)/


data-reports:
	@scp $(etl-host):$(etl-dir)/$(dr-tag)/output/drdr18.0_diff_csv/part-*.csv $(input-data-path)/$(dr-tag)/$(dr-tag)-$(prev-dr)-diff-report.csv
	@scp $(etl-host):$(etl-dir)/$(dr-tag)/output/mp_chooser_json/part-*.txt $(input-data-path)/$(dr-tag)/


email-data-reports:
	@scp mi_adm@codon-slurm-login:$(input-data-path)/$(dr-tag)/$(dr-tag)-$(prev-dr)-diff-report.csv $(staging-path)/$(dr-tag)/artefacts/$(dr-tag)-$(prev-dr)-diff-report.csv
	@scp mi_adm@codon-slurm-login:$(input-data-path)/$(dr-tag)/part-*.txt $(staging-path)/$(dr-tag)/artefacts/
	@scp mi_adm@codon-slurm-login:$(input-data-path)/data-archive/emails/* $(staging-path)/$(dr-tag)/artefacts/
	@python3 util/fill_in_dr_report_emails.py $(dr-tag) $(prev-dr) $(staging-path)/$(dr-tag)/artefacts/ $(etl-dir)


imaging-data-media: ## Create folder structure for the imaging data
	@if [ ! -d "$(input-data-path)/imaging-data-archive/$(dr-tag)" ]; then mkdir $(input-data-path)/imaging-data-archive/$(dr-tag) && chgrp phenomics $(input-data-path)/imaging-data-archive/$(dr-tag) && chmod -R g+sw $(input-data-path)/imaging-data-archive/$(dr-tag); fi
	@python3 imaging/RetrieveMediaUpdates.py $(dr-tag) $(input-data-path)/imaging-data-archive/media_data
	@if [ -f "$(input-data-path)/imaging-data-archive/media_data/$(dr-tag)_media_data.json" ]; then echo "Media data successfully retrieved."; else "Unable to retrieve media data"; fi


imaging-data-download:
	@if [ ! -d "$(staging-path)/$(dr-tag)/artefacts" ]; then mkdir $(staging-path)/$(dr-tag)/artefacts; fi
	@if [ ! -d "$(staging-path)/$(dr-tag)/artefacts/images_data" ]; then mkdir $(staging-path)/$(dr-tag)/artefacts/images_data; fi
	@if [ ! -d "$(staging-path)/$(dr-tag)/artefacts/media_data" ]; then mkdir $(staging-path)/$(dr-tag)/artefacts/media_data; fi
	@if [ ! -d "$(staging-path)/$(dr-tag)/images" ]; then mkdir $(staging-path)/$(dr-tag)/images; fi
	@if [ ! -d "$(staging-path)/$(dr-tag)/logs" ]; then mkdir $(staging-path)/$(dr-tag)/logs; fi
	@if [ -f "$(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json" ]; then rm -rf $(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json; fi

	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/media_data/* $(staging-path)/$(dr-tag)/artefacts/media_data/
	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/omero_dev.properties $(staging-path)/$(dr-tag)/artefacts/omero_dev.properties
	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/base_omero_image_data/image_data.list $(staging-path)/$(dr-tag)/artefacts/image_data.list
	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/base_omero_image_data/images_data/* $(staging-path)/$(dr-tag)/artefacts/images_data/
	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/dr_omero_image_data/* $(staging-path)/$(dr-tag)/artefacts/images_data/

	@python3 imaging/CreateImagingFolders.py $(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json $(staging-path)/$(dr-tag)/images/
	@python3 imaging/DownloadImages.py $(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json $(staging-path)/$(dr-tag)/artefacts/images_data $(staging-path)/$(dr-tag)/images/ $(staging-path)/$(dr-tag)/logs/$(dr-tag)_imagedownload.out


imaging-omero-upload-prep:
	@python imaging/CheckMissingDatasources.py $(staging-path)/$(dr-tag)/images $(staging-path)/$(dr-tag)/artefacts/ $(staging-path)/$(dr-tag)/artefacts/omero_dev.properties
	@python imaging/CreateCSVForUploadToOmero.py $(staging-path)/$(dr-tag)/images/ $(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json $(dr-tag) $(staging-path)/$(dr-tag)/artefacts/


imaging-omero-upload:
	@source /net/isilonP/public/rw/homes/mi_adm/.bash_profile && python imaging/UploadCSVToOmero.py $(dr-tag) $(staging-path)/$(dr-tag)/artefacts/ $(staging-path)/$(dr-tag)/images/ $(staging-path)/$(dr-tag)/logs/ $(staging-path)/$(dr-tag)/artefacts/omero_dev.properties $(clean-path) 2>&1


imaging-data-csv-check:
	@cp $(etl-dir)/$(dr-tag)/output/images_pipeline_input_csv/part-*.csv $(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_wo_omero_ids.csv
	@if [ -f "$(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_wo_omero_ids.csv" ]; then echo "CSV file successfully retrieved"; else "ERROR: The Pre-statistical analysis task did not produce a CSV file!"; fi


imaging-data-csv-process:
	@scp mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_wo_omero_ids.csv $(staging-path)/$(dr-tag)/artefacts/impc_images_input_wo_omero_ids.csv
	@if [ -f "$(staging-path)/$(dr-tag)/artefacts/impc_images_input_wo_omero_ids.csv" ]; then echo "CSV file successfully copied across for processing"; else "ERROR: Cannot find CSV file!" && exit -1; fi
	@export PYTHONPATH=$(staging-path)/$(dr-tag)/impc-etl && python3 imaging/CheckForMissingImagesInPipelineCSV.py $(dr-tag) $(staging-path)/$(dr-tag)/artefacts/impc_images_input_wo_omero_ids.csv $(staging-path)/$(dr-tag)/artefacts/media_data


imaging-data-add-omero-ids-and-wrapup:
	@PYTHONPATH=$(pwd):$PYTHONPATH
	@export PYTHONPATH=$(staging-path)/$(dr-tag)/impc-etl && python3 imaging/AddOmeroIdsToCSVFile.py $(staging-path)/$(dr-tag)/artefacts/impc_images_input_wo_omero_ids.csv $(staging-path)/$(dr-tag)/artefacts/impc_images_input_with_omero_ids.csv $(staging-path)/$(dr-tag)/artefacts/media_data $(staging-path)/$(dr-tag)/artefacts/images_data
	@scp $(staging-path)/$(dr-tag)/artefacts/impc_images_input_with_omero_ids.csv mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_with_omero_ids.csv
	@scp $(staging-path)/$(dr-tag)/artefacts/media_data/$(dr-tag)_media_data.json mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/media_data/$(dr-tag)_media_data.json
	@scp $(staging-path)/$(dr-tag)/artefacts/images_data/$(dr-tag)_imagedata.json mi_adm@codon-slurm-login:$(input-data-path)/imaging-data-archive/dr_omero_image_data/$(dr-tag)_imagedata.json


imaging-data-move-csv-to-hadoop:
	@if [ -f "$(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_with_omero_ids.csv" ]; then echo "Moving file to Hadoop"; else "ERROR: CSV file missing!" && exit -1; fi
	@scp $(input-data-path)/imaging-data-archive/$(dr-tag)/impc_images_input_with_omero_ids.csv $(etl-host):$(etl-dir)/$(dr-tag)/misc/impc_images_input_with_omero_ids.csv


imaging-omero-upload-check-pid:
	@python imaging/CheckUploadProcessStatus.py


imaging-omero-upload-check-status:
	@python3 imaging/CheckOmeroUploadStatus.py $(dr-tag) $(staging-path)/$(dr-tag)/artefacts/


createProdLuigiCfg:       ##@build Generates a new luigi-prod.cfg file from the luigi.cfg.template a using a new dr-tag, remember to create luigi.cfg.template file first, parameter: dr-tag (e.g. dr15.0)
	sed 's/%DR_TAG%/$(dr-tag)/' luigi.cfg.template > luigi-prod.cfg

createDailyLuigiCfg:       ##@build Generates a new luigi-prod.cfg file from the luigi.cfg.template a using a new dr-tag, remember to create luigi.cfg.template file first, parameter: dr-tag (e.g. dr15.0)
	sed 's/%DR_TAG%/$(dr-tag)/' luigi.cfg.template > luigi-daily.cfg

test:       ##@best_practices Run pystest against the test folder
	source venv/bin/activate && pytest


 HELP_FUN = \
		 %help; \
		 while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^(\w+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/ }; \
		 print "usage: make [target]\n\n"; \
	 for (keys %help) { \
		 print "$$_:\n"; $$sep = " " x (20 - length $$_->[0]); \
		 print "  $$_->[0]$$sep$$_->[1]\n" for @{$$help{$$_}}; \
		 print "\n"; }


help:
	@echo "Run 'make' without a target to clean all, install dev dependencies, test, lint and build the package \n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)