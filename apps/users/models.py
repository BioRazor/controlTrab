from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trabajador(models.Model):
    user = models.OneToOneField(User)

    nombre = models.CharField(blank=False, max_length=50)
    apellido = models.CharField(blank=False, max_length=50)
    registrado = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Trabajadores"

    def __str__(self):
        return ('%s - %s') %(self.nombre, self.apellido)
