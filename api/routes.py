from flask import Flask
import json
import pandas as pd

app = Flask("CrimeVis")


def readXls():
    df = pd.read_excel("../src/dataset.xls")
	json = df.to_json()
    return(json)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    msg_j = json.dumps(readXls())
    return(msg_j)


app.run()
