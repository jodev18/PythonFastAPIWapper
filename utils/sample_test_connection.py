
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Test the connection
# Access a database
db = client.get_database("sample_collection_1")

# Access a collection
collection = db.get_collection("scoll2")

# Sample insert -- ordinary json data
result = collection.insert_one({
    "Name" : "Jojo",
    "Age" : 29
})
print(result)
if result is not None:
    print("Successfully inserted value.")
else:
    print("An error was encountered while inserting a value.")