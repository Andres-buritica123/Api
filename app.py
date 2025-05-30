import os
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  # ... tus usuarios ...
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usar puerto dinámico o 5000 localmente
    app.run(host='0.0.0.0', port=port, debug=True)