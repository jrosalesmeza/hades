from django.db import models
from datetime import datetime
# Create your models here.



class Type(models.Model):
    name= models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']

class Category(models.Model):
    name= models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']



class Employee(models.Model):
    Category= models.ManyToManyField(Category) 
    type= models.ForeignKey(Type, on_delete=models.CASCADE)  #models.CASCADE=> Si llegase a eliminar la tabla, se elimina la información || ForeignKey => Tablas relacionales
    names = models.CharField(max_length=150, verbose_name='Nombres')     #names= models.TextField() //Permite cualquier numero de caracteres
    cedula = models.CharField(max_length=10, verbose_name='Cedula', unique=True)    #verbose_name // Sirve para nombrar la columna con algo en especifico, si no se llama como su propiedad
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")  #default= Un valor por defecto
    date_creation= models.DateTimeField(auto_now=True)
    date_updated= models.DateTimeField(auto_now_add=True)  #auto now add => Se incrementa automaticamente la fecha
    age= models.PositiveBigIntegerField(default=0, verbose_name='Edad')
    salary=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state= models.BooleanField(default=True)
    avatar= models.ImageField(upload_to='avatar/%Y/%m/%d',null=True, blank=True) 
    cvitae= models.FileField(upload_to='cvitae/%Y/%m/%d',null=True, blank=True)
    gender = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.names

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id']

