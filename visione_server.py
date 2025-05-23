from flask import Flask, request, jsonify
from flask_cors import CORS
from VisioneAI import VisioneAI

app = Flask(__name__)
CORS(app)

visione_ai = VisioneAI()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Modulo Visione AI attivo."})

@app.route("/registra", methods=["POST"])
def registra():
    dati = request.get_json()
    oggetto = dati.get("oggetto")
    descrizione = dati.get("descrizione")
    if not oggetto or not descrizione:
        return jsonify({"success": False, "errore": "Dati mancanti."})
    visione_ai.registra_visione(oggetto, descrizione)
    return jsonify({"success": True})

@app.route("/log", methods=["GET"])
def log():
    return jsonify({"success": True, "log": visione_ai.get_log()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3016)