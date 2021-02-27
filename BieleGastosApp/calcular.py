

from BieleGastosApp.models import Convenio, Resultado, Calendario, Horas
from decimal import Decimal

# Cuartos dia 1:Normal; 2:9-10 y sabadao mañana; 3:Mas 10 y sabado tarde; 4: Domingo; 5:Viaje
Cuartos_Dia = [0 for i in range(96)]
Contaje_Horas = (0.0, 0.0, 0.0, 0.0, 0.0)

#Datos que vendrán como parametros

usuario = 2
mes = 1
aino = 2021
reduccion = 0


def obtener_datos (usuario,mes,aino):

    array_mes = []
    '''
    longitud = len(Res_Act_Array)
    for i in range(0,longitud,+1):
        #Obtenemos la fecha separada en una lista siendo [0]:año; [1]:mes; [2]:dia
        data = Res_Act_Array[i][1].split(sep='-')
        if Res_Act_Array[i][9]==usuario and int(data[0])==aino and int(data[1])==mes:
            array_mes.append(Res_Act_Array[i])
    '''
    for dia_sel in range(1,32,+1):
        fecha = str(aino) + '-' + str(mes) + '-' + str(dia_sel)
        try:
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
            array_mes.append(datos_resultado)
        except:
            continue
    return array_mes

def buscar_tipo_dia (aino, mes, dia):
            
    try:
            resultado = Calendario.objects.get(dia=dia, mes=mes)
            tipo = resultado.codigo
    except:
        print("Dia no encontrado")



    return tipo

#Inicializar Cuartos de dia
def Inicializar ():
    for i in range(0,96,+1):    
        Cuartos_Dia[i]=0

