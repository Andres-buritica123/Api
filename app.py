import os
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Leer usuarios desde Excel
def cargar_usuarios_desde_excel():
    try:
        df = pd.read_excel('trata_de_personas.csv')  # Asegúrate de que esté en la misma carpeta
        return df.to_dict(orient='records')  # Convierte el DataFrame en lista de diccionarios
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return []

# Carga inicial
users = cargar_usuarios_desde_excel()

@app.route('/')
def home():
    return "API de usuarios desde Excel funcionando correctamente"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or not "id" in new_user or not "name" in new_user or not "email" in new_user:
        return jsonify({"error": "Faltan campos: se requieren id, name y email"}), 400
    users.append(new_user)
    
    # Opcional: guardar el nuevo usuario en el archivo Excel
    df = pd.DataFrame(users)
    df.to_excel("usuarios.xlsx", index=False)
    
    return jsonify(new_user), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)