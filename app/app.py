from flask import Flask
from services.service import consultar

app = Flask(__name__)

@app.route('/api/v1/consulta', methods=['POST'])
def consultar_enpoint():
    return consultar()

@app.route('/api/v1/say-hello', methods=['GET'])
def say_hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
