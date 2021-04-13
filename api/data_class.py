import json
import pandas as pd

def readXls(ini_month, brand):
    df = pd.read_excel("../data/dataset.xls")
    df = df.dropna(subset=['latitude', 'longitude'])
    if brand == "APPLE":
        df = df.query('mes == "'+ini_month+'" & marca_celular == "APPLE"')
    elif brand == "ANDROID":
        df = df.query('mes == "'+ini_month+'" & marca_celular != "APPLE"')
    else:
        df = df.query('mes == "'+ini_month+'"')
    df = df[0:1000]
    df = df[['ano_bo', 'mes', 'latitude', 'longitude', 'rubrica', 'marca_celular']]
    json_msg = df.to_json(orient='records')
    return(json_msg)
