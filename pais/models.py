from django.db import models

# Create your models here.
class Pais(models.Model):

    nombre=models.CharField(max_length=30)

    #especie de get
    def str (self):
        return self.nombre

class Meta:
    verbose_name="pais"
