import os
import json
import sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from Insurance_Prediction.constants import ASTRA_DB_SECURE_BUNDLE_PATH, ASTRADB_APPLICATION_TOKEN, DATA_INGESTION_KEYSPACE_NAME
from Insurance_Prediction.exception import InsuranceException
from Insurance_Prediction.logger import logging

# astra db connection settings
class AstraDBClient:
    """
    A class to manage connections and operations with DataStax AstraDB.

    Attributes:
        keyspace_name (str): The keyspace to connect to in AstraDB.
    """
    client = None
    session = None

    def __init__(self, keyspace_name=DATA_INGESTION_KEYSPACE_NAME):
        try:
            if AstraDBClient.client is None:
                # Use constants defined in constants.py
                secure_bundle_path = ASTRA_DB_SECURE_BUNDLE_PATH
                token_path = ASTRADB_APPLICATION_TOKEN

                if not secure_bundle_path:
                    raise Exception("Environment variable ASTRA_DB_SECURE_BUNDLE_PATH is not set.")
                if not token_path:
                    raise Exception("Environment variable ASTRADB_APPLICATION_TOKEN is not set.")

                # Cloud configuration for the Cassandra cluster
                cloud_config = {
                    'secure_connect_bundle': secure_bundle_path
                }

                # Load the token JSON file
                with open(token_path) as f:
                    secrets = json.load(f)

                CLIENT_ID = secrets["clientId"]
                CLIENT_SECRET = secrets["secret"]

                # Set up authentication and connect to the cluster
                auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
                AstraDBClient.client = Cluster(cloud=cloud_config, auth_provider=auth_provider)
                AstraDBClient.session = AstraDBClient.client.connect(keyspace=keyspace_name)

                # Check session initialization
                if AstraDBClient.session:
                    logging.info("AstraDB session initialized successfully.")
                else:
                    raise Exception("AstraDB session is not initialized.")

                # Execute a query to test the connection
                row = AstraDBClient.session.execute("SELECT release_version FROM system.local").one()
                if row:
                    print(f"AstraDB connection successful. Cassandra version: {row[0]}")
                else:
                    raise Exception("Failed to retrieve Cassandra release version.")

                logging.info("AstraDB connection successful.")
        except Exception as e:
            error_message = f"Error initializing AstraDBClient: {str(e)}"
            logging.error(error_message)
            raise InsuranceException(error_message, sys)

    def execute_query(self, query):
        """
        Execute a CQL query on the connected keyspace.

        Args:
            query (str): The CQL query to execute.

        Returns:
            cassandra.cluster.ResultSet: The result set of the query execution.
        """
        try:
            if AstraDBClient.session:
                return AstraDBClient.session.execute(query)
            else:
                raise Exception("Cassandra session is not initialized.")
        except Exception as e:
            error_message = f"Error executing query: {query}. Error: {str(e)}"
            logging.error(error_message)
            raise InsuranceException(error_message, sys)

    def close_connection(self):
        """
        Close the Cassandra client connection.
        """
        try:
            if AstraDBClient.client:
                AstraDBClient.client.shutdown()
                logging.info("AstraDB client shutdown.")
        except Exception as e:
            error_message = f"Error closing AstraDB client: {str(e)}"
            logging.error(error_message)
            raise InsuranceException(error_message, sys)
     