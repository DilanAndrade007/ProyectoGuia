from django.shortcuts import render
from django.views.generic import (ListView,TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Facultad
from django.urls import reverse_lazy

# Create your views here.

def facultades(request):
    return render(request,'facultad/facultades.html')

class SuccessFacultadView(TemplateView):
    template_name = 'facultad/messages/successFacultad.html'

class ListarFacultades(ListView):
    model = Facultad
    context_object_name = 'listaFacultades'
    template_name = 'facultad/lists/listaFacultades.html'

class FacultadCreateView(CreateView):
    model = Facultad
    template_name = 'facultad/operations/crearFacultad.html'
    fields = ['nombre','nombreCorto','activo']
    success_url = reverse_lazy('successFacultad')

class FacultadDeleteView(DeleteView):
    model = Facultad
    fields = ['nombre','nombreCorto','activo']
    template_name = 'facultad/operations/borrarFacultad.html'
    success_url = reverse_lazy('successFacultad')

class ListarDeleteFacultades(ListView):
    model = Facultad
    context_object_name = 'listaDeleteFacultad'
    template_name = 'facultad/lists/listaDeleteFacultad.html'
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        listaResultados = Facultad.objects.filter(nombre=nombre)
        return listaResultados

class FacultadUpdateView(UpdateView):
    model = Facultad
    fields = ['nombre','nombreCorto','activo']
    template_name = 'facultad/operations/actualizarFacultad.html'
    success_url = reverse_lazy('successFacultad')

class ListarUpdateFacultades(ListView):
    model = Facultad
    context_object_name = 'listaUpdateFacultad'
    template_name = 'facultad/lists/listaUpdateFacultad.html'
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        listaResultados = Facultad.objects.filter(nombre=nombre)
        return listaResultados