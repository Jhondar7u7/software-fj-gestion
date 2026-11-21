# entidad.py
# Clase abstracta base: representa cualquier "cosa" del sistema.

from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase base abstracta. No se puede crear directamente."""

    def __init__(self, id_entidad):
        # Todas las entidades tienen un identificador
        self._id = id_entidad

    @property
    def id(self):
        # Permite leer el id, pero no cambiarlo desde afuera
        return self._id

    @abstractmethod
    def describir(self):
        """Cada clase hija debe explicar cómo se describe."""
        pass