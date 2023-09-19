from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion"

try:
    logger.info(f"Starting stage: {STAGE_NAME}...")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} COMPLETED...")
except Exception as e:
    logger.exception(e)
    raise e 