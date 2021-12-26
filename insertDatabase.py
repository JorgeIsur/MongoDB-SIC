import pymongo
import time
cliente =  pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["base_datos"]
collection = database["alumnos"]

diccionario = {"_id":"6","name":"Andres","Adress":"margaritas 721"}
push = collection.insert_one(diccionario)
print(push.inserted_id)
ordenar = collection.find().sort("name")
for nombre in ordenar:
    print(nombre)