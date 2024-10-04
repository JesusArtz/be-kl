from db import session
from flask import request, jsonify, render_template
from src.database.models import Jugadores, Equipos

def generar_credenciales():
    query = session.query(Jugadores).all()
    # send jugadores in format [[id, nombre, nombre_equipo, posicion, dorsal, foto], ...]
    # foto format is /static/images/str.png only send str.png without route9
    jugadores = [[x.id, x.nombre, session.query(Equipos).get(x.equipo_id).nombre, x.posicion, x.dorsal, str(x.foto).replace('/static/','')] for x in query]
    print(jugadores)
    return render_template("credenciales.html", jugadores=jugadores)
