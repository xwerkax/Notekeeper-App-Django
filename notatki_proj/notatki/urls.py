from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notatek, name='lista_notatek'),
    path('dodaj/', views.dodaj_notatke, name= 'dodaj_notatke'),
]
