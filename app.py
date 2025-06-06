import os
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Leer usuarios desde CSV
def cargar_usuarios_desde_csv():
    try:
        df = pd.read_csv('trata_de_personas.csv')  # Asegúrate de que este archivo exista
        return df.to_dict(orient='records')
    except Exception as e:
        print("Error al leer el archivo CSV:", e)
        return []

# Guardar usuarios al CSV
def guardar_usuarios_a_csv():
    df = pd.DataFrame(users)
    df.to_csv("usuarios.csv", index=False)

# Carga inicial
users = cargar_usuarios_desde_csv()

@app.route('/')
def home():
    return "✅ API de usuarios funcionando correctamente desde CSV"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or not all(k in new_user for k in ("id", "name", "email")):
        return jsonify({"error": "Faltan campos: se requieren id, name y email"}), 400

    if any(user["id"] == new_user["id"] for user in users):
        return jsonify({"error": "El ID ya existe"}), 400

    users.append(new_user)
    guardar_usuarios_a_csv()
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user)
            guardar_usuarios_a_csv()
            return jsonify(user), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if any(user['id'] == user_id for user in users):
        users = [user for user in users if user['id'] != user_id]
        guardar_usuarios_a_csv()
        return jsonify({'message': f'Usuario {user_id} eliminado'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)