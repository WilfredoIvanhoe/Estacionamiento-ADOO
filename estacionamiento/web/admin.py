from django.contrib import admin
from .models import Usuario, Cajon, Solicitud,Automovil,Sancion,LugarAsignado

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cajon)
admin.site.register(Solicitud)
admin.site.register(Automovil)
admin.site.register(Sancion)
admin.site.register(LugarAsignado)