from django.db import models

# Create your models here.
class Pais(models.Model):

    nombre=models.TextField()

    #especie de get
    def str (self):
        return self.nombre
    
