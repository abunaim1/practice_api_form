from django.urls import path
from . import views

urlpatterns = [
    path('api_form/', views.apiForm, name='apiForm'),
    path('django_model/', views.djangoModel, name='djangoModel')
]
