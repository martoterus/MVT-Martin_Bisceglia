from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    lugar_nac = models.CharField(max_length=50)
    
