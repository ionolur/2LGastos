from django.contrib import admin
from .models import Horas, Calendario, Gastos

# Register your models here.

class HorasAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('autor','dia',)}

admin.site.register(Horas, HorasAdmin)

@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('semana','dia','mes','dia_sem','codigo')

class GastosAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('autor','dia',)}