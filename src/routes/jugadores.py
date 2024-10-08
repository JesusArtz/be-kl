from db import session
from flask import request, jsonify, make_response
from src.database.models import Jugadores
from src.methods.convert_image import processImage

def crear_jugador():
    data = request.get_json()
    jugador = Jugadores(data["nombre"], data["equipo_id"], data["nocontrol"], processImage(data["foto"]))
    session.add(jugador)
    session.commit()
    return make_response(jsonify({"message":"Created!"}), 200)

def jugadores_equipo(equipo_id):
    query = session.query(Jugadores).filter(Jugadores.equipo_id == equipo_id).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre, "id_equipo":x.equipo_id, "nocontrol":x.nocontrol, "foto":x.foto} for x in query}
    return make_response(jsonify(response), 200)

def obtener_jugadores():
    query = session.query(Jugadores).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre, "id_equipo":x.equipo_id, "nocontrol":x.nocontrol, "foto":x.foto} for x in query}
    return make_response(jsonify(response), 200)

def obtener_jugador(id):
    query = session.query(Jugadores).get(id)
    response = {"id":query.id, "nombre":query.nombre, "id_equipo":query.equipo_id, "nocontrol":query.nocontrol, "foto":query.foto}
    return make_response(jsonify(response), 200)

def borrar_jugador():
    data = request.get_json()
    session.query(Jugadores).filter(Jugadores.id == data["id"]).delete()
    session.commit()
    return make_response(jsonify({"message":"Deleted!"}))
