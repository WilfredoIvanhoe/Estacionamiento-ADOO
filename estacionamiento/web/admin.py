from django.contrib import admin
from .models import Usuario, Cajon, Solicitud,Automovil

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cajon)
admin.site.register(Solicitud)
admin.site.register(Automovil)