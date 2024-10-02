from src.routes.cancha import *
from src.routes.equipos import *
from src.routes.jugadores import *

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
]