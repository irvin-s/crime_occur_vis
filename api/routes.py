from flask import Flask, request
import json
import pandas as pd

app = Flask("CrimeVis")


def readXls():
    df = pd.read_excel("../src/dataset.xls")
    df = df.query('mes == "Agosto" & marca_celular == "APPLE"')
    df = df[['ano_bo', 'mes', 'latitude', 'longitude', 'rubrica', 'marca_celular']]
    json_msg = df.to_json(orient='index')
    return(json_msg)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    ini_month = request.arqs.get("ini_month")
    #msg_j = json.dumps(readXls())
    msg_j = readXls()
    return(ini_month)


app.run()
