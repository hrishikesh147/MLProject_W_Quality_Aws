from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME="Data Ingestion"

try:
    logger.info(f"Starting stage: {STAGE_NAME}...")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} COMPLETED...")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME="Data Validation" 

try:
    logger.info(f"Stage {STAGE_NAME} STARTED...")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} COMPLETED...")

except Exception as e:
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e


STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e