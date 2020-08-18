from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    """ Class persona
    """

    def __init__(self, nombre, apellido):
        """ Definir atributos
        """
        self.nombre = nombre
        self.apellido = apellido


# crear vista
def saludo_inicial(request):
    """
    Función primera vista que devuelve una respuesta
    Luego hay que linkear esta función con el archivos urls
    """
    # Crear instancias de persona
    person1 = Persona("Marlon Aurelio", "GARCIA MORALES")

    """# Variables
    nombre = "Marlon"
    apellido = "GARCIA"
    """
    fecha_actual = datetime.datetime.now()
    hora = fecha_actual.hour
    min = fecha_actual.minute
    seg = fecha_actual.second
    total = str(hora) + ':' + str(min) + ':' + str(seg)

    sk = ["Python", "Lenguaje C", "Bash", "MySQL"]

    doc_externo = open(
        "/home/marlon/Django/proyecto_inicial/proyecto_inicial/plantillas/entrada.html")

    # crear objeto template.  Se puede llamar coo se quiera
    planti = Template(doc_externo.read())

    # cerrar el documnento
    doc_externo.close()

    # Crear contexto con el diccionario
    contex = Context(
        {"nombre_persona": person1.nombre, "apellido_persona": person1.apellido, "ahora": fecha_actual, "skill": sk})

    # Renderizar el documento
    mensaje = planti.render(contex)

    return HttpResponse(mensaje)


def despedir(request):
    """
    Función segunda  vista que devuelve una respuesta
    Luego hay que linkear esta función con el archivos urls
    """

    mensaje = """
    <html>
        <body>
            <h1 style="color:blue">
                Hasta la próxima amigos.....
            </h1>
        </body>
    </html>
    """
    return HttpResponse(mensaje)


def darfecha(request):
    """
    Devuelve la fecha y hora actual, usando marcador de posición
    """
    fecha_actual = datetime.datetime.now()
    hora = fecha_actual.hour
    min = fecha_actual.minute
    seg = fecha_actual.second
    total = str(hora) + ':' + str(min) + ':' + str(seg)
    mensaje = """
    <html>
        <body>
            <h1 style="color:blue">
                Hora actual --->>> %s
            </h1>
        </body>
    </html>
    """ % total
    return HttpResponse(mensaje)


def calcularedad(request, agno):
    """
    Calcular la edad
    """
    agno = int(agno)
    edadactual = 20
    periodo = agno - 2020
    edadfutura = edadactual + periodo
    mensaje = """
    <html>
        <body>
            <h1 style="color:blue">
                En el año %s vas a tener %s años
            </h1>
        </body>
    </html>
    """ % (agno, edadfutura)
    return HttpResponse(mensaje)
