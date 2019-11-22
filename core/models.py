from django.db import models

# Create your models here.

class Producto(models.Model):
    
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    foto=models.ImageField(upload_to='fotos/')
    categoria=models.CharField(max_length=50)

    def __str__(self):
	    return self.nombre+", "+str(self.precio)+", "+str(self.stock)+", "+str(self.foto)+", "+self.nombre


class Pro(models.Model):
    
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    foto=models.ImageField(upload_to='fotos/')
    categoria=models.CharField(max_length=50)

    def __str__(self):
	    return self.nombre+", "+str(self.precio)+", "+str(self.stock)+", "+str(self.foto)+", "+self.categoria


class Usuario(models.Model):
    nombre = models.CharField(max_length=10)
    contrasenia = models.CharField(max_length=150)

    def crearUsuario(self):
        self.save()

    def __str__(self):
        return self.nombre



    