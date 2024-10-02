from db import Base

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, Time

class Canchas(Base):

    __tablename__ = "canchas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

class Equipos(Base):

    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    puntos = Column(Integer, nullable=False)
    logo = Column(String, nullable=False)
    cancha_id = Column(Integer, ForeignKey(Canchas.id))

    def __init__(self, nombre, puntos, logo, cancha_id):
        self.nombre = nombre
        self.puntos = puntos
        self.logo = logo
        self.cancha_id = cancha_id

class Presidentes(Base):

    __tablename__ = "presidentes"

    id = Column(Integer, primary_key=True)
    equipo_id = Column(Integer, ForeignKey(Equipos.id))

    def __init__(self, equipo_id):
        self.equipo_id = equipo_id

class Jugadores(Base):

    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    equipo_id = Column(Integer, ForeignKey(Equipos.id))
    posicion = Column(String, nullable=False)
    dorsal = Column(Integer, nullable=False)
    foto = Column(String, nullable=False)

    def __init__(self, nombre, equipo_id, posicion, dorsal, foto):
        self.nombre = nombre
        self.equipo_id = equipo_id
        self.posicion = posicion
        self.dorsal = dorsal
        self.foto = foto

class Arbitros(Base):

    __tablename__ = "arbitros"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    foto = Column(String)

    def __init__(self, nombre, foto):
        self.nombre = nombre
        self.foto = foto

class Partidos(Base):

    __tablename__ = "partidos"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    id_equipo_local = Column(Integer, ForeignKey(Equipos.id))
    id_equipo_visitante = Column(Integer, ForeignKey(Equipos.id))
    jornada = Column(Integer, nullable=False)
    jugado = Column(Boolean, nullable=False)
    cancha_id = Column(Integer, ForeignKey(Canchas.id))
    arbitro = Column(Integer, ForeignKey(Arbitros.id ))

    def __init__(self, fecha, hora, id_equipo_local, id_equipo_visitante, jornada, jugado, cancha_id, arbitro):
        self.fecha = fecha
        self.hora = hora
        self.id_equipo_local = id_equipo_local
        self.id_equipo_visitante = id_equipo_visitante
        self.jornada = jornada
        self.jugado = jugado
        self.cancha_id = cancha_id
        self.arbitro = arbitro

class Usuarios(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    usuario = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)

    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena