from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from web.models import Usuario

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#VISTAS PARA USUARIOS
class UserCreate(CreateView):
    model = Usuario
    #fields = ['num_id ','usuario ','nombres ','a_paterno ','a_materno ','password ','telefono ','tipo_usuario ', 'discapacitado']
    fields = '__all__'

class UserDetailView(DetailView):
    model = Usuario