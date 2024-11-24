
"""
    Main class for handling database connection
    for MongoDB.

"""

from pymongo import MongoClient

class MongoConnect:

    def __init__(self):
        self.mongo_client = MongoClient("mongodb://localhost:27017/")
        self.mongo_db = None
        self.mongo_collection = None


    # Step 1
    def get_database(self, database_name: str=''):
        self.mongo_db = self.mongo_client.get_database(database_name)


    # Step 2
    def get_collection(self):
        pass

    # Then query.