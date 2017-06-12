from django.contrib import admin
from .models import Departamento, Trabajo, tiposTrabajos
# Register your models here.

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    pass

@admin.register(tiposTrabajos)
class tiposTrabajosAdmin(admin.ModelAdmin):
    pass
