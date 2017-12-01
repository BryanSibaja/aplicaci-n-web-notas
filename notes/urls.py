from django.conf.urls import url
from notes.views import index, editor, registro, acceder
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index),
    url(r'^editor/$', login_required(editor)),
    url(r'^accounts/login/$',acceder),
    url(r'^create_user/$', registro)
]