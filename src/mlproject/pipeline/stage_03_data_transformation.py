from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import train_test_split
from src.mlproject import logger
from pathlib import Path


STAGE_NAME="Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            
            else :
                raise Exception("The data schema is not correct...")

        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info("Data Transformation Stage started")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info (f"Stage {STAGE_NAME} COMPLETED...")
                    
    except Exception as e:
        raise e




