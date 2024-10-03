from db import session
from flask import request, jsonify, make_response
from src.database.models import Usuarios
from flask_jwt_extended import create_access_token
import bcrypt

# Crea un sistema de registro de usuarios y login usando jwt y encryptando la contraseña usando bcrypt

def registrar():
    if request.method == 'POST':
        data = request.get_json()
        if data["usuario"] and data["contrasena"]:
            usuario = Usuarios(usuario=data["usuario"], contrasena=bcrypt.hashpw(data["contrasena"].encode('utf-8'), bcrypt.gensalt()))
            session.add(usuario)
            session.commit()
            return jsonify({"mensaje": "Usuario registrado exitosamente"})
        else:
            return jsonify({"mensaje": "Faltan datos"})
        
def login():
    if request.method == 'POST':
        data = request.get_json()
        if data["usuario"] and data["contrasena"]:
            usuario = session.query(Usuarios).filter(Usuarios.usuario == data["usuario"]).first()
            if usuario:
                if bcrypt.checkpw(data["contrasena"].encode('utf-8'), usuario.contrasena):
                    token = create_access_token(identity=usuario.usuario)
                    return jsonify({"mensaje": "Login exitoso", "token": token})
                else:
                    return jsonify({"mensaje": "Contraseña incorrecta"})
            else:
                return jsonify({"mensaje": "Usuario no encontrado"})
        else:
            return jsonify({"mensaje": "Faltan datos"})