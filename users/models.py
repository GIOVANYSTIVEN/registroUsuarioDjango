from django.db import models

# Create your models here.
class Persona(models.model):
    ESTADO_CHOISE =[
    ('activo','activo')
    ('inactivo',)

]
    name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    datecrated = models.DateField(auto_now=True)
    state = models.CharField(max_length=100, choices=ESTADO_CHOISE,default='activo' ) 

    def __str__(self):
        return self.name
