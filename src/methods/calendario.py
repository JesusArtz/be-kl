
def generar_calendario(equipos):
    n = len(equipos)
    if n % 2 != 0:
        equipos.append("Descansa")  # Si el número de equipos es impar, agregamos un "Descansa"
        n += 1

    jornadas = []
    
    # Rueda de enfrentamientos para generar todas las combinaciones
    for j in range(n - 1):
        jornada = []
        for i in range(n // 2):
            equipo_local = equipos[i]
            equipo_visitante = equipos[n - 1 - i]
            jornada.append((equipo_local, equipo_visitante))
        
        jornadas.append(jornada)
        
        # Rotar la lista de equipos excepto el primero
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]
    
    return jornadas



def verificar_enfrentamientos(calendario):
    enfrentamientos = []
    for jornada in calendario:
        for enfrentamiento in jornada:
            enfrentamiento = tuple(sorted(enfrentamiento))
            if enfrentamiento in enfrentamientos:
                return False
            enfrentamientos.append(enfrentamiento)
    return True