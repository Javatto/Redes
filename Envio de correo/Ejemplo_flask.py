from flask import Flask
import Funciones


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Servidor de Flask"

@app.route('/enviar/<destinatario>')
def interface(destinatario):
    Funciones.mandar_correo(destinatario)
    return "Correo enviado exitosamente!!!"

if __name__ == '__main__':
    app.run( debug=False)

