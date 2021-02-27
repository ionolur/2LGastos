

from BieleGastosApp.models import Calendario

def obtener_mes(mes, aino):
    res_mes = []
    f = open('BieleGastosApp/templates/BieleGastosApp/mes.html','w')
    html="""
        {% extends "BieleGastosApp/base.html" %}

        {% load static %}

        {% block content %}
        <div align="center">
            <form action="" method="POST" >
                <table>
    
                    {{ calendario.mes }}
    
                </table>
                <input type="submit" value="Cargar" name="cargar"> {% csrf_token %}
            </form>
            
        </div>
        <div align="center">
            <table width="50%" border="0" align="center" id="mes_calendario">
        <th>
            <td align='center'>Lun </td>
            <td align='center' >Mar </td>
            <td align='center'>Mie </td>
            <td align='center'>Jue </td>
            <td align='center'>Vie </td>
            <td align='center'>Sab </td>
            <td align='center'>Dom </td>
        </th>
    """

    for i in range (1,32,+1):
        try:
            dia = Calendario.objects.get(
                            mes= mes,
                            dia= i
                            )
            codigo = "#E3E3E3"
            if dia.codigo == 2:
                codigo = "#69BCB8"
            elif dia.codigo == 3:
                codigo = "#AEDE4A"
            elif dia.codigo == 4:
                codigo = "#DE544A"
            if dia.dia == 1:
                html = html + "<tr>"
                html = html + "\n\t<td> W" + str(dia.semana) + "</td>"
                for i in range(1,dia.dia_sem,+1):
                    html = html + "\n\t<td></td>"
                html = html + "\n\t<td style='background-color:"+ codigo + "' align='center'> " + str(dia.dia) + "</td>"
                mem_sem = dia.semana
            else:
                if mem_sem != dia.semana:
                    html = html + "\n</tr>"
                    html = html + "\n<tr>"
                    html = html + "\n\t<td> W" + str(dia.semana) + "</td>"
                    html = html + "\n\t<td style='background-color:"+ codigo + "' align='center'> " + str(dia.dia) + "</td>"
                else:
                    html = html + "\n\t<td style='background-color:"+ codigo + "' align='center'> " + str(dia.dia) + "</td>"
            mem_sem=dia.semana
        except Calendario.DoesNotExist:
            html = html + "\n</tr>"
    html = html + """\n</tr>
     </table>  

        </div>
        
    {% endblock %}

    """
    f.write(html)
    f.close


