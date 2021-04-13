from flask import Flask, request
from flask_cors import CORS
import data_class

app = Flask("CrimeVis")
cors = CORS(app, resources={r"/getoccur/*": {"origins": "*"}})

# App routes

@app.route("/getoccur", methods=["GET"])
def getOccur():
    ini_month = request.args.get("ini_month")
    brand = request.args["brand"]
    #msg_j = json.dumps(readXls())
    msg_j = data_class.readXls(ini_month, brand)
    return(msg_j)

if __name__ == "__main__":
    app.run()
