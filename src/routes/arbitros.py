from db import session
from flask import request, jsonify, make_response
from src.database.models import Arbitros
from src.methods.convert_image import processImage

def crear_arbitro():
    data = request.get_json()
    arbitro = Arbitros(data["nombre"], processImage(data["foto"]))
    session.add(arbitro)
    session.commit()
    return make_response(jsonify({"message":"Created!"}), 200)

def obtener_arbitros():
    query = session.query(Arbitros).all()
    response = {f"{x.id}":{"id":x.id, "nombre":x.nombre, "foto":x.foto} for x in query}
    return make_response(jsonify(response), 200)

def obtener_arbitro(id):
    query = session.query(Arbitros).get(id)
    response = {"id":query.id, "nombre":query.nombre, "foto":query.foto}
    return make_response(jsonify(response), 200)

def borrar_arbitro():
    data = request.get_json()
    session.query(Arbitros).filter(Arbitros.id == data["id"]).delete()
    session.commit()
    return make_response(jsonify({"message":"Deleted!"}), 200)