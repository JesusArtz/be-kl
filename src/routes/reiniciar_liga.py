from db import session
from flask import request, jsonify, make_response
from src.database.models import Partidos, Equipos, Arbitros, Canchas, Jugadores, Presidentes
import os

def reiniciar_liga():
    session.query(Partidos).delete()
    session.query(Jugadores).delete()
    session.query(Equipos).delete()
    session.query(Arbitros).delete()
    session.query(Canchas).delete()
    session.query(Presidentes).delete()
    session.commit()
    
    # Eliminar archivos de imagenes satatic/images
    images_path = os.path.join(os.getcwd(), "static/images")

    if os.path.exists(images_path):
        for file in os.listdir(images_path):
            os.remove(os.path.join(images_path, file))
    else:
        print(f"Path not found: {images_path}")


    return make_response(jsonify({"message":"Liga reiniciada!"}), 200)
