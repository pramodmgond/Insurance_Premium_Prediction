import pandas as pd
from typing import Optional
from Insurance_Prediction.exception import InsuranceException
from Insurance_Prediction.logger import logging
from Insurance_Prediction.configuration.connection import AstraDBClient
import os
import sys

from pandas import DataFrame  # Import DataFrame from pandas

 # Ensure AstraDBClient is imported correctly

class InsuranceData:
    """
    This class helps to export the entire AstraDB record as a pandas DataFrame.
    """

    def __init__(self):
        """
        Initialize the InsuranceData class with an AstraDBClient.
        """
        try:
            self.db_client = AstraDBClient()
        except Exception as e:
            raise InsuranceException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Export the entire collection as a DataFrame.

        Args:
            collection_name (str): The name of the collection (table).
            database_name (Optional[str]): The name of the database (keyspace). If None, use the default keyspace.

        Returns:
            pd.DataFrame: DataFrame containing the collection data.
        """
        try:
            # Example query execution
            insurance_cols = []

            # Modify query to use collection_name
            query = f"SELECT * FROM {collection_name}"
            result = self.db_client.execute_query(query)

            if result:
                for row in result:
                    insurance_cols.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
                    # logging.info(f"Row: ada")
            else:
                print("No data found.")

            # Create DataFrame from collected data
            df = pd.DataFrame(insurance_cols, columns=['id', 'age', 'bmi', 'children', 'expenses', 'region', 'sex', 'smoker'])
            print("Data frame created")
            logging.info(f"Data frame created with the help of insurance_data.py")

            # Drop duplicate entries if necessary
            df.drop_duplicates(inplace=True, ignore_index=True)
            
            return df

        except InsuranceException as ie:
            print(f"Insurance Exception occurred: {ie}")
            raise ie
        except Exception as e:
            raise InsuranceException(e, sys)
