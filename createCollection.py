import pymongo
import time
cliente =  pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["base_datos"]
collection = database["Alumnos"]
time.sleep(2)
print(database.list_collection_names())
