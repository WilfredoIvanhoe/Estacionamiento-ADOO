from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from web.models import Usuario
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, "web/index.html", {})

#VISTAS PARA USUARIOS
class UserCreate(CreateView):
    model = Usuario
    #fields = ['num_id ','usuario ','nombres ','a_paterno ','a_materno ','password ','telefono ','tipo_usuario ', 'discapacitado']
    fields = '__all__'

class UserDetailView(DetailView):
    model = Usuario

def UserLogin(request):
    return render(request, "web/login.html", {})