from django.http import HttpResponse

from web import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]