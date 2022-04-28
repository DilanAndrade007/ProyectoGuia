from django.urls import path
from . import views
#app_name = 'persona_app'

urlpatterns = [
    # 'path', 'vista', nombre
    path('estudiantes', views.estudiantes.as_view(), name='estudiantes'),
    path('estudiantesFacultad', views.estudiantesFacultad, name='estudiantesFacultad'),
    path('listaEstudiantes', views.ListarEstudiantes.as_view(), name='listaEstudiantes'),
    path('listaEstudiantesNombre', views.ListarEstudiantesBusqueda.as_view(), name='listaEstudiantesNombre'),
    path('listaEstudiantesHabilidad', views.ListarEstudiantesHabilidades.as_view(), name='listaEstudiantesHabilidad'),
    path('listaUpdateEstudiante', views.ListarUpdateEstudiantes.as_view(), name='listaUpdateEstudiante'),
    path('listaDeleteEstudiante', views.ListarDeleteEstudiantes.as_view(), name='listaDeleteEstudiante'),
    path('detailEstudiante/<pk>', views.EstudiantesDetailView.as_view(), name='detailEstudiante'),
    path('crearEstudiante', views.EstudianteCreateView.as_view(), name='crearEstudiante'),
    path('actualizarEstudiante/<pk>', views.EstudianteUpdateView.as_view(), name='actualizarEstudiante'),
    path('borrarEstudiante/<pk>', views.EstudianteDeleteView.as_view(), name='borrarEstudiante'),
    path('success', views.SuccessView.as_view(), name='success'),

    # Facultative
    path('listaEstudiantesFacultad/<facultad>', views.ListarEstudiantesPorFacultad.as_view(), name='listaEstudiantesFacultad'),
    ]

