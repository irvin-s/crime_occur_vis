from flask import Flask, request
from flask_cors import CORS
import json
import pandas as pd

app = Flask("CrimeVis")
cors = CORS(app, resources={r"/getoccur/*": {"origins": "*"}})

def readXls(ini_month, brand):
    df = pd.read_excel("../src/dataset.xls")
    df = df.dropna(subset=['latitude', 'longitude'])
    df = df.iloc[:500].max()
    if brand == "APPLE":
        df = df.query('mes == "'+ini_month+'" & marca_celular == "APPLE"')
    elif brand == "ANDROID":
        df = df.query('mes == "'+ini_month+'" & marca_celular != "APPLE"')
    else:
        df = df.query('mes == "'+ini_month+'"')
    df = df[['ano_bo', 'mes', 'latitude', 'longitude', 'rubrica', 'marca_celular']]
    json_msg = df.to_json(orient='records')
    return(json_msg)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    ini_month = request.args.get("ini_month")
    brand = request.args["brand"]
    #msg_j = json.dumps(readXls())
    msg_j = readXls(ini_month, brand)
    return(msg_j)


app.run()
