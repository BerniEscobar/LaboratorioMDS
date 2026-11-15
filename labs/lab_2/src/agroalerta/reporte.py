def contar_riesgos(sensores, lecturas):
    conteo = {}

    for sensor in sensores:
        valores = lecturas.get(sensor.nombre, [])
        cantidad = 0

        for valor in valores:
            if sensor.es_riesgo(valor):
                cantidad += 1

        conteo[sensor.nombre] = cantidad

    return conteo
