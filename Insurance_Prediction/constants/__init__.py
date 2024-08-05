import os
from datetime import date
from urllib.parse import quote_plus


# secure_bundle_path = r'C:\Users\pramod\Desktop\INURON\Internship\Insurance_Premium_Prediction\research\secure-connect-insurance.zip'
# token_path = r'C:\Users\pramod\Desktop\INURON\Internship\Insurance_Premium_Prediction\research\Insurance-token.json'



ASTRA_DB_SECURE_BUNDLE_PATH = r'C:\Users\pramod\Desktop\INURON\Internship\Insurance_Premium_Prediction\research\secure-connect-insurance.zip'
ASTRADB_APPLICATION_TOKEN = r'C:\Users\pramod\Desktop\INURON\Internship\Insurance_Premium_Prediction\research\Insurance-token.json'

PIPELINE_NAME: str = "insurance"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "expenses"
# CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "insurance.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
# DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
TABLE_NAME: str= "insurance_records"
DATA_INGESTION_KEYSPACE_NAME: str= "data_storage"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"


