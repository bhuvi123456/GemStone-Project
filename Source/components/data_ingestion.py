import os
from Source.Logger import logging
from Source.Exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import sys
from Source.components.data_transformation import DataTransformation
#Whenever we are creating classes if no need to perform __init__ method to initialize the objects or variables 
# dataclass can use
#Initialize Data Ingestion Configuration
#In data ingestion input is path to the data and output should be train data and test data
@dataclass
class DataIngestionConfig:
    train_path : str = os.path.join('artifacts','train.csv')
    test_path : str= os.path.join('artifacts','test.csv')
    raw_path : str = os.path.join('artifacts','raw.csv')
#Above we are intialized the input
class DataIngestion:
    def __init__(self):
        self.ingestion_config_data = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("My data ingestion process starts")
        try:
            df = pd.read_csv('notebooks/Data/GemStone.csv')
            logging.info("Dataset read from pandas")
            os.makedirs(os.path.dirname(self.ingestion_config_data.raw_path),exist_ok=True)
            #df.to_csv(self.ingestion_config_data.raw_path,index = False) #to prevent getting index one more time
            train_set,test_set = train_test_split(df,test_size = 0.3)
            train_set.to_csv(self.ingestion_config_data.train_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config_data.test_path,index = False,header = True)
            logging.info("Data Ingestion is completed")
            return (
                self.ingestion_config_data.train_path,
                self.ingestion_config_data.test_path
            )
        except Exception as e:
            logging.info("Error Occurs")
            raise CustomException(e,sys)
if __name__ == '__main__':
    obj  = DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.complete_data_transformation(train_path,test_path)