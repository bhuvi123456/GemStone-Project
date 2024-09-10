import os
from Source.Logger import logging
from Source.Exception import CustomException
import pandas as pd
from dataclasses import dataclass
import sys
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
from Source.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.Data_transformation_config_data = DataTransformationConfig()
    def initialize_data_transformation(self):
        try:
            logging.info("Data Transformation is initiated")
            num_features = df.select_dtypes(exclude = 'O').columns.drop('price')
            print('num_features:',list(num_features))
            cat_features = [features for features in df.columns if df[features].dtype == 'O']
            print("cat features:",cat_features)
            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            logging.info("Numeric PipeLine has started")
            numeric_pipeline = Pipeline([
        ("SimpleImputer:",SimpleImputer(strategy='median')),
        ("Scaler:",StandardScaler())]

)
            logging.info("Categoric Pipeline has started")
            categoric_pipeline = Pipeline(
    [
        ('SimpleImputer:',SimpleImputer(strategy = 'most_frequent')),
        ('OrdinalEncoder:',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
        ("StandardScaler:",StandardScaler()) #we are Performing scaling also because if i have 10 different data's in my 
        #categorical variable ten i will have ranking from 1 to 10 then to increase accuracy we use scaling to make it from 0 to 1
    ]
)
            logging.info("preprocessor has started")
            preprocessor  = ColumnTransformer(
    [
        ("numeric_pipeline:",numeric_pipeline,num_features),
        ("categoric_pipeline:", categoric_pipeline,cat_features)
        ]
)
            return preprocessor
            logging.info("preprocessor has ended")
        except Exception as e:
            logging.info("Error in Data Transformation")
            pass
            raise CustomException(e,sys)
    def complete_data_transformation(self,train_path,test_path):
        try:
            preprocessor_obj = self.initialize_data_transformation()
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test data done")
            logging.info(f"Train data of first 5 columns{train_df.head().to_string()}")
            logging.info(f"Test data of first 5 columns{test_df.head().to_string()}")
            input_feature_train_df = train_df.drop(columns=['price'],axis = 1)
            output_feature_train_df = train_df['price']
            input_feature_test_df = test_df.drop(columns = ['price'],axis = 1)
            output_feature_test_df = test_df['price']
            logging.info("Splitted the train and test_data")
            logging.info("preprocessing the Data")
            input_feature_train_df = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_df = preprocessor_obj.transform(input_feature_test_df)
            #if i have huge data then using pandas may take more time to load so we will convert into numpy
            train_arr = np.c_[input_feature_train_df,np.array(output_feature_train_df)]
            test_arr = np.c_[input_feature_test_df,np.array(output_feature_test_df)]
            save_object(
                file_path = self.Data_transformation_config_data.preprocessor_path,
                obj = preprocessor_obj
            )
            
            logging.info("Preprocessing Data is Saved")
            return (
                train_arr,
                test_arr,
                self.Data_transformation_config_data.preprocessor_path
            )

             

        except Exception as e:
            logging.info("Error occured at complete_data_transformation")
            raise CustomException(e,sys)


