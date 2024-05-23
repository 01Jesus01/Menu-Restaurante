from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('cliente', 'Cliente'),
        ('mesero', 'Mesero'),
        ('cocinero', 'Cocinero'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=20, choices=USUARIO_CHOICES)
    
    def __str__(self):
        return f'{self.user.username} - {self.get_tipo_usuario_display()}'

class Mesero(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad= models.IntegerField()
    rfc = models.CharField(max_length=100)
    
      #Representar el registro como cadena de texto
    def _str_(self):
        return self.nombre

class Categoria_platillo(models.Model):
    nombre_cetgaoria= models.CharField(max_length=60)

    #Representar el registro como cadena de texto
    def _str_(self):
        return self.nombre_cetgaoria
    

# Create your models here.
class Menu(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=300)
    Precio = models.IntegerField()
    categoria= models.ForeignKey(Categoria_platillo,on_delete=models.CASCADE)
    Descuento = models.IntegerField(default=0) 
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
    
    
    #Representar el registro como cadena de texto
    def _str_(self):
        return self.Nombre
    

class Orden(models.Model):
    id_mesero = models.ForeignKey(Mesero,on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(Menu,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    comentario = models.CharField(max_length=400)
    precio_total = models.IntegerField()
    
class Mesa(models.Model):
    numero_mesa = models.IntegerField(default=0)
    num_orden = models.ForeignKey(Orden,on_delete=models.CASCADE)