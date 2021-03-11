from flask import Flask
import pandas as pd
import json

app = Flask("CrimeVis")


def readXls():
    df = pd.read_excel("../src/dataset.xls")
	df.to_json()
    return(df)

# App routes


@app.route("/getoccur", methods=["GET"])
def getOccur():
    msg_j = json.dumps(readXls())
    return(msg_j)


app.run()
