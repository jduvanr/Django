from django.db import models

class Clientes (models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    nombreEmpleado= models.ForeignKey('Empleados', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f" cliente:{self.nombre}- vendedor:{self.nombreEmpleado.nombre}"

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()

    def __str__(self):
        return self.nombre


# Create your models here.
