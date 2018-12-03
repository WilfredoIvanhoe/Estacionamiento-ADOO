from django.http import HttpResponse
from django.views.generic import TemplateView
from web import views
from django.urls import path

urlpatterns = [
    path('new/', views.UserCreate.as_view(), name='user-add'),
    path('<slug:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]