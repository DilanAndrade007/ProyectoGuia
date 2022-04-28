from django.contrib import admin
from .models import Facultad
# Register your models here.

class FacultadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'nombreCorto',
    )

admin.site.register(Facultad,FacultadAdmin)