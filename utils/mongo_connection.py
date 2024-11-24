
"""
    Main class for handling database connection
    for MongoDB.

"""

from pymongo import MongoClient
from utils.mongo_logger import MongoLogger

class MongoConnect:

    def __init__(self):
        self._MONGO_URL = "mongodb://localhost:27017/"

        self.mongo_client = MongoClient(self._MONGO_URL)
        self.mongo_db = None
        self.mongo_collection = None
        self.logger = MongoLogger()


    # Step 1
    def get_database(self, database_name: str=''):
        self.logger.write_log(module_name="Mongo Connect", log_msg="Connecting to database.")

        self.mongo_db = self.mongo_client.get_database(database_name)
        return True


    # Step 2
    def get_collection(self, collection_name: str=''):

        self.logger.write_log(module_name="Mongo Connect", log_msg=f"Accessing collection: {collection_name}")

        if self.mongo_db is not None:
            self.mongo_collection = self.mongo_db.get_collection(collection_name)

            return self.mongo_collection
        else:
            raise Exception("You should initialize database connection first!")

    # Then query.

if __name__ == "__main__":

    sample_connect = MongoConnect()
    db = sample_connect.get_database('sample_collection_1')

    if db:
        coll = sample_connect.get_collection('scoll1')