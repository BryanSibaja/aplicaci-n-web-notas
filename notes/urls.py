from django.conf.urls import url
from notes.views import index

urlpatterns = [
    url(r'^$', index)
]