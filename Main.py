from flask import Flask, jsonify, render_template,send_from_directory
from Controller.Endpoint import ChatBot

main = Flask(__name__, template_folder='Web', static_folder="Web/Js")

main.register_blueprint(ChatBot)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/js/<path:filename>")
def js_files(filename):
    return send_from_directory("Web/Js", filename)

if __name__=="__main__":
    main.run(debug=True)
