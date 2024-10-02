from db import session
from flask import request, jsonify, make_response
from src.database.models import Presidentes
from src.methods.convert_image import processImage

def crear_presidente():
    data = request.get_json()
    presidente = Presidentes(data["nombre"], processImage(data["foto"]))
    session.add(presidente)
    session.commit()
    return make_response(jsonify({"message":"Created!"}), 200)

def obtener_presidentes():
    query = session.query(Presidentes).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre, "foto":x.foto} for x in query}
    return make_response(jsonify(response), 200)

def obtener_presidente(id):
    query = session.query(Presidentes).get(id)
    response = {"id":query.id, "nombre":query.nombre, "foto":query.foto}
    return make_response(jsonify(response), 200)

def borrar_presidente():
    data = request.get_json()
    session.query(Presidentes).filter(Presidentes.id == data["id"]).delete()
    session.commit()
    return make_response(jsonify({"message":"Deleted!"}), 200)