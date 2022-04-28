from django.shortcuts import render
from django.views.generic import (ListView,TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Estudiante
from django.urls import reverse_lazy

# Create your views here.

class estudiantes(ListView):
    template_name = 'persona/estudiantes.html'
    model = Estudiante
    context_object_name = 'estudiantes'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        #print('Nombre en back', nombre)
        listaResultados = Estudiante.objects.filter(primerNombre=nombre)
        return listaResultados

def estudiantesFacultad(request):
    return render(request, 'persona/listaFacultadesEstudiantes.html')

#   Lists View

# 1. Lista de todos los estudiantes
class ListarEstudiantes(ListView):
    # configurar modelo de la vista
    model = Estudiante
    # Parámetro específico para las vistas
    context_object_name = 'listaEstudiantes'
    # definir el template de salida
    template_name = 'persona/listaEstudiantes.html'

# 2 Listar todos los estudiantes por Facultad, filtros con el ORM
class ListarEstudiantesPorFacultad(ListView):
    #modelo
    model = Estudiante
    # template
    template_name = 'persona/listaEstudiantesFacultad.html'
    # Tomar nombre corto de facultad desde la url
    def get_queryset(self):
        # Recoger el parámetro GET desde la url
        facultadBusqueda = self.kwargs['facultad']
        # Select Estudiante -> Atributo Facultad -> Del atributo facultad sacar el nombre corto
        # -> Nombre corto en url == Nombre corto facultad estudiantes
        # Usaremos el operador __
        listaResultados = Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        return listaResultados

# 3 Listar por búsqueda de nombre (pasando por get)
class ListarEstudiantesBusqueda(ListView):
    template_name = 'persona/listaEstudiantesBusqueda.html'
    model = Estudiante
    context_object_name = 'estudiantes'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        #print('Nombre en back', nombre)
        listaResultados = Estudiante.objects.filter(primerNombre=nombre)
        return listaResultados


# 4 Listar Habilidades del estudiantes (m2m)
class ListarEstudiantesHabilidades(ListView):
    template_name = 'persona/listaEstudiantesHabilidad.html'
    model = Estudiante
    context_object_name = 'habilidades'
    def get_queryset(self):
        estudiante = Estudiante.objects.get(id=2)
        return estudiante.habilidad.all()

#   CRUD views
# Crear

class SuccessView(TemplateView):
    template_name = 'persona/messages/success.html'

# Detailed View
class EstudiantesDetailView(DetailView):
    model = Estudiante
    template_name = 'persona/detailEstudiantes.html'
    # context obtiene la informacion que le pasamos al template
    def get_context_data(self, **kwargs):
        #contenido todos los datos y atributos
        context = super(EstudiantesDetailView, self).get_context_data(**kwargs)
        # le agrego algo nuevos datos o atributos sin intervenir en la base de datos
        context['titulo'] = 'Mejor estudiante'
        return context

# Create View
class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'persona/crearEstudiante.html'
    #fields = ('__all__')
    fields = ['primerNombre','apellido','nombreCompleto','tipo','facultad','cartaMotivacion','habilidad']
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # hacer validacion, crear parametros sin que se pase desde el html
        estudiante = form.save()
        estudiante.nombreCompleto = estudiante.primerNombre + ' ' + estudiante.apellido
        estudiante.save()
        return super(EstudianteCreateView, self).form_valid(form)

# Update View
class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['primerNombre','apellido','nombreCompleto','tipo','facultad','cartaMotivacion','habilidad']
    template_name = 'persona/actualizarEstudiante.html'
    success_url = reverse_lazy('success')

# Delete View
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    fields = ['primerNombre','apellido','nombreCompleto','tipo','facultad','cartaMotivacion','habilidad']
    template_name = 'persona/borrarEstudiante.html'
    success_url = reverse_lazy('success')

# Other
class ListarDeleteEstudiantes(ListView):
    model = Estudiante
    context_object_name = 'listaDeleteEstudiante'
    template_name = 'persona/listaDeleteEstudiante.html'
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        listaResultados = Estudiante.objects.filter(primerNombre=nombre)
        return listaResultados

class ListarUpdateEstudiantes(ListView):
    model = Estudiante
    context_object_name = 'listaUpdateEstudiante'
    template_name = 'persona/listaUpdateEstudiante.html'
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        listaResultados = Estudiante.objects.filter(primerNombre=nombre)
        return listaResultados