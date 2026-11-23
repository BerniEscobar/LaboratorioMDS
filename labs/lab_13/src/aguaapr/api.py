"""Rutas de inferencia: información del modelo, vida y predicción."""

from fastapi import APIRouter, Depends

from src.aguaapr.artifacts import a_tabla, predecir
from src.aguaapr.constants import RANGOS
from src.aguaapr.contracts import RespuestaPrediccion, Servicios
from src.aguaapr.deps import crear_dependencia_clave
from src.aguaapr.validation import MedicionAgua


def crear_router_inferencia(servicios: Servicios) -> APIRouter:
    """Construye el router con las tres rutas de inferencia."""

    router = APIRouter()

    # Ruta 1: información del modelo
    @router.get("/")
    def informacion_modelo():
        return {
            "metricas_validacion": servicios.metadata["metricas_validacion"],
            "entrada": {
                nombre: {"min": minimo, "max": maximo}
                for nombre, (minimo, maximo) in RANGOS.items()
            },
            "salida": {
                "prediccion": "0 = No potable, 1 = Potable",
                "probabilidad": "Probabilidad de ser potable",
            },
        }

    # Ruta 2: comprobar que el servicio está funcionando
    @router.get("/health")
    def health():
        return {"estado": "ok"}

    # Ruta 3: realizar una predicción
    @router.post(
        "/predict",
        response_model=RespuestaPrediccion,
        dependencies=[Depends(crear_dependencia_clave(servicios))],
    )
    def predict(medicion: MedicionAgua):
        tabla = a_tabla([medicion])

        clases, probabilidades = predecir(servicios.modelo, tabla)

        return RespuestaPrediccion(
            prediccion=int(clases[0]),
            probabilidad=round(float(probabilidades[0]), 4),
        )

    return router


# Prueba de cache de Docker
