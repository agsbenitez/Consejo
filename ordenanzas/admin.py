from django.contrib import admin
from django.db import models
from .models import Ordenanza, Tag, Categoria


#@admin.register(Categoria)
class Ordenanza_admin(admin.ModelAdmin):
    list_display = ('__str__','fecha_promulgacion', 'reseña', 'cat')
    search_fields = ['nombre', 'fecha_promulgacion', 'cat__descripcion']
   
    
    
admin.site.site_header = "CD Municipalidad de Riachuelo" #cambio la leyenda del encabezado del almin
admin.site.site_title = "Sitio de Administración"
admin.site.register(Ordenanza, Ordenanza_admin)
admin.site.register(Tag)
admin.site.register(Categoria)
# Register your models here.
