from src.routes.cancha import *
from src.routes.equipos import *
from src.routes.jugadores import *
from src.routes.arbitros import *
from src.routes.presidentes import *

ROOT = [
    {
        'path': '/crear_cancha',
        'method': 'POST',
        'function': crear_cancha
    },
    {
        'path':'/obtener_canchas',
        'method':'GET',
        'function':obtener_canchas
    },
    {
        'path':'/obtener_cancha/<id>',
        'method':'GET',
        'function':obtener_cancha
    },
    {
        'path':'/eliminar_cancha',
        'method':'DELETE',
        'function':eliminar_cancha
    }, 
    # EQUIPOS
    {
        'path':'/crear_equipo',
        'method':'POST',
        'function':crear_equipo
    },
    {
        'path':'/obtener_equipos',
        'method':'GET',
        'function':obtener_equipos
    },
    {
        'path':'/obtener_equipo/<id>',
        'method':'GET',
        'function':obtener_equipo
    },
    # JUGADORES
    {
        'path':'/crear_jugador',
        'method':'POST',
        'function':crear_jugador
    },
    {
        'path':'/jugador_equipo/<equipo_id>',
        'method':'GET',
        'function':jugadores_equipo
    },
    {
        'path':'/obtener_jugadores',
        'method':'GET',
        'function':obtener_jugadores
    },
    {
        'path':'/obtener_jugador/<id>',
        'method':'GET',
        'function':obtener_jugador
    },
    {
        'path':'/borrar_jugador',
        'method':'DELETE',
        'function':borrar_jugador
    },
    {
        'path':'/actualizar_dorsal',
        'method':'PUT',
        'function':actualizar_dorsal
    },
    # ARBITROS
    {
        'path':'/crear_arbitro',
        'method':'POST',
        'function':crear_arbitro
    },
    {
        'path':'/obtener_arbitros',
        'method':'GET',
        'function':obtener_arbitros
    },
    {
        'path':'/obtener_arbitro/<id>',
        'method':'GET',
        'function':obtener_arbitro
    },
    {
        'path':'/borrar_arbitro',
        'method':'DELETE',
        'function':borrar_arbitro
    },
    # PRESIDENTES
    {
        'path':'/crear_presidente',
        'method':'POST',
        'function':crear_presidente
    },
    {
        'path':'/obtener_presidentes',
        'method':'GET',
        'function':obtener_presidentes
    },
    {
        'path':'/obtener_presidente/<id>',
        'method':'GET',
        'function':obtener_presidente
    },
    {
        'path':'/borrar_presidente',
        'method':'DELETE',
        'function':borrar_presidente
    }
]