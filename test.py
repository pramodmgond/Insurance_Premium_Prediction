

# from Insurance_Prediction.configuration.connection import AstraDBClient
# from Insurance_Prediction.exception import InsuranceException
# from Insurance_Prediction.logger import logging
# from Insurance_Prediction.constants import  DATA_INGESTION_KEYSPACE_NAME,ASTRA_DB_SECURE_BUNDLE_PATH

 
# # Usage Example:
# if __name__ == "__main__":
#     try:
#         db_client = AstraDBClient()

#         # Example query execution
#         result = db_client.execute_query("SELECT * FROM insurance_records LIMIT 5")
#         if result:
#             for row in result:
#                 print(row)
#                 logging.info(f"Row: {row}")
#         else:
#             print("No data found.")

#     except InsuranceException as ie:
#         print(f"Insurance Exception occurred: {ie}")

#     finally:
#         if db_client:
#             db_client.close_connection()

# from Insurance_Prediction.pipeline.training_pipeline import TrainPipeline

# pipeline = TrainPipeline()
# pipeline.run_pipeline()


from Insurance_Prediction.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()