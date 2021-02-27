from django.urls import path
from django.contrib import admin
from . import views

from BieleGastosApp import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('usuario', views.usuario, name='Usuario'),
    path('recibo', views.recibo, name='Recibo'),
    path('horas', views.horas, name='Horas'),
    path('calendario', views.calendario, name='Calendario'),
    path('convenio', views.convenio, name='Convenio'),
    path('mail', views.mail, name='Mail'),
    path('gastos', views.gastos, name='Gastos'),

    path('admin/', admin.site.urls),

]
