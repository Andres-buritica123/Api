import os
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {"id": 1, "name": "Juan", "email": "juan@mail.com"},
  {"id": 2, "name": "Ana", "email": "ana@mail.com"},
  {"id": 3, "name": "Carlos", "email": "carlos@mail.com"},
  {"id": 4, "name": "Luisa", "email": "luisa@mail.com"},
  {"id": 5, "name": "Pedro", "email": "pedro@mail.com"},
  {"id": 6, "name": "María", "email": "maria@mail.com"},
  {"id": 7, "name": "Andrés", "email": "andres@mail.com"},
  {"id": 8, "name": "Sofía", "email": "sofia@mail.com"},
  {"id": 9, "name": "Diego", "email": "diego@mail.com"},
  {"id": 10, "name": "Valentina", "email": "valentina@mail.com"},
  {"id": 11, "name": "Camilo", "email": "camilo@mail.com"},
  {"id": 12, "name": "Isabella", "email": "isabella@mail.com"},
  {"id": 13, "name": "Sebastián", "email": "sebastian@mail.com"},
  {"id": 14, "name": "Laura", "email": "laura@mail.com"},
  {"id": 15, "name": "Mateo", "email": "mateo@mail.com"},
  {"id": 16, "name": "Daniela", "email": "daniela@mail.com"},
  {"id": 17, "name": "Felipe", "email": "felipe@mail.com"},
  {"id": 18, "name": "Juliana", "email": "juliana@mail.com"},
  {"id": 19, "name": "Esteban", "email": "esteban@mail.com"},
  {"id": 20, "name": "Paula", "email": "paula@mail.com"}
]

# Ruta raíz para verificar que la API está funcionando
@app.route('/')
def home():
    return "API de usuarios funcionando"

# Obtener lista de usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Agregar un nuevo usuario
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or not "id" in new_user or not "name" in new_user or not "email" in new_user:
        return jsonify({"error": "Faltan campos en el usuario. Debe incluir id, name y email"}), 400
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
