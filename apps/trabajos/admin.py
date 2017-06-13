from django.contrib import admin
from .models import Departamento, Trabajo, tiposTrabajos, Cliente
from apps.users.models import Trabajador
# Register your models here.

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    fields = ('cliente', 'tipo', 'precio', 'cdRDC', 'dvdRDC', 'penRDC')
    list_display = ('tipo', 'Trabajador', 'cliente', 'fecha', 'precio')
    search_fields = ('cliente__nombre<  ',)

    def save_model(self, request, obj, form, change):
        if not change:
        # can use this condition also to set 'created_by'
        # if not getattr(obj, 'created_by', None):
            obj.Trabajador = Trabajador.objects.get(user=request.user)
        obj.save()

@admin.register(tiposTrabajos)
class tiposTrabajosAdmin(admin.ModelAdmin):
    pass
