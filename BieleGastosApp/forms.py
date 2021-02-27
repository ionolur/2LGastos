from django import forms

Sel_mes = [
    (1,'Enero'),
    (2,'Febrero'),
    (3,'Marzo'),
    (4,'Abril'),
    (5,'Mayo'),
    (6,'Junio'),
    (7,'Julio'),
    (8,'Agosto'),
    (9,'Septiembre'),
    (10,'Octubre'),
    (11,'Noviembre'),
    (12,'Diciembre'),
]

Sel_aino = [(2021),(2022)]


class FormularioHoras (forms.Form):
    dia = forms.DateField(required=True, widget=forms.SelectDateWidget)
    horas_trabajo = forms.DecimalField(max_digits=3, decimal_places=1, required=False)
    viaje_ida = forms.DecimalField(max_digits=3, decimal_places=1, required=False)
    viaje_vuelta = forms.DecimalField(max_digits=3, decimal_places=1, required=False)
    pernocta = forms.BooleanField(required=False)
    semana_3 = forms.BooleanField(required=False)
    notas = forms.CharField(required=False, widget=forms.Textarea)

class EmailContacto (forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class FormularioRecibo (forms.Form):
    id_nombre = forms.CharField(max_length=25, required=False)
    mes = forms.DecimalField(max_digits=2, decimal_places=0, required=False,label="Selecione mes", widget=forms.Select(choices=Sel_mes))
    aino = forms.DecimalField(max_digits=4, decimal_places=0, required=False,label="Selecione año", widget=forms.Select(choices=Sel_aino))

class LoginForm (forms.Form):
    usuario = forms.CharField()
    contraseina = forms.CharField(widget=forms.PasswordInput)

class FormularioGastos (forms.Form):
    dia = forms.DateField(required=True, widget=forms.SelectDateWidget)
    concepto = forms.CharField(max_length=25, required=False)
    cantidad = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    moneda = forms.CharField(max_length=25, required=False)
    notas = forms.CharField(required=False, widget=forms.Textarea)

class FormularioCalendario (forms.Form):
    mes = forms.DecimalField(max_digits=2, decimal_places=0, required=False,label="Selecione mes", widget=forms.Select(choices=Sel_mes))
    aino = forms.DecimalField(max_digits=4, decimal_places=0, required=False,label="Selecione año", widget=forms.Select(choices=Sel_aino))

class FormularioUsuario (forms.Form):
    irpf = forms.DecimalField(max_digits=4, decimal_places=2, required=False,label="I.R.P.F")
    reduccion= forms.DecimalField(max_digits=4, decimal_places=2, required=False,label="Reducción")
    guardar_normal  = forms.BooleanField(required=False, label= "Guardar 9-10 / sabado mañana")
    guardar_ertain = forms.BooleanField(required=False, label= "Guardar +10 y sabado tarde")
    guardar_berezi = forms.BooleanField(required=False, label= "Guardar festivo")