from django.conf.urls import url
from notes.views import index, editor, registro

urlpatterns = [
    url(r'^$', index),
    url(r'^editor/$', editor),
    url(r'^registro/$', registro)
]