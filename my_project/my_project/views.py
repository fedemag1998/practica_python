from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime, timedelta

def saludo(request):
    return HttpResponse("Holis!")


def segunda_vista(request):
    return HttpResponse("<b>Sera que anda?</b>")

 
def mi_nombre_es(request, nombre):
    dia = datetime.now()
    documento_de_texto = f"Mi nombre es: {nombre} y hoy es {dia}"
    return HttpResponse(documento_de_texto)


def pueba_template(request):
    with open("my_project\my_project\plantillas\template1.html") as archivo:
        plantilla = Template(archivo.read())
    diccionario = {'nombre': 'Fede', 'apellido' : 'Maguera'} 
    contexto = Context(diccionario)
    documento_html=plantilla.render(contexto)
    return HttpResponse(documento_html) 


def pueba_template_legacy(request):
    diccionario = {'my_project\db.sqlite3'} 
    plantilla = loader.get_template('template1.html')
    documento_html=plantilla.render(diccionario)
    return HttpResponse(documento_html) 


