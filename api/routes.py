from flask import Flask
import json
import pandas as pd

app = Flask("CrimeVis")


def readXls():
    df = pd.read_excel("../src/dataset.xls", encoding='utf8')
    df = df[0:5].query('MARCA_CELULAR == "APPLE"')
    json_msg = df.to_json()
    return(json_msg)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    #msg_j = json.dumps(readXls())
    msg_j = readXls()
    return(msg_j)


app.run()
