import os
stream = os.popen('nfc-poll|grep UID')
salida = stream.read()
print(salida)
newUID = (salida.replace('UID: ','')).replace("",'')
print(newUID)