from django.urls import path 
from pais.views import home, crear_vista


#llamas a metodos, no los entrecomilles hostia
urlpatterns = [
path('home/',home),
path('c/',crear_vista),
]