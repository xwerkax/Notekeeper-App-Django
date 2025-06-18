from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notatek, name='lista_notatek'),
    path('dodaj/', views.dodaj_notatke, name= 'dodaj_notatke'),
    path('edytuj/<int:notatka_id>/', views.edytuj_notatke, name= 'edytuj_notatke'),
    path('moje_notatki/', views.moje_notatki, name= 'moje_notatki'),
    path('usun/<int:notatka_id>/', views.usun_notatke, name='usun_notatke'),
    path('podglad/<int:notatka_id>',views.podglad_notatki, name='podglad_notatki' ),
]
