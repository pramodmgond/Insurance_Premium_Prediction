
from Insurance_Prediction.logger import logging
from Insurance_Prediction.exception import InsuranceException
import sys 

from Insurance_Prediction.pipeline.training_pipeline import TrainPipeline

from Insurance_Prediction.data_access.insurance_data import InsuranceData


# try :
#     a = 10/"the"
# except Exception as e :
#     logging.info(e)
#     raise InsuranceException(e, sys) from e 

# pipline  = TrainPipeline()
# pipline.run_pipeline()

# if __name__ == "__main__":
#     try:
#         insurance_data = InsuranceData()
#         df = insurance_data.export_collection_as_dataframe("insurance_records")
#         print(df.head())
#     except InsuranceException as ie:
#         print(f"Insurance Exception occurred: {ie}")


# import os
# from Insurance_Prediction.entity.config_entity import DataIngestionConfig
# from Insurance_Prediction.components.data_ingestion_old import DataIngestion
# from Insurance_Prediction.exception import InsuranceException
# import logging

# def main():
#     try:
#         logging.basicConfig(level=logging.INFO)

#         # Create a DataIngestionConfig instance with default or customized settings
#         data_ingestion_config = DataIngestionConfig()

#         # Initialize DataIngestion instance with the config
#         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

#         # Call the export_data_into_feature_store method to create artifact folder and save CSV file
#         dataframe = data_ingestion.export_data_into_feature_store()

#         # Verify if the CSV file is created and the dataframe is not empty
#         if os.path.exists(data_ingestion_config.feature_store_file_path):
#             logging.info(f"CSV file created successfully at {data_ingestion_config.feature_store_file_path}")
#         else:
#             logging.error(f"CSV file was not created at {data_ingestion_config.feature_store_file_path}")

#         if not dataframe.empty:
#             logging.info("DataFrame is not empty, data ingestion successful.")
#         else:
#             logging.error("DataFrame is empty, data ingestion failed.")

#     except InsuranceException as e:
#         logging.error(f"InsuranceException occurred: {e}")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()

# import os
# import sys
# import logging
# from Insurance_Prediction.entity.config_entity import DataIngestionConfig
# from Insurance_Prediction.components.data_ingestion_old import DataIngestion
# from Insurance_Prediction.exception import InsuranceException
# import pandas as pd

# def main():
#     try:
#         logging.basicConfig(level=logging.INFO)

#         # Create a DataIngestionConfig instance with default or customized settings
#         data_ingestion_config = DataIngestionConfig()

#         # Initialize DataIngestion instance with the config
#         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

#         # Call the export_data_into_feature_store method to create artifact folder and save CSV file
#         dataframe = data_ingestion.export_data_into_feature_store()

#         # Verify if the CSV file is created and the dataframe is not empty
#         if os.path.exists(data_ingestion_config.feature_store_file_path):
#             logging.info(f"CSV file created successfully at {data_ingestion_config.feature_store_file_path}")
#         else:
#             logging.error(f"CSV file was not created at {data_ingestion_config.feature_store_file_path}")

#         if not dataframe.empty:
#             logging.info("DataFrame is not empty, data ingestion successful.")
            
#             # Call split_data_as_train_test method
#             data_ingestion.split_data_as_train_test(dataframe)

#             # Verify if the training and testing CSV files are created
#             if os.path.exists(data_ingestion_config.training_file_path):
#                 logging.info(f"Training CSV file created successfully at {data_ingestion_config.training_file_path}")
#             else:
#                 logging.error(f"Training CSV file was not created at {data_ingestion_config.training_file_path}")

#             if os.path.exists(data_ingestion_config.testing_file_path):
#                 logging.info(f"Testing CSV file created successfully at {data_ingestion_config.testing_file_path}")
#             else:
#                 logging.error(f"Testing CSV file was not created at {data_ingestion_config.testing_file_path}")
#         else:
#             logging.error("DataFrame is empty, data ingestion failed.")

#     except InsuranceException as e:
#         logging.error(f"InsuranceException occurred: {e}")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()

import logging
from Insurance_Prediction.entity.config_entity import DataIngestionConfig
from Insurance_Prediction.data_access.insurance_data import InsuranceData
from Insurance_Prediction.components.data_ingestion_old import DataIngestion
from Insurance_Prediction.logger import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        logging.info("Starting data ingestion process")
        
        # Initialize data ingestion config
        data_ingestion_config = DataIngestionConfig()

        # Initialize data ingestion object
        data_ingestion = DataIngestion(data_ingestion_config)

        # Initiate data ingestion
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        logging.info(f"Data ingestion completed successfully. Artifacts: {data_ingestion_artifact}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
