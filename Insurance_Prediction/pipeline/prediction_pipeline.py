import os
import sys

import numpy as np
import pandas as pd
from Insurance_Prediction.entity.config_entity import InsurancePredictorConfig
from Insurance_Prediction.entity.s3_estimator import InsuranceEstimator
from Insurance_Prediction.exception import InsuranceException
from Insurance_Prediction.logger import logging
from Insurance_Prediction.utils.main_utils import read_yaml_file
from pandas import DataFrame


class InsuranceData:
    def __init__(self,
                age,
                bmi,
                children,
                region,
                sex,
                smoker
                ):
        """
        Insurance Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.age = age
            self.bmi = bmi
            self.children = children
            self.region = region
            self.sex = sex
            self.smoker = smoker



        except Exception as e:
            raise InsuranceException(e, sys) from e



    def get_insurance_data_as_dict(self):
        """
        This function returns a dictionary from InsuranceData class input 
        """
        logging.info("Entered get_insurance_data_as_dict method as InsuranceData class")

        try:
            input_data = {
                "age": [self.age],
                "bmi": [self.bmi],
                "children": [self.children],
                "region": [self.region],
                "sex": [self.sex],
                "smoker": [self.smoker]
            }

            logging.info("Created Insurance data dict")

            logging.info("Exited get_insurance_data_as_dict method as InsuranceData class")

            return input_data

        except Exception as e:
            raise InsuranceException(e, sys) from e
        
    def get_insurance_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            insurance_input_dict = self.get_insurance_data_as_dict()
            return DataFrame(insurance_input_dict)
        
        except Exception as e:
            raise InsuranceException(e, sys) from e

class InsuranceRegressor:
    def __init__(self,prediction_pipeline_config: InsurancePredictorConfig = InsurancePredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise InsuranceException(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of InsuranceRegressor
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of InsuranceRegressor class")
            model = InsuranceEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise InsuranceException(e, sys)