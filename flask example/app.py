import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

KEY = "?access_key=314dd5e57ab376e68890c481801a47d7"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")
    res = requests.get(f"http://data.fixer.io/api/latest{KEY}",
                       params={"base": "USD", "symbols": currency})

    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})
