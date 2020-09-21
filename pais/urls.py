from django.urls import path 
from pais.views import home

#llamas a metodos, no los entrecomilles hostia
urlpatterns = [
path('',home)
]