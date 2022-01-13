from django.contrib import admin
from django.urls import path, include
from .views import ContribSearchView, orden, ListOrdenanza, Odetalle, send_file
app_name='ordenanzas'

urlpatterns = [
    path("O/", ListOrdenanza.as_view(), name='Listado-Ordenanzas'),
    path("search/", ContribSearchView.as_view(), name="search"),
    path("file/", send_file, name="PDF")
]
