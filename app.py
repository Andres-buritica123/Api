import os
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Ruta al archivo CSV
archivo_csv = 'trata_de_personas.csv'

# Leer los datos desde el CSV
def cargar_casos():
    try:
        df = pd.read_csv(archivo_csv)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error al leer CSV: {e}")
        return []

# Guardar datos al CSV
def guardar_casos(casos):
    try:
        df = pd.DataFrame(casos)
        df.to_csv(archivo_csv, index=False)
    except Exception as e:
        print(f"Error al guardar CSV: {e}")

# Carga inicial
casos = cargar_casos()

@app.route('/')
def home():
    return "API de Casos de Trata funcionando correctamente"

@app.route('/casos', methods=['GET'])
def get_casos():
    return jsonify(casos)

@app.route('/casos', methods=['POST'])
def agregar_caso():
    nuevo = request.get_json()
    casos.append(nuevo)
    guardar_casos(casos)
    return jsonify(nuevo), 201

@app.route('/casos/<int:indice>', methods=['PUT'])
def actualizar_caso(indice):
    if indice < 0 or indice >= len(casos):
        return jsonify({"error": "Índice fuera de rango"}), 404
    actualizado = request.get_json()
    casos[indice].update(actualizado)
    guardar_casos(casos)
    return jsonify(casos[indice]), 200

@app.route('/casos/<int:indice>', methods=['DELETE'])
def eliminar_caso(indice):
    global casos
    if indice < 0 or indice >= len(casos):
        return jsonify({"error": "Índice fuera de rango"}), 404
    eliminado = casos.pop(indice)
    guardar_casos(casos)
    return jsonify({"mensaje": "Caso eliminado", "caso": eliminado}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)