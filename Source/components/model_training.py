import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from Source.Exception import CustomException
from Source.Logger import logging
import sys
import os
from Source.utils import evaluate_model,save_object
from dataclasses import dataclass
@dataclass
class ModelTrainerConfig:
    Model_Trainer_Path = os.path.join('artifacts','model.pkl')
class ModelTrainer:
    def __init__(self):
        self.model_trainer_path_data = ModelTrainerConfig()
    def initiate_model_training(self,train_arr,test_arr):
        try:
            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]            
)
            linear = LinearRegression()
            ridge = Ridge()
            lasso = Lasso()
            elastic = ElasticNet()
            models = {
            "linear" : linear,
            "ridge" : ridge,
            "lasso" : lasso,
            "elasticnet" : elastic
}
            model_report = evaluate_model(x_train,y_train,x_test,y_test,models)
            print(model_report)
            logging.info(f"model report: {model_report}")
            #To get best model score
            best_score = max((model_report.values()))
            best_model = list(model_report.keys())[list(model_report.values()).index(best_score)]
            best_model_name = models[best_model]
            print(f"Best Model was {best_model_name} and r2_score is {best_score} ")
            print("-"*30)
            logging.info(f"Best Model was {best_model_name} and r2_score is {best_score} ")
            save_object(
                file_path = self.model_trainer_path_data.Model_Trainer_Path,
                obj = best_model_name
            )
        except Exception as e:
            logging.info("Error ar model_training file")
            raise CustomException(e,sys)

