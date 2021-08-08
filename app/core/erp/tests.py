
from os import name
from config.wsgi import *
from core.erp.models import *


#ORM de Django
# #Listar

# #Select *from Tabla
# query=Type.objects.all()

# print(query)

# #Insercion
# t= Type(name="Prueba2").save()


#Edición

# t= Type.objects.get(id=5)

# t.name= "Prueba2 Editado"
# t.save()


#Eliminación


# try:
#     t= Type.objects.get(pk=3)
#     t.delete()
# except Exception as e:
#     print('No se puede elimintar el id=3 ', e)




# for i in Type.objects.filter(name__endswith='e'):
#     print(i.id)

