from django.contrib import admin
from .models import Trabajador

# Register your models here.

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    pass
