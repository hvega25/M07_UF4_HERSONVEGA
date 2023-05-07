from django.urls import path
from . import views


#Rutas de la aplicación
urlpatterns=[
    path('student/', views.alum, name='student'),
    path('prof/', views.prof, name='prof'),
]