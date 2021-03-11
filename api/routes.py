from flask import Flask
import json
import pandas as pd

app = Flask("CrimeVis")

#App routes
@app.route("/getoccur", methods=["GET"])
def getOccur():
    occur = {
		"ANO_BO": "2020",
		"NUM_BO": "877138",
		"NUMERO_BOLETIM": "877138/2020",
		"BO_INICIADO": "30/06/2020 21:04",
		"BO_EMITIDO": "01/07/2020 00:04",
		"DATAOCORRENCIA": "06/26/2020",
		"HORAOCORRENCIA": "19:30",
		"PERIDOOCORRENCIA": "A NOITE",
		"DATACOMUNICACAO": "06/30/2020",
		"DATAELABORACAO": "30/06/2020 21:04",
		"BO_AUTORIA": "Desconhecida",
		"FLAGRANTE": "",
		"NUMERO_BOLETIM_PRINCIPAL": " ",
		"LOGRADOURO": "RUA GOBBO FERRUCCIO",
		"NUMERO": "19",
		"BAIRRO": "RIO PEQUENO",
		"CIDADE": "S.PAULO",
		"UF": "SP",
		"LATITUDE": "-23.571925778839",
		"LONGITUDE": "-46.743817385774",
		"DESCRICAOLOCAL": "",
		"EXAME": " ",
		"SOLUCAO": "",
		"DELEGACIA_NOME": "DELEGACIA ELETRONICA",
		"DELEGACIA_CIRCUNSCRICAO": "",
		"ESPECIE": "",
		"RUBRICA": "Roubo (art. 157) - TRANSEUNTE",
		"DESDOBRAMENTO": " ",
		"STATUS": "Consumado",
		"NOMEPESSOA": " ",
		"TIPOPESSOA": " ",
		"VITIMAFATAL": " ",
		"RG": " ",
		"RG_UF": " ",
		"NATURALIDADE": " ",
		"NACIONALIDADE": " ",
		"SEXO": " ",
		"DATANASCIMENTO": " ",
		"IDADE": " ",
		"ESTADOCIVIL": " ",
		"PROFISSAO": " ",
		"GRAUINSTRUCAO": " ",
		"CORCUTIS": " ",
		"NATUREZAVINCULADA": " ",
		"TIPOVINCULO": " ",
		"RELACIONAMENTO": " ",
		"PARENTESCO": " ",
		"PLACA_VEICULO": " ",
		"UF_VEICULO": " ",
		"CIDADE_VEICULO": " ",
		"DESCR_COR_VEICULO": " ",
		"DESCR_MARCA_VEICULO": " ",
		"ANO_FABRICACAO": " ",
		"ANO_MODELO": " ",
		"DESCR_TIPO_VEICULO": " ",
		"QUANT_CELULAR": " ",
		"MARCA_CELULAR": "APPLE"
	}
		readXls()
    	msg_j = json.dumps(occur)
    return(msg_j)

def readXls():
	df = pd.read_excel("src.dataset.xls")
	return(df)

app.run()

