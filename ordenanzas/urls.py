from django.contrib import admin
from django.urls import path, include
from .views import OrdenSearchView, ListOrdenanza, send_file
app_name='ordenanzas'

urlpatterns = [
    path("O/", ListOrdenanza.as_view(), name='Listado-Ordenanzas'),
    path("search/", OrdenSearchView.as_view(), name="search"),
    path("file/", send_file, name="PDF")
]
