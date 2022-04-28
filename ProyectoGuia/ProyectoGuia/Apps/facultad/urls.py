from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('facultades', views.facultades, name='facultades'),
    path('successFacultad', views.SuccessFacultadView.as_view(), name='successFacultad'),
    path('listaFacultades', views.ListarFacultades.as_view(), name='listaFacultades'),
    path('listaDeleteFacultad', views.ListarDeleteFacultades.as_view(), name='listaDeleteFacultad'),
    path('listaUpdateFacultad', views.ListarUpdateFacultades.as_view(), name='listaUpdateFacultad'),
    path('crearFacultad', views.FacultadCreateView.as_view(), name='crearFacultad'),
    path('borrarFacultad/<pk>', views.FacultadDeleteView.as_view(), name='borrarFacultad'),
    path('actualizarFacultad/<pk>', views.FacultadUpdateView.as_view(), name='actualizarFacultad')
    ]
