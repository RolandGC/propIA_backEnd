from django.urls import path
from .views import *
#El atributo app_name te permite especificar un nombre de aplicación para todas las URL definidas en ese archivo
app_name = 'inmueble'

urlpatterns = [
    path('list/',ListProperty),
    path('add/',create_property),
    path('<int:pk>/',property_detail),
]