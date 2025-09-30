import json
import pandas as pd
import duckdb

#Create a function to convert xls duckbd database and filter by month and brand limited to 1000 records
def readXls(ini_month, brand):
    con = duckdb.connect(database=':memory:')
    if brand == "APPLE":
        query = f"""
        SELECT ano_bo, mes, latitude, longitude, rubrica, marca_celular
        FROM read_excel_auto('../data/dataset.xls')
        WHERE mes = '{ini_month}' AND marca_celular = 'APPLE'
        LIMIT 1000
        """
    elif brand == "ANDROID":
        query = f"""
        SELECT ano_bo, mes, latitude, longitude, rubrica, marca_celular
        FROM read_excel_auto('../data/dataset.xls')
        WHERE mes = '{ini_month}' AND marca_celular != 'APPLE'
        LIMIT 1000
        """
    else:
        query = f"""
        SELECT ano_bo, mes, latitude, longitude, rubrica, marca_celular
        FROM read_excel_auto('../data/dataset.xls')
        WHERE mes = '{ini_month}'
        LIMIT 1000
        """
    df = con.execute(query).fetchdf()
    df = df.dropna(subset=['latitude', 'longitude'])
    json_msg = df.to_json(orient='records')
    return(json_msg)