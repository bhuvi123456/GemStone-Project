import sys
import os
import pickle
import numpy as np
import pandas as pd
from Source.Exception import CustomException
from Source.Logger import logging
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as file:
            pickle.dump(obj,file)
        logging.info(f"Object saved successfully to {file_path}")
        logging.info(f"File size: {os.path.getsize(file_path)} bytes")
    except Exception as e:
        raise CustomException(e,sys)
logging.info("Splitting the data into 4 ")

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report = {}
        for model_name,model_evaluation in models.items():
            model_evaluation.fit(x_train,y_train)
            y_pred = model_evaluation.predict(x_test)
            test_r2_score = r2_score(y_test,y_pred)
            report[model_name] = test_r2_score
            logging.info("Evaluated the model")
        return report
    except Exception as e:
        raise CustomException(e,sys)
def load_object(file_path):
    try:
        with open(file_path,'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException(e,sys)
    





