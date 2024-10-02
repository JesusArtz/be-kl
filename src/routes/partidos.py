import random
from db import session
from flask import request, jsonify, make_response
from src.database.models import Partidos, Equipos, Arbitros, Canchas
from src.methods.convert_image import processImage

