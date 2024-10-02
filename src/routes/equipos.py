from db import session
from flask import request, jsonify, make_response
from src.database.models import Equipos
from src.methods.convert_image import processImage


def crear_equipo():
    data = request.get_json()
    equipo = Equipos(data["nombre"], 0, processImage(data["logo"]), data["cancha_id"])
    session.add(equipo)
    session.commit()
    return  make_response(jsonify({"message":"Team created!"}), 200)

def obtener_equipos():
    query = session.query(Equipos).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre, "puntos":x.puntos, "logo":x.logo, "cancha_id":x.cancha_id} for x in query}
    return make_response(jsonify(response), 200)

def obtener_equipo(id):
    query = session.query(Equipos).get(id)
    response = {"id":query.id, "nombre":query.nombre, "puntos":query.puntos, "logo":query.logo, "cancha_id":query.cancha_id}
    return make_response(jsonify(response), 200)

def eliminar_equipo():
    data = request.get_json
    session.query(Equipos).filter(Equipos.id == data["id"]).delete()
    session.query()
    return make_response(jsonify({"message":"Deleted!"}), 200)