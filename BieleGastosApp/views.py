from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Horas
from BieleGastosApp.forms import FormularioHoras, EmailContacto, FormularioRecibo, FormularioGastos, FormularioCalendario, FormularioUsuario
from BieleGastosApp.calcular import recibo_imprimir
from BieleGastosApp.calendario import obtener_mes
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_in
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from BieleGastosApp.models import Convenio, Resultado, Calendario, Horas, Usuario
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.
'''
def login(request):

    if request.User.is_authenticated:
        return render(request,"BieleGastosApp/usuario.html")

    return render(request, "BieleGastosApp/login.html")
'''
def usuario(request):
    user_actual=request.user.id
    user = User.objects.get(id=user_actual)
    new_form_data = {}
    miUsuario = FormularioUsuario(new_form_data)
    usuario = {}
    print(user)
    print(user_actual)
    '''
    try:
        usuario = Usuario.objects.get(autor= user)
        new_form_data = {}
        new_form_data['irpf'] = usuario.irpf
        new_form_data['reduccion'] = usuario.reduccion
        new_form_data['guardar_normal'] = usuario.guardar_normal
        new_form_data['guardar_ertain'] = usuario.guardar_ertain
        new_form_data['guardar_berezi'] = usuario.guardar_berezi
        miUsuario = FormularioUsuario(new_form_data)
    except Exception as e:
        
        print(e)
        print("No existe datos usuario")
    
        new_form_data = {}
        new_form_data['irpf'] = 0.0
        new_form_data['reduccion'] = 0.0
        new_form_data['guardar_normal'] = False
        new_form_data['guardar_ertain'] = False
        new_form_data['guardar_berezi'] = False
        miUsuario = FormularioUsuario(new_form_data)
    

    if request.method=='POST' and ('guardar' in request.POST):
        miUsuario=FormularioUsuario(request.POST)
        print(user_actual)
        try:
            usuario = Usuario.objects.get(autor= user_actual)
            usuario.irpf = miUsuario.data['irpf']
            usuario.reduccion = miUsuario.data['reduccion']
            usuario.guardar_normal = miUsuario.data['guardar_normal']
            usuario.guardar_ertain = miUsuario.data['guardar_ertain']
            usuario.guardar_berezi = miUsuario.data['guardar_berezi']
            usuario.save()
            print("Guardado datos usuario")
        except:
            print("Usuario no existe")
            usuario = Usuario(autor= user,
                                    irpf= miUsuario.data['irpf'],
                                    reduccion = miUsuario.data['reduccion'],
                                    guardar_normal='guardar_normal' in miUsuario.data,
                                    guardar_ertain='guardar_ertain' in miUsuario.data,
                                    guardar_berezi='guardar_berezi' in miUsuario.data,) 
            usuario.save()                      

        new_form_data = {}
        new_form_data['irpf'] = usuario.irpf
        new_form_data['reduccion'] = usuario.reduccion
        new_form_data['guardar_normal'] = usuario.guardar_normal
        new_form_data['guardar_ertain'] = usuario.guardar_ertain
        new_form_data['guardar_berezi'] = usuario.guardar_berezi
        miUsuario = FormularioUsuario(new_form_data)
    '''
    return render(request, "BieleGastosApp/usuario_datos.html") #, {'usuario': miUsuario})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)    
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['usuario'],
                                password=cd['contraseina'])
            print(cd['usuario'])
            print(cd['contraseina'])
              
            if user is not None:
                if user.is_active:
                    login_in(request, user)
                    return redirect(usuario)
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
                #
    else:
        form = LoginForm()
    return render (request, "BieleGastosApp/loginuser.html", {'form': form})
                

def recibo(request):
    usuario = request.user.id
    aino_sel =2021
    miConvenio = Convenio()
    miResultado = Resultado()
    user = User.objects.get(id=usuario)
    reduccion = 0

    if request.method=='POST':
        miRecibo= FormularioRecibo(request.POST)
        array_mes = []
        if miRecibo.is_valid():
            infRecibo = miRecibo.cleaned_data
            mes_selecion = miRecibo.data['mes']
            print(mes_selecion)
            miResultado = recibo_imprimir(usuario,mes_selecion,aino_sel,reduccion)
            '''
            for dia_sel in range(1,32,+1):
                try:
                    fecha = str(aino_sel) + '-' + str(mes_sel) + '-' + str(dia_sel)
                    resultado = Horas.objects.get(dia=fecha, autor=usuario)
                    datos_resultado = ((resultado.id),
                                        (resultado.dia),
                                        (resultado.slug),
                                        (resultado.horas_trabajo),
                                        (resultado.viaje_ida),
                                        (resultado.viaje_vuelta),
                                        (resultado.pernocta),
                                        (resultado.semana_3),
                                        (resultado.notas),
                                        (resultado.autor)
                    )
                    print(resultado.dia)
                    array_mes.append(datos_resultado)
                except:
                    print("")
            
            print(array_mes)
            '''
            return render(request, "BieleGastosApp/recibo_impreso.html", {"form": miRecibo,"convenio": miConvenio, "resultado": miResultado})
    
    else:
        miRecibo = FormularioRecibo()
        #print (miRecibo.mes)

    return render(request, "BieleGastosApp/recibo.html", {"form": miRecibo})


