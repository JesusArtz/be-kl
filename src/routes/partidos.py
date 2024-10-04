import random
from db import session
from flask import request, jsonify, make_response
from src.database.models import Partidos, Equipos, Arbitros, Canchas
from src.methods.convert_image import processImage
from datetime import datetime
from src.methods.calendario import generar_calendario, verificar_enfrentamientos


def crear_calendario():
    # Eliminar todos los partidos
    session.query(Partidos).delete()
    session.commit()
    # Obtener todos los equipos
    equipos = session.query(Equipos).all()
    # Obtener los ids de los equipos para generar el calendario
    equipos = [x.id for x in equipos]
    calendario = generar_calendario(equipos)
    if not verificar_enfrentamientos(calendario):
        return make_response(jsonify({"message":"Error"}), 400)
    # Formato de generar_calendario: [[(equipo_local, equipo_visitante), ...], ...]
    # Partido(fecha, hora, equipo_local, equipo_visitante, jornda, jugado: boolean, cancha_id, arbitro_id)
    arbitros = session.query(Arbitros).all()
    # Hacer que cada arbitro arbitre un partido al menos
    for jornada, partidos in enumerate(calendario):
        for partido in partidos:
            fecha = datetime.now().date() 
            hora = datetime.now().time()  
            equipo_local, equipo_visitante = partido
            nuevo_partido = Partidos(fecha=fecha, hora=hora, id_equipo_local=equipo_local, id_equipo_visitante=equipo_visitante, jornada=jornada+1, jugado=False, cancha_id=1, arbitro=random.choice(arbitros).id)
            session.add(nuevo_partido)
            session.commit()
    return make_response(jsonify({"message":"Created!"}), 200)


def obtener_partidos():
    query = session.query(Partidos).all()
    equipo = session.query(Equipos).all()
    # {f"{x.id}":{"id":x.id, "fecha":x.fecha, "hora":x.hora, "equipo_local":nombre, "equipo_visitante":nombre, "jornada":x.jornada, "jugado":x.jugado, "cancha_id":x.cancha_id, "arbitro_id":x.arbitro_id} for x in query}
    response = {f"{x.id}":{"id":x.id, "fecha":f"{x.fecha}", "hora":f"{x.hora}", "equipo_local":session.query(Equipos).get(x.id_equipo_local).nombre, "equipo_visitante":session.query(Equipos).get(x.id_equipo_visitante).nombre, "jornada":x.jornada, "jugado":x.jugado, "cancha_id":x.cancha_id, "arbitro_id":x.arbitro} for x in query}
    print(response)
    return make_response(jsonify(response), 200)

def editar_partido():
    data = request.get_json()
    partido = session.query(Partidos).get(data["id"])
    # Editar la fecha, hora, cancha y arbitro de un partido en específico
    partido.fecha = data["fecha"]
    partido.hora = data["hora"]
    partido.cancha_id = data["cancha_id"]
    partido.arbitro_id = data["arbitro_id"]
    session.commit()
    return make_response(jsonify({"message":"Updated!"}), 200)

def partido_jugado():
    data = request.get_json()
    partido = session.query(Partidos).get(data["id"])
    partido.jugado = True
    session.commit()
    return make_response(jsonify({"message":"Updated!"}), 200)

def obtener_jornada(jornada):
    query = session.query(Partidos).filter(Partidos.jornada == jornada).all()
    response = {f"{x.id}":{"id":x.id, "fecha":f"{x.fecha}", "hora":f"{x.hora}", "equipo_local":session.query(Equipos).get(x.id_equipo_local).nombre, "equipo_visitante":session.query(Equipos).get(x.id_equipo_visitante).nombre, "jornada":x.jornada, "jugado":x.jugado, "cancha_id":x.cancha_id, "arbitro_id":x.arbitro} for x in query}
    return make_response(jsonify(response), 200)