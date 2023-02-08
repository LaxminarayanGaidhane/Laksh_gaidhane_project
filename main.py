from Insurance_machine_learning import logging
from Insurance_machine_learning.exception import Insurance_machine_learning_Exception
import os,sys
from Insurance_machine_learning.utils import get_collection_as_dataframe
from Insurance_machine_learning.entity.config_entity import DataIngestionConfig
from Insurance_machine_learning.entity import config_entity

#def test_logger_and_exception():
    # try:
    #     logging.info("Starting the test_logger_and_exception")
    #     result = 3/0
    #     print(result)
    #     logging.info("Ending point of the test_logger_and_exception")
    # except Exception as e:
    #     logging.debug(str(e))
    #     raise Insurance_machine_learning_Exception(e,sys)

if __name__ == "__main__":
    try:
        # start_training_pipeline
        # test_logger_and_exception()
        # get_collection_as_dataframe(database_name = "INSURANCE",collection_name = "INSURANCE_PROJECT")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)