def horas(request):
    usuario = request.user.id
    user = User.objects.get(id=usuario)
    aux = request.POST
    new_form_data = {}
    new_form = FormularioHoras(new_form_data)
    #boton cargar

    if request.method=='POST' and ('cargar' in request.POST):
        misHoras=FormularioHoras(request.POST)

        fecha = misHoras.data['dia_year'] + '-' + misHoras.data['dia_month'] + '-' + misHoras.data['dia_day']
        '''
        horas = get_object_or_404(Horas,
                            autor= '2',
                            dia= fecha ,
                            )
        '''
        try:
            horas = Horas.objects.get(
                            autor= usuario,
                            dia= fecha ,
                            )
            new_form_data = {}
            new_form_data['dia'] = horas.dia
            new_form_data['horas_trabajo'] = horas.horas_trabajo
            new_form_data['viaje_ida'] = horas.viaje_ida
            new_form_data['viaje_vuelta'] = horas.viaje_vuelta
            new_form_data['pernocta'] = horas.pernocta
            new_form_data['semana_3'] = horas.semana_3
            new_form = FormularioHoras(new_form_data)
            #if new_form.is_valid():
            #    return render(request, "BieleGastosApp/formulario_horas.html", {"form": new_form})
 
        except Horas.DoesNotExist:
            new_form_data = {}
            new_form_data['dia'] = fecha
            new_form_data['horas_trabajo'] = 0
            new_form_data['viaje_ida'] = 0
            new_form_data['viaje_vuelta'] = 0
            new_form_data['pernocta'] = False
            new_form_data['semana_3'] = False
            new_form = FormularioHoras(new_form_data)
            #if new_form.is_valid():
            #    return render(request, "BieleGastosApp/formulario_horas.html", {"form": new_form})
    
    #boton guardar
    elif request.method=='POST' and ('guardar' in request.POST):
        misHoras=FormularioHoras(request.POST)
        print(misHoras.data)
        fecha = misHoras.data['dia_year'] + '-' + misHoras.data['dia_month'] + '-' + misHoras.data['dia_day']
        try:
            horas = Horas.objects.get(
                            autor= usuario,
                            dia= fecha ,
                            )
            horas.dia = fecha
            horas.horas_trabajo = misHoras.data['horas_trabajo']
            horas.viaje_ida = misHoras.data['viaje_ida']
            horas.viaje_vuelta = misHoras.data['viaje_vuelta']
            horas.pernocta = 'pernocta' in misHoras.data
            horas.semana_3 = 'semana_3' in misHoras.data
            horas.save()
        except Horas.DoesNotExist:
            horas = Horas(autor=user,
                        dia=fecha,
                        horas_trabajo = misHoras.data['horas_trabajo'],
                        viaje_ida= misHoras.data['viaje_ida'],
                        viaje_vuelta=misHoras.data['viaje_vuelta'],
                        pernocta='pernocta' in misHoras.data,
                        semana_3='semana_3' in misHoras.data,
                        notas='')
            horas.save()
        new_form_data = {}
        new_form_data['dia'] = horas.dia
        new_form_data['horas_trabajo'] = horas.horas_trabajo
        new_form_data['viaje_ida'] = horas.viaje_ida
        new_form_data['viaje_vuelta'] = horas.viaje_vuelta
        new_form_data['pernocta'] = horas.pernocta
        new_form_data['semana_3'] = horas.semana_3
        new_form = FormularioHoras(new_form_data)
            
    
    else:
        new_form_data = {}
        new_form_data['horas_trabajo'] = 0
        new_form_data['viaje_ida'] = 0
        new_form_data['viaje_vuelta'] = 0
        new_form_data['pernocta'] = False
        new_form_data['semana_3'] = False
        new_form = FormularioHoras(new_form_data)
        misHoras = FormularioHoras()
            
    #return render(request, "BieleGastosApp/horas.html", {"horas": horas})
    return render(request, "BieleGastosApp/formulario_horas.html", {"form": new_form})

    

def calendario(request):

    miCalendario = FormularioCalendario(request.POST)
    aino = 2021
    
    if request.method=='POST' and ('cargar' in request.POST):
        miCalendario = FormularioCalendario(request.POST)
        obtener_mes(miCalendario.data['mes'],aino)

        return render(request, "BieleGastosApp/mes.html", {"calendario": miCalendario})
        
    return render(request, "BieleGastosApp/calendario.html", {"calendario": miCalendario})

def convenio(request):

    miConvenio = Convenio()

    return render(request, "BieleGastosApp/convenio.html", {"convenio": miConvenio})

def gastos(request):

    misGastos = FormularioGastos()

    return render(request, "BieleGastosApp/gastos.html", {"form": misGastos})

def mail(request):

    if request.method=='POST':
        miEmail=EmailContacto(request.POST)
        if miEmail.is_valid():
            infEmail=miEmail.cleaned_data
            

            #Enviar el formularioa la base de dato FALTA

            return HttpResponse ("Mail enviado correctamente")

    else:
        miEmail = EmailContacto()
    
    return render(request, "BieleGastosApp/mail.html", {"form": miEmail})


def logout(request):
    #Finalizar sesion
    do_logout(request)
    #Redireccionamos a portada
    return ('/')