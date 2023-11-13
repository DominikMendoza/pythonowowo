import requests
from app.domain import ProcesadorDatos

def realizar_consulta(data):
    url = data.get('url')
    codigo = data.get('codigo')
    print(url + "/"+ codigo)
    response = requests.get(url + "/"+ codigo)
    if response.status_code == 200:
        datos_api = response.json()
        print(datos_api)
        print("uwu")
        procesador = ProcesadorDatos()
        return procesador.procesar(datos_api)
    else:
        raise Exception("Error al consultar la API externa")
