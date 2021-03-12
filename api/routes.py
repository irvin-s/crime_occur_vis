from flask import Flask, request
import json
import pandas as pd

app = Flask("CrimeVis")


def readXls(ini_month,tp_smart):
    df = pd.read_excel("../src/dataset.xls")
    if tp_smart == "APPLE":
        df = df.query('mes == "'+ini_month+'" & marca_celular == "APPLE"')
    else:
        df.query('mes == "'+ini_month+'"')
    df = df[['ano_bo', 'mes', 'latitude', 'longitude', 'rubrica', 'marca_celular']]
    json_msg = df.to_json(orient='index')
    return(json_msg)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    ini_month = request.args.get("ini_month")
    ini_month = request.args.get("tp_smart")
    #msg_j = json.dumps(readXls())
    msg_j = readXls(ini_month)
    return(msg_j)


app.run()
