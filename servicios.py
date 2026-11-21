# servicios.py
# Clase abstracta Servicio y tres servicios especializados.

from abc import abstractmethod
from entidad import Entidad
from excepciones import (ParametroFaltanteError, ReservaInvalidaError,
                         ServicioNoDisponibleError, CalculoInconsistenteError)
from logger_config import logger


class Servicio(Entidad):
    """Clase abstracta: base de todos los servicios."""

    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)
        # Validamos nombre y precio antes de guardar
        if nombre is None or str(nombre).strip() == "":
            raise ParametroFaltanteError("El nombre del servicio es obligatorio")
        if not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise CalculoInconsistenteError("El precio debe ser mayor a 0")
        self._nombre = nombre.strip()
        self._precio_base = precio_base
        self.disponible = True  # Por defecto el servicio está disponible
        logger.info("Servicio creado: " + self._nombre)

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    def verificar_disponible(self):
        # Lanza error si el servicio no se puede usar
        if not self.disponible:
            raise ServicioNoDisponibleError(
                "El servicio " + self._nombre + " no está disponible")

    def _validar_duracion(self, duracion, maximo, unidad):
        # Revisa que la duración sea un número entre 1 y el máximo
        if not isinstance(duracion, (int, float)) or duracion < 1 or duracion > maximo:
            raise ReservaInvalidaError(
                "La duración debe estar entre 1 y " + str(maximo) + " " + unidad)

    def _aplicar_extras(self, subtotal, descuento, impuesto):
        # Aplica descuento e impuesto (ambos en porcentaje)
        if descuento < 0 or descuento > 100:
            raise CalculoInconsistenteError("El descuento debe estar entre 0 y 100")
        if impuesto < 0:
            raise CalculoInconsistenteError("El impuesto no puede ser negativo")
        total = subtotal - subtotal * descuento / 100
        total = total + total * impuesto / 100
        return round(total, 2)

    @abstractmethod
    def validar_parametros(self, duracion):
        """Cada servicio revisa su duración de forma distinta."""
        pass

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Cada servicio calcula su costo de forma distinta."""
        pass


class ReservaSala(Servicio):
    """Sala que se cobra por hora."""

    def __init__(self, id_servicio, nombre, precio_hora, capacidad):
        super().__init__(id_servicio, nombre, precio_hora)
        self.capacidad = capacidad

    def validar_parametros(self, duracion):
        # Máximo 8 horas
        self._validar_duracion(duracion, 8, "horas")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        subtotal = self._precio_base * duracion
        return self._aplicar_extras(subtotal, descuento, impuesto)

    def describir(self):
        return ("Sala " + self._nombre + " | capacidad: " + str(self.capacidad)
                + " personas | $" + str(self._precio_base) + " por hora")


class AlquilerEquipo(Servicio):
    """Equipo que se cobra por día."""

    def __init__(self, id_servicio, nombre, precio_dia, tipo_equipo):
        super().__init__(id_servicio, nombre, precio_dia)
        self.tipo_equipo = tipo_equipo

    def validar_parametros(self, duracion):
        # Máximo 30 días
        self._validar_duracion(duracion, 30, "días")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        subtotal = self._precio_base * duracion
        return self._aplicar_extras(subtotal, descuento, impuesto)

    def describir(self):
        return ("Equipo " + self._nombre + " | tipo: " + str(self.tipo_equipo)
                + " | $" + str(self._precio_base) + " por día")


class Asesoria(Servicio):
    """Asesoría especializada: se cobra por hora con recargo."""

    def __init__(self, id_servicio, nombre, precio_hora, especialidad):
        super().__init__(id_servicio, nombre, precio_hora)
        self.especialidad = especialidad

    def validar_parametros(self, duracion):
        # Máximo 5 horas
        self._validar_duracion(duracion, 5, "horas")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        # Recargo del 25% por ser especializada
        subtotal = self._precio_base * duracion * 1.25
        return self._aplicar_extras(subtotal, descuento, impuesto)

    def describir(self):
        return ("Asesoría " + self._nombre + " | especialidad: "
                + str(self.especialidad) + " | $" + str(self._precio_base)
                + " por hora (+25%)")