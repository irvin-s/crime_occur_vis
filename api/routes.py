from flask import Flask, request
import json
import pandas as pd

app = Flask("CrimeVis")


def readXls(ini_month, brand):
    df = pd.read_excel("../src/dataset.xls")
    if brand == "APPLE":
        df = df.query('mes == "'+ini_month+'" & marca_celular == "APPLE"')
    elif brand == "ANDROID":
        df = df.query('mes == "'+ini_month+'" & marca_celular != "APPLE"')
    else:
        df = df.query('mes == "'+ini_month+'"')
    df = df[['ano_bo', 'mes', 'latitude', 'longitude', 'rubrica', 'marca_celular']]
    json_msg = df.to_json(orient='index')
    return(json_msg)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    ini_month = request.args.get("ini_month")
    brand = request.args.get("brand")
    #msg_j = json.dumps(readXls())
    msg_j = readXls(ini_month, brand)
    return(msg_j)


app.run()
