from flask import Flask

app = Flask("CrimeVis")

#App routes
@app.route("/getoccur", methods=["GET"])
def olaMundo():
    return{"msg": "Olá Mundo!"}

app.run(host = '0.0.0.0')