from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_validation import DataValidation
from src.mlproject import logger

STAGE_NAME="Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_val=config.get_data_validation_config()
        data_validation=DataValidation(config=data_val)
        data_validation.validate_all_columns()


if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} STARTED...")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} COMPLETED...")

    except Exception as e:
        raise e

