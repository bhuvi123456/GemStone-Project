from Source.Exception import CustomException
from Source.Logger import logging
import sys
import os
import pandas as pd
from Source.components.data_ingestion import DataIngestion
from Source.components.model_training import ModelTrainer
from Source.components.data_transformation import DataTransformation
if __name__ == '__main__':
    obj  = DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.complete_data_transformation(train_path,test_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)