from ast import Return
from urllib import request
from urllib.request import Request
from django.db.models.base import Model
from django.db.models import Q
from django.http import FileResponse, Http404
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from .models import Ordenanza

# Create your views here.}


def Odetalle(context, ordenanza):
    return HttpResponse(f"la Ordenanza es: {ordenanza}")

class ListOrdenanza(ListView):
    model = Ordenanza
    paginate_by = 5
    tamplate_name = 'ordenazas/ordenaza_list.html'
    context_object_name = 'ordenazas'
    queryset = Ordenanza.objects.all()
    
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "un menaje"
        
        print(context)
        
        return context
    

    


def send_file(response):

    pdf = open('media/ordenanzas/ord._Nº_227_07.pdf', 'rb')
    

    response = FileResponse(pdf)

    return response



#funciones para la búsqueda

class OrdenSearchView(ListView):
    template_name =  'ordenazas/ordenaza_list.html' #se indica el template a utiliza 
    paginate_by = 5
    #en este caso el queryset va a depender de lo que el snippets search nos mande en el atributo q
    #queryset =  

    
    def get_queryset(self):#se hace la consulta        
        filters = Q(numero__icontains=self.query()) | Q(ano__icontains=self.query()) | Q(cat__descripcion__icontains=self.query())
        return Ordenanza.objects.filter(filters)   

    def query(self):#se obtiene el valor de q en el request
        q = self.request.GET.get('q')
        return q

    def get_context_data(self, **kwargs): #sobre esctibo el metodo para obtener el contexto de la peticion
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['ordenazas'] = context['ordenanza_list']
        context['count'] = context['ordenanza_list'].count()
        print(context)
        return context
