from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    descripcion = models.TextField("Descripcion", max_length=30, unique=True)
    
    def __str__(self) -> str:
        return self.descripcion

class Tag(models.Model):
    #ordenanza = models.ForeignKey(Ordenanza, on_delete=models.CASCADE)
    tag = models.CharField("Categoria", max_length=30)
    
    def __str__(self) -> str:
        return self.tag
    

class Ordenanza(models.Model):
    numero = models.IntegerField("Numero", blank=True, null=True)
    ano = models.IntegerField("Año", blank=True, null=True)
    cat = models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.CASCADE)
    fecha_promulgacion = models.DateField("Fecha de Promulgacion")
    reseña = models.TextField("Reseña Ordenanza")
    tags = models.ManyToManyField(Tag, verbose_name="Tags", null=True)
    concejal = models.CharField("Presentado por", max_length=60, null=True, blank=False, default='')
    pdfFile = models.FileField("Archivo", upload_to='ordenanzas/', null=False, blank=True)
    created_date = models.DateTimeField("Fecha de Creación", 
            default=timezone.now)
    
    
    
    def __str__(self) -> str:
        return str(self.numero) + "/" + str(self.ano)
    

    


    
#class Tag_Odenanza(models.Model):
#    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="Tags")
#    ordenanza = models.ForeignKey(Ordenanza, on_delete=models.CASCADE, related_name='Ordenanza')