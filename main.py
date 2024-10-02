from db import *
from src.database.models import Equipos, Jugadores, Arbitros, Canchas, Presidentes, Usuarios, Partidos
from __init__ import app
from src import ROOT

for route in ROOT:
    app.add_url_rule(route['path'], view_func=route['function'], methods=[route['method']])


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, host="0.0.0.0")