from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Libro(models.Model):
    nombre = models.CharField(null=False, max_length=35)
    padre = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    pertenece = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

class Nota(models.Model):
    titulo = models.CharField(max_length = 35, null=False)
    cuerpo = RichTextUploadingField()
    creacion = models.DateField(null=False)
    actualizacion = models.DateField(null=False)
    borrado = models.BooleanField()
    libro = models.ForeignKey(Libro, null=False, on_delete=models.CASCADE)
    compartido = models.ManyToManyField(User)

class Etiquetas(models.Model):
    nombre = models.CharField(null=False, max_length=35)
    nota = models.ForeignKey(Nota, null=False, on_delete=models.CASCADE)

class Imagen(models.Model):
    imagen = models.ImageField(null=False)
    usuario = models.ForeignKey(User, null=False)
