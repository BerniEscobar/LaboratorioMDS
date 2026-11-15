import argparse
from pathlib import Path

from src.agroalerta.datos import cargar_lecturas
from src.agroalerta.reporte import contar_riesgos
from src.agroalerta.sensores import (
    SensorHumedad,
    SensorTemperatura,
    SensorViento,
)


def main():
    parser = argparse.ArgumentParser(description="AgroAlerta")
    parser.add_argument("--fecha", default="2026-06-15")
    args = parser.parse_args()

    sensores = [
        SensorTemperatura(0, 40),
        SensorViento(25),
        SensorHumedad(85),
    ]

    lecturas = cargar_lecturas(Path("data/lecturas.csv"), args.fecha)

    conteo, descartadas = contar_riesgos(sensores, lecturas)

    print(f"Estación Parcela Norte — {args.fecha}")

    for sensor in sensores:
        cantidad = conteo[sensor.nombre]
        print(f"{sensor.nombre.capitalize()}: {cantidad} lecturas en riesgo")

    total = sum(conteo.values())

    print()
    print(f"Descartadas: {descartadas} lecturas inválidas")
    print(f"Total: {total} situaciones de riesgo")


if __name__ == "__main__":
    main()
