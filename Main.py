from flask import Flask, jsonify, render_template,send_from_directory
from Controller.Endpoint import ChatBot

#Creamos un instancia de la app en Flask
main = Flask(__name__, template_folder='Web', static_folder="Web/Js")


#Cargamos las rutas desde el Controller
main.register_blueprint(ChatBot)


#Definimos la ruta principal que mostrar el Front-End
@main.route("/")
def index():
    return render_template("index.html")


#Cargamos los archivos de la carpeta JS en el index.html
@main.route("/js/<path:filename>")
def js_files(filename):
    """
    Ruta para servir archivos JavaScript desde la carpeta Web/Js.
    
    Args:
        filename (str): Nombre del archivo solicitado.
    
    Returns:
        File: Archivo JS correspondiente.
    """
    return send_from_directory("Web/Js", filename)


#Hacemos un "Deploy" del servidor
if __name__=="__main__":
    main.run(debug=False)
