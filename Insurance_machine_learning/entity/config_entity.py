import os , sys
from Insurance_machine_learning.exception import Insurance_machine_learning_Exception
from Insurance_machine_learning.logger import logging
from datetime import datetime


FILE_NAME = "insurance.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime("%m%d%Y__%H%M%S")}")
        except Exception as e:
            raise Insurance_machine_learning_Exception(e,sys)
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "Insurance"
            self.collection_name = "Premium"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
        except Exception as e:
            raise Insurance_machine_learning_Exception(e,sys)

# Convert data into Dict
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise Insurance_machine_learning_Exception(e,sys)


