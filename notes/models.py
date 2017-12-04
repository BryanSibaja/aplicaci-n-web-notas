from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Libro(models.Model):
    class Meta:
        unique_together = (('nombre', 'pertenece'),)
    nombre = models.CharField(null=False, max_length=35)
    pertenece = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.nombre)

class Nota(models.Model):
    titulo = models.CharField(max_length = 35, null=False)
    cuerpo = RichTextUploadingField(null=True)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now=True)
    borrado = models.BooleanField(default=False)
    libro = models.ForeignKey(Libro, null=False, on_delete=models.CASCADE)
    compartido = models.ManyToManyField(User)

class Etiquetas(models.Model):
    nombre = models.CharField(null=False, max_length=35)
    nota = models.ForeignKey(Nota, null=False, on_delete=models.CASCADE)

class Imagen(models.Model):
    imagen = models.ImageField(null=False)
    usuario = models.ForeignKey(User, null=False)
