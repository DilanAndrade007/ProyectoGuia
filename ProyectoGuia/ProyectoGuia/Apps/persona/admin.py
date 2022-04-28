from django.contrib import admin
from .models import Estudiante, Habilidades
# Register your models here.
#admin.site.register(Estudiante)

admin.site.register(Habilidades)

class EstudianteAdmin(admin.ModelAdmin):
    # Columnas a mostrarse en formato de tabla
    list_display = (
        'id',
        'apellido',
        'primerNombre',
        'tipo',
        'facultad',
        # agregar una columna
        'full_name',
    )

    def full_name(self, obj):
        return obj.primerNombre + ' ' + obj.apellido

    # Agregar filtros de búsqueda
    # 1. Filtro texto
    search_fields = ('apellido',)
    # 2. Filtro de lista
    list_filter = ('facultad', 'tipo', 'habilidad')
    # 3. Exclusivo m2m, filtro horizontal
    filter_horizontal = ('habilidad',)

admin.site.register(Estudiante, EstudianteAdmin)