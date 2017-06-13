from django.db import models

# Create your models here.

class Departamento(models.Model):
    """(Departamento description)"""
    """
        Cada uno de los deparatamentos a los que pertenecen los trabajos
        realizados en la empresa
    """
    nombre = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(blank=True, max_length=100)
    telefono = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre

class tiposTrabajos(models.Model):
    nombre = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name= 'Tipo de Trabajo'
        verbose_name_plural= 'Tipos de Trabajos'

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    """(Trabajo   description)"""
    Trabajador = models.ForeignKey('users.Trabajador')
    cliente = models.OneToOneField(Cliente, blank=True, null= True)
    tipo = models.ForeignKey(tiposTrabajos)
    precio = models.SmallIntegerField(blank=False, null=False)
    fecha = models.DateTimeField(blank=True, auto_now_add=True)
    cdRDC = models.BooleanField(default=False)
    dvdRDC = models.BooleanField(default=False)
    penRDC = models.BooleanField(default=False)

    def __str__(self):
        return ('%s - %s - %s') %(self.tipo, self.fecha, self.precio)
