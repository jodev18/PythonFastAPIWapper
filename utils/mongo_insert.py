
from mongo_connection import MongoConnect

class MongoInsert(MongoConnect):

    def __init__(self):
        super().__init__()

    def insert_value(self, key_values: dict):
        self.logger.write_log(module_name="Mongo Insert", log_msg=f"Inserting value {key_values}")
        # static code for automatically setting the timestamp for insertion
        key_values['created_on'] = self.logger.get_timestamp_str()
        return self.mongo_collection.insert_one(key_values)


# Test code
if __name__ == "__main__":

    ins_data = MongoInsert()
    ins_data.get_database("sample_collection_1")
    ins_data.get_collection("scoll1")
    ins_data.insert_value({
            "random":"Value",
            "such_as":69
        })