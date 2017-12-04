"""Direciones URL aplicación"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from notes.views import index, editor, registro, acceder, listarLibros, listarNotas, nuevoCuaderno, borrarNota

urlpatterns = [
    url(r'^$', index),
    # url(r'^editor/$', login_required(editor)),
    url(r'^editor/$', login_required(listarLibros)),
    url(r'^editor/notas/$', login_required(listarNotas)),
    url(r'^editor/nuevo/$', login_required(nuevoCuaderno)),
    url(r'^editor/eliminar/$', login_required(borrarNota)),
    url(r'^accounts/login/$', acceder),
    url(r'^create_user/$', registro)
]