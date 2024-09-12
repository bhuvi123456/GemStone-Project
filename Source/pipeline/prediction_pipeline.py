import sys
import os
from Source.Exception import CustomException
from Source.Logger import logging
from Source.utils import load_object
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            data_scaling = preprocessor.transform(features)
            pred = model.predict(data_scaling)
            return pred

        except Exception as e:
            logging.info("Error has occu red")
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,carat:float,table:float,cut:str,color:str,clarity:str):
        self.carat = carat
        self.table = table
        self.cut = cut
        self.color = color
        self.clarity = clarity
    def get_data_as_dataframe(self):
        try:
            custom_input_data = {
                'carat' : [self.carat],
                'table' : [self.table],
                'cut' : [self.cut],
                'color' : [self.color],
                'clarity' : [self.clarity]
            }
            df = pd.DataFrame(custom_input_data)
            return df
            logging.info("DataFrame was corrected")
        except Exception as e:
            logging.info("Error has Occured in prediction pipeline(get_data_as_dataframe)")
            raise CustomException(e,sys)