import pymongo
import time
cliente =  pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["base_datos"]
time.sleep(2)
print(cliente.list_database_names())