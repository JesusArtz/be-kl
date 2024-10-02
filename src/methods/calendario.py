def generar_calendario_circulos_concentricos(equipos):
  """Genera un calendario de enfrentamientos entre equipos utilizando el método de círculos concéntricos.

  Args:
    equipos: Una lista de nombres de equipos.

  Returns:
    Un diccionario donde las claves son las jornadas y los valores son listas de enfrentamientos (tupla de local y visitante).
  """

  # Verificar si hay un número par de equipos
  if len(equipos) % 2 != 0:
    equipos.append("Descanso")

  # Número total de jornadas
  num_jornadas = len(equipos) - 1

  # Crear un calendario vacío
  calendario = {}

  # Crear una matriz para representar los círculos concéntricos
  matriz = [[None] * len(equipos) for _ in range(num_jornadas)]

  # Inicializar la primera fila
  for i in range(len(equipos) // 2):
      matriz[0][i] = equipos[i]
      matriz[0][len(equipos) - 1 - i] = equipos[len(equipos) - 1 - i]

  # Llenar las demás filas
  for jornada in range(1, num_jornadas):
      for i in range(len(equipos)):
          matriz[jornada][i] = matriz[jornada - 1][(i + 1) % (len(equipos) - 1)]

  # Crear los enfrentamientos
  for jornada in range(num_jornadas):
      enfrentamientos = []
      for i in range(len(equipos) // 2):
          enfrentamientos.append((matriz[jornada][i], matriz[jornada][-i - 1]))
      calendario[f"Jornada {jornada + 1}"] = enfrentamientos

  return calendario

# Ejemplo de uso:
equipos = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4", "Equipo 5", "Equipo 6", "Equipo 7", "Equipo 8",  "Equipo 9", "Equipo 10"]
calendario = generar_calendario_circulos_concentricos(equipos)

# Imprimir el calendario
for jornada, enfrentamientos in calendario.items():
  print(jornada)
  for local, visitante in enfrentamientos:
    print(f"- {local} (Local) vs {visitante} (Visitante)")