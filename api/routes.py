from flask import Flask

app = Flask("CrimeViz")

#App routes
@app.route("/olamundo", methods=["POST"])
def olaMundo():
    return{"msg": "Olá Mundo!"}

app.run(host = '0.0.0.0')