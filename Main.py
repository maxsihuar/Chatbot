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

#Cargamos los archivos de la capeerta Css en el index.html
@main.route("/Css/<path:filename>")
def css_file(filename):
    """
    Ruta para servir archivos CSS desde la carpeta Web/Css.

    Args:
        filename (str): Nombre del archivo CSS solicitado.

    Returns:
        File: Archivo CSS correspondiente.
    """
    return send_from_directory("Web/Css", filename)

#Cargamos los archivos de la capeerta Html en el index.html
@main.route("/Html/<path:filename>")
def html_file(filename):
    """
    Ruta para servir archivos Html desde la carpeta Web/Html 
    Args:
        filename (str): Nombre del archivo Hmtl solicitado.

    Returns:
        File: Archivo Html correspondiente.
    """
    return send_from_directory("Web/Html", filename)

#Cargamos los archivos de la capeerta Html en el index.html
@main.route("/Img/<path:filename>")
def Img_file(filename):
    """
    Ruta para servir archivos png, jpg, etc desde la carpeta Web/Img 
    Args:
        filename (str): Nombre del archivo Img solicitado.

    Returns:
        File: Archivo Img correspondiente.
    """
    return send_from_directory("Web/Img", filename)

#Hacemos un "Deploy" del servidor
if __name__=="__main__":
    main.run(debug=True)
