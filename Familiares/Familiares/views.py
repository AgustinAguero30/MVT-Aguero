from django.http import HttpResponse
from django.template import loader, Context, Template
from AppFamilia.models import Familia


def mostrar_Html(request):

    familiar1 = Familia(nombre="Luco", apellido="Aguero", edad="65",
                        email="luchi.aguero@gmail.com", nacimiento=str('1957-06-10'))
    familiar2 = Familia(nombre="Moco", apellido="Mercado", edad="62",
                        email="silvia.mercado@gmail.com", nacimiento=str('1960-06-11'))
    familiar3 = Familia(nombre="Pelo", apellido="Behr", edad="86",
                        email="nelly.behr@gmail.com", nacimiento=str('1936-06-12'))

    lista = [
        familiar1, familiar2, familiar3
    ]

    for miembro in lista:
        miembro.save()

    diccionario = {
        'familias': lista
    }

    plantilla = loader.get_template('Template.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
