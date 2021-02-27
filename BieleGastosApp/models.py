from django.db import models
from django.contrib.auth.models import User

class Horas(models.Model):

    autor = models.ForeignKey(User,on_delete=models.CASCADE,)
    dia = models.DateField()
    slug = models.SlugField()
    horas_trabajo = models.DecimalField(max_digits=3, decimal_places=1)
    viaje_ida = models.DecimalField(max_digits=3, decimal_places=1)
    viaje_vuelta = models.DecimalField(max_digits=3, decimal_places=1)
    pernocta = models.BooleanField()
    semana_3 = models.BooleanField()
    notas = models.TextField()

    class Meta:
        ordering =('autor','dia')
        verbose_name ="hora"
        verbose_name_plural ="horas"
    
class Calendario(models.Model):

    semana = models.IntegerField()
    dia = models.IntegerField()
    mes = models.IntegerField()
    dia_sem = models.IntegerField()
    codigo = models.IntegerField()

    class Meta:
        ordering = ('semana', 'mes', 'dia')
        verbose_name = "calendario"
    
class Gastos(models.Model):
    dia = models.DateField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE,)
    slug = models.SlugField()
    concepto = models.CharField(max_length=25)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=25)
    notas = models.TextField()

    class Meta:
        ordering = ('autor','dia')
        verbose_name = 'gasto'
        verbose_name_plural = 'gastos'
# Create your models here.

class Convenio (models.Model):
    dia_trabajo = 37.9
    viernes = 75.8
    sabado_medio = 94.75
    sabado_completo = 236.9
    domingo_medio = 165.85
    domingo_completo = 331.7
    pernocta_normal = 40
    pernocta_festivo = 60
    tercera_semana = 10
    kilometros = 0.35
    extra_normal = 18.95
    extra_ertain = 28.43
    extra_especial = 33.17
    horas_viaje = 26.32

    class Meta: 
        verbose_name = 'convenio'

class Resultado (models.Model):
    Plus_A = 0.0
    Plus_A_euro = 0.0
    Plus_B = 0.0
    Plus_B_euro = 0.0
    Plus_C = 0.0
    Plus_C_euro = 0.0
    Total_Plus = 0.0
    Dia_Normal = 0
    Dia_Normal_euro = 0.0
    Viernes = 0
    Viernes_euro = 0.0
    Medio_Sabado = 0
    Medio_Sabado_euro = 0.0
    Completo_Sabado = 0
    Completo_Sabado_euro = 0.0
    Medio_Domingo = 0
    Medio_Domingo_euro = 0.0
    Completo_Domingo = 0
    Completo_Domingo_euro = 0.0
    Total_PeM = 0.0
    Desplazamiento = 0.0
    Desplazamiento_euro = 0.0
    Pernocta_dia = 0
    Pernocta_dia_euro = 0.0
    Pernocta_festivo = 0
    Pernocta_festivo_euro = 0.0
    Pernocta_dia_sem3 = 0
    Pernocta_dia_sem3_euro = 0.0
    Pernocta_festivo_sem3 = 0
    Pernocta_festivo_sem3_euro = 0.0
    Total_Pernocta = 0.0
    Kilometros = 0.0
    Kilometros_euro = 0.0
    Horas_a_Deber = 0.0
    Total_Bruto = 0.0
    
    class Meta:
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'
    
class Usuario(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE,)
    irpf = models.DecimalField(max_digits=4, decimal_places=2)
    reduccion = models.DecimalField(max_digits=4, decimal_places=2)
    guardar_normal = models.BooleanField()
    guardar_ertain = models.BooleanField()
    guardar_berezi = models.BooleanField()