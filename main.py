from src.cnnClassifier_benign_vs_malignant import logger
from src.cnnClassifier_benign_vs_malignant.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier_benign_vs_malignant.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model_obj = PrepareBaseModelTrainingPipeline()
    prepare_base_model_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e