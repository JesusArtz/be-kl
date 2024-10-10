from db import session
from flask import request, jsonify, make_response
from src.database.models import Jugadores
from src.methods.convert_image import processImage
import os

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

def actualizar_nocontrol():
    data = request.get_json()
    session.query(Jugadores).filter(Jugadores.id == data["id"]).update({"nocontrol":data["nuevo_nocontrol"]})
    session.commit()
    query = session.query(Jugadores).get(data["id"])
    res = {"id":query.id, "nombre":query.nombre, "id_equipo":query.equipo_id, "nocontrol":query.nocontrol, "foto":query.foto}
    return make_response(jsonify(res), 200)

def actualizar_foto():
    data = request.get_json()
    antigua_foto = session.query(Jugadores).get(data["id"]).foto
    session.query(Jugadores).filter(Jugadores.id == data["id"]).update({"foto":processImage(data["nueva_foto"])})
    session.commit()
    os.remove(f"{antigua_foto}") 
    query = session.query(Jugadores).get(data["id"])
    res = {"id":query.id, "nombre":query.nombre, "id_equipo":query.equipo_id, "nocontrol":query.nocontrol, "foto":query.foto}
    return make_response(jsonify(res), 200)

def actualizar_foto_equipo():
    data = request.get_json()
    jugadores = session.query(Jugadores).filter(Jugadores.equipo_id == data["equipo_id"]).all()
    nueva_foto = processImage(data["nueva_foto"])
    for jugador in jugadores:
        antigua_foto = jugador.foto
        session.query(Jugadores).filter(Jugadores.id == jugador.id).update({"foto":nueva_foto})
    session.commit()
    return make_response(jsonify({"message":"Updated!"}), 200)