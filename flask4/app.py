from flask import Flask,render_template,request,jsonify
#import jsonify
import requests 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert",methods=["POST"])
def convert():
    #query for currency rate
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest?access_key=fd90d71fe1218510c280d457149ad749",params={"symbols":currency})

    #make sure request succeseded
    if res.status_code != 200:
        return jsonify({"success":False})
    #make sure currency is in response
    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success":False})
    return jsonify({"success":True,"rate": data["rates"][currency]})




