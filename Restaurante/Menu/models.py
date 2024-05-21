from django.db import models


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
    num_orden = models.ForeignKey(Orden,on_delete=models.CASCADE)