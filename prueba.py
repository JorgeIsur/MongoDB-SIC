import pymongo
miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
base_datos = miCliente["UAM"]
alumnos = base_datos["alumnos"]
admin = base_datos["administrativos"]
nombre = {"nombre":"AMLO"}
retorno = alumnos.find_one(nombre)
print(retorno)