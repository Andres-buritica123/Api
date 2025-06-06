import os
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Leer usuarios desde CSV
def cargar_usuarios_desde_csv():
    try:
        df = pd.read_csv('trata_de_personas.csv', encoding='utf-8')  # Asegúrate de que el archivo esté en la raíz del proyecto
        return df.to_dict(orient='records')  # Convierte el DataFrame en lista de diccionarios
    except Exception as e:
        print("❌ Error al leer el archivo CSV:", e)
        return []

# Carga inicial de datos
users = cargar_usuarios_desde_csv()

@app.route('/')
def home():
    return "✅ API de usuarios desde CSV funcionando correctamente"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
