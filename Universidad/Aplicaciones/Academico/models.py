from django.db import models


# Create your models here.


class Curso(models.Model):

    num = models.AutoField(primary_key=True)
    edificio = models.CharField(max_length=2)
    fecharegistrada = models.CharField(max_length=20)
    numerodeparte = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    solicitud = models.CharField(max_length=50)



    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.num,self.edificio, self.fecharegistrada, self.numerodeparte, self.descripcion, self.modelo, self.fecha, self.solicitud)


