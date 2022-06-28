from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', 
         views.ListaLibros.as_view(), 
         name='libros'
        ),
    path('libros-2/', 
         views.ListaLibros2.as_view(), 
         name='libros2'
        ),
    path('libros-trg/', 
        views.ListaLibrosTrg.as_view(), 
        name='libros_trg'
    ),
    path('libros-detalle/<pk>/', 
         views.LibroDetailView.as_view(), 
         name='libros_detalle'
        ),
]
