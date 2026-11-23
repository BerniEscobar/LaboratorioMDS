"""Carga del modelo y verificación de compatibilidad del artefacto."""

from pathlib import Path
from typing import Any

import joblib
import sklearn
from sklearn.pipeline import Pipeline

from src.aguaapr.artifacts import (
    FEATURES,
    ErrorArtefacto,
    leer_metadata,
)


def cargar_modelo(directorio: Path) -> tuple[Pipeline, dict[str, Any]]:
    """Carga el modelo y su metadata, verificando su compatibilidad."""

    directorio = Path(directorio)

    # Comprobar que existan los archivos
    if not (directorio / "model.joblib").is_file():
        raise ErrorArtefacto("No existe el archivo model.joblib")

    if not (directorio / "metadata.json").is_file():
        raise ErrorArtefacto("No existe el archivo metadata.json")

    # Leer metadata
    metadata = leer_metadata(directorio)

    # Verificar que las variables coincidan y estén ordenadas
    if metadata["features"] != list(FEATURES):
        raise ErrorArtefacto(
            "Las variables del modelo no coinciden con FEATURES."
        )

    # Verificar la versión de scikit-learn
    if metadata["sklearn_version"] != sklearn.__version__:
        raise ErrorArtefacto(
            f"Versión de scikit-learn incompatible: "
            f"{metadata['sklearn_version']} != {sklearn.__version__}"
        )

    # Cargar el modelo
    modelo = joblib.load(directorio / "model.joblib")

    return modelo, metadata
