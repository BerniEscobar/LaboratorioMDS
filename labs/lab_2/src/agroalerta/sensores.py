from abc import ABC, abstractmethod

from src.agroalerta.errores import LecturaInvalidaError


class Sensor(ABC):
    """Representa un sensor con un nombre y una unidad de medida."""

    def __init__(self, nombre: str, unidad: str) -> None:
        self.nombre = nombre
        self.unidad = unidad

    @abstractmethod
    def es_riesgo(self, valor: float) -> bool:
        """Indica si una lectura representa riesgo."""
        pass

    @abstractmethod
    def validar(self, valor: float) -> None:
        """Valida que una lectura sea físicamente posible."""
        pass

    @property
    @abstractmethod
    def rango_seguro(self) -> str:
        """Describe el rango considerado seguro."""
        pass


class SensorTemperatura(Sensor):
    def __init__(self, minimo: float, maximo: float) -> None:
        super().__init__("temperatura", "°C")
        self._minimo = minimo
        self._maximo = maximo

    def es_riesgo(self, valor: float) -> bool:
        return valor < self._minimo or valor > self._maximo

    def validar(self, valor: float) -> None:
        if valor < -50 or valor > 60:
            raise LecturaInvalidaError(
                f"Temperatura físicamente imposible: {valor} °C"
            )

    @property
    def rango_seguro(self) -> str:
        return f"entre {self._minimo} y {self._maximo} {self.unidad}"


class SensorViento(Sensor):
    def __init__(self, maximo: float) -> None:
        super().__init__("viento", "km/h")
        self._maximo = maximo

    def es_riesgo(self, valor: float) -> bool:
        return valor > self._maximo

    def validar(self, valor: float) -> None:
        if valor < 0 or valor > 200:
            raise LecturaInvalidaError(
                f"Viento físicamente imposible: {valor} km/h"
            )

    @property
    def rango_seguro(self) -> str:
        return f"bajo {self._maximo} {self.unidad}"


class SensorHumedad(Sensor):
    def __init__(self, maximo: float) -> None:
        super().__init__("humedad", "%")
        self._maximo = maximo

    def es_riesgo(self, valor: float) -> bool:
        return valor > self._maximo

    def validar(self, valor: float) -> None:
        if valor < 0 or valor > 100:
            raise LecturaInvalidaError(
                f"Humedad físicamente imposible: {valor} %"
            )

    @property
    def rango_seguro(self) -> str:
        return f"bajo {self._maximo} {self.unidad}"