# Calcula las hora de un dia normal de trabajo
def calcular_dia (Horas_Trabajo, Viaje_Ida, Viaje_Vuelta, Sem_3, Pernocta, reduccion):
    Inicializar()
    Saltos = 0
    Saltos_Mem = 0
    reduccion_float = float(reduccion)
    Saltos_jornada= 32.0 - ((32.0*reduccion_float)/100)
    if Viaje_Ida != 0.0:
        Saltos = int(Viaje_Ida/0.25)
        
        for i in range (0,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada :
                Cuartos_Dia[i]=5
        
        Saltos_Mem = Saltos
         

    if Horas_Trabajo != 0.0:
        Saltos = Saltos + int(Horas_Trabajo/0.25)
        
        for i in range (Saltos_Mem,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada and i < 40:
                Cuartos_Dia[i]=2
            # >10 Horas
            if i >= 40:
                Cuartos_Dia[i]=3
        
        Saltos_Mem = Saltos
    
    if Viaje_Vuelta !=0.0:
        Saltos = Saltos + int(Viaje_Vuelta/0.25)
        for i in range (Saltos_Mem,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada :
                Cuartos_Dia[i]=5
    print ("Día Normal")



# Calcula las hora de un viernes especial
def calcular_viernes (Horas_Trabajo, Viaje_Ida, Viaje_Vuelta, Sem_3, Pernocta, reduccion):
    Inicializar()
    Saltos = 0
    Saltos_Mem = 0
    reduccion_float = float(reduccion)
    Saltos_jornada= 24.0 - ((24.0*reduccion_float)/100)
    if Viaje_Ida != 0:
        Saltos = int(Viaje_Ida/0.25)
        
        for i in range (0,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada :
                Cuartos_Dia[i]=5
        
        Saltos_Mem = Saltos
         

    if Horas_Trabajo != 0:
        Saltos = Saltos + int(Horas_Trabajo/0.25)
        
        for i in range (Saltos_Mem,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada and i <= 40:
                Cuartos_Dia[i]=2
            # >10 Horas
            if i >= 40:
                Cuartos_Dia[i]=3
        
        Saltos_Mem = Saltos
    
    if Viaje_Vuelta !=0:
        Saltos = Saltos + int(Viaje_Vuelta/0.25)
        for i in range (Saltos_Mem,Saltos,+1):
            if i < Saltos_jornada:
                Cuartos_Dia[i]=1
            # 9-10 hora
            if i >= Saltos_jornada :
                Cuartos_Dia[i]=5

    print ("Viernes Especial")

# Calcula las hora de un dia sabado o puente
def calcular_sabado (Horas_Trabajo, Viaje_Ida, Viaje_Vuelta, Sem_3, Pernocta):
    Inicializar()
    Saltos = 0
    Saltos_Mem = 0
    if Viaje_Ida != 0:
        Saltos = int(Viaje_Ida/0.25)
        
        for i in range (0,Saltos,+1):
            Cuartos_Dia[i]=5
        
        Saltos_Mem = Saltos

    if Horas_Trabajo != 0:
        Saltos = Saltos + int(Horas_Trabajo/0.25)
        
        for i in range (Saltos_Mem,Saltos,+1):
            # hasta 5 horas
            if i < 20:
                Cuartos_Dia[i]=2
            # mas de 5 horas
            if i >= 20:
                Cuartos_Dia[i]=3

        Saltos_Mem = Saltos
    
    if Viaje_Vuelta !=0:
        Saltos = Saltos + int(Viaje_Vuelta/0.25)
        for i in range (Saltos_Mem,Saltos,+1):
                Cuartos_Dia[i]=5

    print ("Sabado o puente")
        
    

# Calcula las hora de un dia domingo o festivo 
def calcular_domingo (Horas_Trabajo, Viaje_Ida, Viaje_Vuelta, Sem_3, Pernocta):
    Inicializar()
    Saltos = 0
    Saltos_Mem = 0

    if Viaje_Ida != 0:
        Saltos = int(Viaje_Ida/0.25)
        
        for i in range (0,Saltos,+1):
            Cuartos_Dia[i]=5
        
        Saltos_Mem = Saltos

    if Horas_Trabajo != 0:
        Saltos = Saltos + int(Horas_Trabajo/0.25)
        
        for i in range (Saltos_Mem,Saltos,+1):
                Cuartos_Dia[i]=4
    
    Saltos_Mem = Saltos
    
    if Viaje_Vuelta !=0:
        Saltos = Saltos + int(Viaje_Vuelta/0.25)
        for i in range (Saltos_Mem,Saltos,+1):
                Cuartos_Dia[i]=5

    print ("Domingo o festivo")

def contaje (Cuartos_Dia, Tipo, reduccion, Convenio):
    Cuartos_Horas_Simple = 0
    Cuartos_Horas_Ertain = 0
    Cuartos_Horas_Berezi = 0
    Cuartos_Horas_Viaje = 0
    Cuartos_Horas_Normal = 0
    Horas_Normales = 0
    Res = Resultado()

    for i in range (0,96,+1):
        if Cuartos_Dia[i] == 2:
            Cuartos_Horas_Simple = Cuartos_Horas_Simple + 1
        elif Cuartos_Dia[i] == 3:
            Cuartos_Horas_Ertain = Cuartos_Horas_Ertain + 1
        elif Cuartos_Dia[i] == 4:
            Cuartos_Horas_Berezi = Cuartos_Horas_Berezi + 1
        elif Cuartos_Dia[i] == 5:
            Cuartos_Horas_Viaje = Cuartos_Horas_Viaje +1
        elif Cuartos_Dia[i] == 1:
            Cuartos_Horas_Normal = Cuartos_Horas_Normal+1

    Horas_dia_Normal = 8 - ((8*reduccion)/100)
    Horas_dia_Viernes =  6 - ((6*reduccion)/100)
    Medio_Festivo = 5
    Completo_Festivo = 10

    
    Res.Plus_A = Cuartos_Horas_Simple/4
    Res.Plus_B = Cuartos_Horas_Ertain/4
    Res.Plus_C = Cuartos_Horas_Berezi/4
    Res.Desplazamiento = Cuartos_Horas_Viaje/4
    Horas_Normales = Cuartos_Horas_Normal/4

    # Comprobar si son completos o medios en funcion de reduccion y quitar a Res
    
    if Tipo == 0 or Tipo ==1:
        if Res.Plus_A >= (Completo_Festivo-Horas_dia_Normal):
            Res.Dia_Normal = 1
            Res.Dia_Normal_euro = Res.Dia_Normal * Convenio.dia_trabajo
            Res.Plus_A = Res.Plus_A - 2
    elif Tipo == 2:
        if Res.Plus_A >= (Completo_Festivo-Horas_dia_Viernes):
            Res.Viernes = 1
            Res.Viernes_euro = Res.Viernes * Convenio.viernes
            Res.Plus_A = Res.Plus_A - 4
    elif Tipo == 3:
        if Res.Plus_A >= Medio_Festivo:
            Res.Medio_Sabado = 1
            Res.Medio_Sabado_euro = Res.Medio_Sabado * Convenio.sabado_medio
            Res.Plus_A = Res.Plus_A - Medio_Festivo
        if Res.Plus_B >= Medio_Festivo:
            Res.Completo_Sabado = 1
            Res.Completo_Sabado_euro = Res.Completo_Sabado * Convenio.sabado_completo
    elif Tipo == 4:
        if Res.Plus_C >= Medio_Festivo and Res.Plus_C < Completo_Festivo:
            Res.Medio_Domingo = 1
            Res.Medio_Domingo_euro = Res.Medio_Domingo * Convenio.domingo_medio
            Res.Plus_C = Res.Plus_C - Medio_Festivo
        elif Res.Plus_C >= Completo_Festivo:
            Res.Completo_Domingo = 1
            Res.Completo_Domingo_euro = Res.Completo_Domingo * Convenio.domingo_completo
            Res.Plus_C = Res.Plus_C - Completo_Festivo
            
    

    if Tipo == 0 or Tipo == 1:
        if Horas_Normales < Horas_dia_Normal:
            Res.Horas_a_Deber = Horas_dia_Normal - Horas_Normales
    
    if Tipo == 2:
        if Horas_Normales < Horas_dia_Viernes:
            Res.Horas_a_Deber= Horas_dia_Viernes -Horas_Normales
    
    Res.Plus_A_euro = Res.Plus_A * Convenio.extra_normal
    Res.Plus_B_euro = Res.Plus_B * Convenio.extra_ertain
    Res.Plus_C_euro = Res.Plus_C * Convenio.extra_especial
    Res.Desplazamiento_euro = Res.Desplazamiento * Convenio.horas_viaje

    Res.Total_Plus = Res.Plus_A_euro + Res.Plus_B_euro + Res.Plus_C_euro
    Res.Total_PeM = Res.Dia_Normal_euro + Res.Viernes_euro + Res.Medio_Sabado_euro + Res.Completo_Sabado_euro + Res.Medio_Domingo_euro + Res.Completo_Domingo_euro
    

    return Res


def calcular (Aino, Mes, Dia, Horas_Trabajo, Viaje_Ida, Viaje_Vuelta, Pernocta, Sem_3, Tipo, reduccion):

    miconvenio = Convenio

    if Tipo == 0 or Tipo == 1:
        calcular_dia (float(Horas_Trabajo), float(Viaje_Ida), float(Viaje_Vuelta), Sem_3, Pernocta, reduccion)
        #print("Normal")
        
    elif Tipo == 2:
        calcular_viernes (float(Horas_Trabajo), float(Viaje_Ida), float(Viaje_Vuelta), Sem_3, Pernocta, reduccion)
        #print("Viernes")
        
    elif Tipo == 3:
        calcular_sabado (float(Horas_Trabajo), float(Viaje_Ida), float(Viaje_Vuelta), Sem_3, Pernocta)
        #print("Sabado")
        
    elif Tipo == 4:
        calcular_domingo (float(Horas_Trabajo), float(Viaje_Ida), float(Viaje_Vuelta), Sem_3, Pernocta)
        #print("Domingo")
        

    Contaje_Horas = contaje(Cuartos_Dia,Tipo, reduccion, miconvenio)

    #Pernocta
    if Pernocta == 1:
        if Sem_3 == 0:
            if Tipo == 0 or Tipo == 1 or Tipo ==2:
                Contaje_Horas.Pernocta_dia = 1
                Contaje_Horas.Pernocta_dia_euro = Contaje_Horas.Pernocta_dia * miconvenio.pernocta_normal
            elif Tipo == 3 or Tipo == 4:
                Contaje_Horas.Pernocta_festivo = 1
                Contaje_Horas.Pernocta_festivo_euro = Contaje_Horas.Pernocta_festivo * miconvenio.pernocta_festivo
        else:
            if Tipo == 0 or Tipo == 1 or Tipo ==2:
                Contaje_Horas.Pernocta_dia_sem3 = 1
                Contaje_Horas.Pernocta_dia_sem3_euro = Contaje_Horas.Pernocta_dia_sem3 * (miconvenio.pernocta_normal+miconvenio.tercera_semana)
            elif Tipo == 3 or Tipo == 4:
                Contaje_Horas.Pernocta_festivo_sem3 = 1
                Contaje_Horas.Pernocta_festivo_sem3_euro = Contaje_Horas.Pernocta_festivo_sem3 * (miconvenio.pernocta_festivo+miconvenio.tercera_semana)
    
    Contaje_Horas.Total_Pernocta = Contaje_Horas.Pernocta_dia_euro + Contaje_Horas.Pernocta_festivo_euro + Contaje_Horas.Pernocta_dia_sem3_euro + Contaje_Horas.Pernocta_festivo_sem3_euro

    return Contaje_Horas

def recibo_imprimir (usuario, mes, aino, reduccion):

    mes_datos = obtener_datos(usuario,mes,aino)
    print(mes_datos)
    #a partir de aqui recorreriamos los datos de la lista de mes_datos
    long_mes = len(mes_datos)
    print(long_mes)

    Recibo = Resultado()

    if long_mes > 0:
        for i in range(0,long_mes,+1):
            print(mes_datos[i][1].day)
            print(mes_datos[i][1].month)
            print(mes_datos[i][1].year)
            #data = mes_datos[i][1].split(sep='-')
            tipo_dia = buscar_tipo_dia(mes_datos[i][1].year,mes_datos[i][1].month,mes_datos[i][1].day)
            horas = calcular(mes_datos[i][1].year,mes_datos[i][1].month,mes_datos[i][1].day,mes_datos[i][3],mes_datos[i][4],mes_datos[i][5],mes_datos[i][6],mes_datos[i][7],tipo_dia,reduccion)
            # suma los campos          
            Recibo.Plus_A = Recibo.Plus_A + horas.Plus_A
            Recibo.Plus_A_euro = Recibo.Plus_A_euro + horas.Plus_A_euro
            Recibo.Plus_B = Recibo.Plus_B + horas.Plus_B
            Recibo.Plus_B_euro = Recibo.Plus_B_euro + horas.Plus_B_euro
            Recibo.Plus_C = Recibo.Plus_C + horas.Plus_C
            Recibo.Plus_C_euro = Recibo.Plus_C_euro + horas.Plus_C_euro
            Recibo.Total_Plus = Recibo.Total_Plus + horas.Total_Plus
            Recibo.Dia_Normal = Recibo.Dia_Normal + horas.Dia_Normal
            Recibo.Dia_Normal_euro = Recibo.Dia_Normal_euro + horas.Dia_Normal_euro
            Recibo.Viernes = Recibo.Viernes + horas.Viernes
            Recibo.Viernes_euro = Recibo.Viernes_euro + horas.Viernes_euro
            Recibo.Medio_Sabado = Recibo.Medio_Sabado + horas.Medio_Sabado
            Recibo.Medio_Sabado_euro = Recibo.Medio_Sabado_euro + horas.Medio_Sabado_euro
            Recibo.Completo_Sabado = Recibo.Completo_Sabado + horas.Completo_Sabado
            Recibo.Completo_Sabado_euro = Recibo.Completo_Sabado_euro + horas.Completo_Sabado_euro 
            Recibo.Medio_Domingo = Recibo.Medio_Domingo + horas.Medio_Domingo 
            Recibo.Medio_Domingo_euro = Recibo.Medio_Domingo_euro + horas.Medio_Domingo_euro
            Recibo.Completo_Domingo = Recibo.Completo_Domingo + horas.Completo_Domingo 
            Recibo.Completo_Domingo_euro = Recibo.Completo_Domingo_euro + horas.Completo_Domingo_euro
            Recibo.Total_PeM = Recibo.Total_PeM + horas.Total_PeM
            Recibo.Desplazamiento = Recibo.Desplazamiento + horas.Desplazamiento
            Recibo.Desplazamiento_euro = Recibo.Desplazamiento_euro + horas.Desplazamiento_euro
            Recibo.Pernocta_dia = Recibo.Pernocta_dia + horas.Pernocta_dia
            Recibo.Pernocta_dia_euro = Recibo.Pernocta_dia_euro + horas.Pernocta_dia_euro
            Recibo.Pernocta_festivo = Recibo.Pernocta_festivo + horas.Pernocta_festivo
            Recibo.Pernocta_festivo_euro = Recibo.Pernocta_festivo_euro + horas.Pernocta_festivo_euro
            Recibo.Pernocta_dia_sem3 = Recibo.Pernocta_dia_sem3 + horas.Pernocta_dia_sem3
            Recibo.Pernocta_dia_sem3_euro = Recibo.Pernocta_dia_sem3_euro + horas.Pernocta_dia_sem3_euro
            Recibo.Pernocta_festivo_sem3 = Recibo.Pernocta_festivo_sem3 + horas.Pernocta_festivo_sem3
            Recibo.Pernocta_festivo_sem3_euro = Recibo.Pernocta_festivo_sem3_euro + horas.Pernocta_festivo_sem3_euro 
            Recibo.Total_Pernocta = Recibo.Total_Pernocta + horas.Total_Pernocta 
            Recibo.Kilometros = Recibo.Kilometros + horas.Kilometros
            Recibo.Kilometros_euro = Recibo.Kilometros_euro + horas.Kilometros_euro
            Recibo.Horas_a_Deber = Recibo.Horas_a_Deber + horas.Horas_a_Deber

    Recibo.Total_Bruto = Recibo.Total_Plus + Recibo.Total_PeM + Recibo.Desplazamiento_euro + Recibo.Total_Pernocta + Recibo.Kilometros_euro

    return Recibo
