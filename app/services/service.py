from flask import render_template, request
import requests
import json
from domain.models.Consulta import Consulta
from domain.models.Aliado import Aliado
from domain.models.Producto import Producto
from domain.domain import ProcesadorDatos

def _realizar_consulta(data):
    response = requests.get(f"{data.url}/{data.codigo}")
    if response.status_code == 200:
        datos_api = response.json()
        procesador = ProcesadorDatos()
        return procesador.procesar(datos_api)
    else:
        raise Exception("Error al consultar la API externa")

def consultar():
    if request.is_json:
        json_data = request.get_json()
        consulta = Consulta(json_data.get('url'), json_data.get('codigo'))
        if (json_data.get('url') == 'http://127.0.0.1:8081/api/v1/productos'):
            json_producto = _realizar_consulta(consulta)[0]
            producto = Producto(**json_producto)
            return render_template('producto.html', producto=producto)
        elif (json_data.get('url') == 'http://127.0.0.1:8082/api/v1/aliados'):
            json_aliado = _realizar_consulta(consulta)[0]
            aliado = Aliado(**json_aliado)
            return render_template('aliado.html', aliado=aliado)
        else:
            return "Error en la URL"