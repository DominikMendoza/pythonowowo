from flask import Flask, request, render_template
from app.service import realizar_consulta

app = Flask(__name__)

@app.route('/mi_endpoint', methods=['POST'])
def mi_endpoint():
    data = request.get_json()
    print(data.url)
    print(data.codigo)

    try:
        # Llama a la función del servicio para realizar la consulta
        datos_api = realizar_consulta(data)
        
        # Renderiza la tabla HTML con los datos recibidos
        return render_template('tabla.html', datos_api=datos_api)
    
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/print', methods=['POST'])
def print_url():
    if request.is_json:
        datos_api = realizar_consulta(request.get_json())
        dato = datos_api[0]
        print(dato)
        return render_template('tabla.html', dato=dato)
@app.route('/getHello', methods=['GET'])
def getHello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
