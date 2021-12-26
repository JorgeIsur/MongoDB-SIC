import pymongo
import time
miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
base_datos = miCliente["UAM"]
alumnos = base_datos["alumnos"]
admin = base_datos["administrativos"]
def registro():
    print("***********************************************")
    print("*******************REGISTRO********************")
    opcion=input("Ingrese 0 para regresar al menú y 1 para continuar.\n")
    if opcion=='0':
        menu()
    tipo = input("1. Profesor/Administrativo\n"
                 "2. Alumno\n")
    nombre = input("Ingresa tu nombre:\t")
    matricula = input("Ingresa tu matricula:\t")           
    info = input("Ingresa tu correo institucional:\t") 
    password = input("Ingresa tu contraseña:\t")
    prueba_pass = input("Vuelve a ingresar tu contraseña:\t")
    if password !=prueba_pass:
        print("Contraseña incorrecta.")
        registro()
    miRegistro = {"nombre":nombre,"_id":matricula,"info":info,"password":password}
    if tipo=='1':
        for dato in admin.find({},{"_id":1}):
            if dato["_id"]==matricula:
                print("Esta matricula ya fue registrada con anterioridad")
                registro()
        push = admin.insert_one(miRegistro)
        print("*************************************************")
        print("Registro exitoso.\n")
        print("*************************************************")
    if tipo=='2':
        for dato in alumnos.find({},{"_id":1}):
            if dato["_id"]==matricula:
                print("Esta matricula ya fue registrada con anterioridad")
                registro()
        push = alumnos.insert_one(miRegistro)
        print("*************************************************")
        print("Registro exitoso.\n")
        print("*************************************************")
def login():
    print("***********************************************")
    print("*******************LOGIN********************")
    opcion=input("Ingrese 0 para regresar al menú y 1 para continuar.\n")
    if opcion=='0':
        menu()
    matricula = input("Ingresa tu matricula.\t")
    contra = input("Ingresa tu contraseña\t")
    tipo = input("1. Profesor/Administrativo\n"
                 "2. Alumno\n")
    busqueda = {"_id":matricula,"password":contra}
    if tipo=='1':
        process=admin.find({"_id":matricula},{"password":1})
        for dato in process:
            if dato["password"]==contra:
                print("Validación exitosa.\n")
            else:
                print("Contraseña incorrecta.\n")
    if tipo=='2':
        process=alumnos.find({"_id":matricula},{"password":1})
        for dato in process:
            if dato["password"]==contra:
                print("Validación exitosa.\n")
            else:
                print("Contraseña incorrecta\n")
                login()
def menu():
    print("-------------------------------------------")
    print("-------------------MENU--------------------")
    print("Sistema de administración de cuentas.\n")
    print("1. Registrar usuario(Admin/alumno)\n")
    print("2. Inicio de sesión de usuario\n")
    print("3. Eliminar usuario.\n")
    print("4. Mostrar todos los alumnos.\n")
    print("5. Mostrar todos los administrativos/profesores.\n")
    print("0. Salir.\n")
    opcion = input("Ingresa tu opción:\t")
    if opcion=='1':
        registro()
    if opcion=='2':
        login()
    if opcion=='3':
        print("Opción no soportada por el momento\n")
        menu()
    if opcion=='4':
        print("****************************************")
        print("*****************ALUMNOS****************")
        for datos in alumnos.find():
            print(datos)
        print("****************************************")
    if opcion=='5':
        print("****************************************")
        print("*****************ADMIN****************")
        for datos in admin.find():
            print(datos)
        print("****************************************")
    if opcion=='0':
        print("****************************************")
        print("****************BYE*********************")
        exit(0)
while True:
    menu()