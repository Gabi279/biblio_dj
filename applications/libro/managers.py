from django.db import models

from django.db.models import Q

class LibroManager(models.Manager):
        
        def listar_libros(self, kword):
            resultado = self.filter(
                titulo__icontains=kword
            )
            return resultado
