from db import session
from flask import request, jsonify, make_response
from src.database.models import Canchas


def crear_cancha():
    data = request.get_json()
    cancha = Canchas(data["nombre"])
    session.add(cancha)
    session.commit()
    return make_response(jsonify({"message":"Created!"}), 200)

def obtener_canchas():
    query = session.query(Canchas).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre} for x in query}
    return make_response(jsonify(response),200)

def obtener_cancha(id):
    query = session.query(Canchas).get(id)
    response = {f"{query.id}":{"id":query.id,"nombre":query.nombre}}
    return make_response(jsonify(response), 200)

def eliminar_cancha():
    data = request.get_json()
    session.query(Canchas).filter(Canchas.id == data["id"]).delete()
    session.commit()
    return make_response(jsonify({"message":"Deleted!"}), 200)