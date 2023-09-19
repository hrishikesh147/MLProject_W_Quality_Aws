from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject import logger

STAGE_NAME="Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingest=config.get_data_ingestion_config()
        data=DataIngestion(config=data_ingest)
        data.download_file()
        data.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f"Starting stage: {STAGE_NAME}...")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED...")
    except Exception as e:
        logger.exception(e)
        raise e 

