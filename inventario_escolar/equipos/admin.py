from django.contrib import admin
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado',
                    'fecha_ingreso', 'ubicacion')
    
admin.site.register(Equipo, EquipoAdmin)


