import shutil
import os,sys
import pandas as pd
from src.logger import logging

from src.exception import CustomException
import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

        
class PredictionPipeline:
    def __init__(self):
          pass



    def predict(self, features):
        try:
            #preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            #preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            ##data_scaled = preprocessor.transform(features)

            pred = model.predict(features)
            return pred

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 cement: float,
                 blast_furnace_slag: float,
                 fly_ash: float,
                 water: float,
                 superplasticizer: float,
                 coarse_aggregate: float,
                 fine_aggregate: float,
                 age: float):

        self.cement = cement
        self.blast_furnace_slag = blast_furnace_slag
        self.fly_ash = fly_ash
        self.water = water
        self.superplasticizer= superplasticizer
        self.coarse_aggregate = coarse_aggregate
        self.fine_aggregate = fine_aggregate
        self.age = age

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Cement (component 1)(kg in a m^3 mixture)': [self.cement],
                'Blast Furnace Slag (component 2)(kg in a m^3 mixture)': [self.blast_furnace_slag],
                'Fly Ash (component 3)(kg in a m^3 mixture)': [self.fly_ash],
                'Water  (component 4)(kg in a m^3 mixture)': [self.water],
                'Superplasticizer (component 5)(kg in a m^3 mixture)': [self.superplasticizer],
                'Coarse Aggregate  (component 6)(kg in a m^3 mixture)': [self.coarse_aggregate],
                'Fine Aggregate (component 7)(kg in a m^3 mixture)': [self.fine_aggregate],
                'Age (day)': [self.age]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e, sys)
