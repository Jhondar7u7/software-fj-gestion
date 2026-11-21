# reserva.py
# Clase Reserva: une cliente, servicio, duración y estado.

from entidad import Entidad
from cliente import Cliente
from servicios import Servicio
from excepciones import (ErrorSoftwareFJ, ReservaInvalidaError,
                         OperacionNoPermitidaError)
from logger_config import logger


class Reserva(Entidad):
    """Reserva de un servicio hecha por un cliente."""

    def __init__(self, id_reserva, cliente, servicio, duracion):
        super().__init__(id_reserva)
        # Revisamos que cliente y servicio sean del tipo correcto
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("El cliente no es válido")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("El servicio no es válido")
        # El servicio revisa si la duración es correcta
        servicio.validar_parametros(duracion)
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "pendiente"  # Toda reserva empieza pendiente
        self._costo = 0
        logger.info("Reserva " + str(self.id) + " creada")

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    def confirmar(self, descuento=0, impuesto=0):
        # Solo se confirma una reserva pendiente
        if self._estado != "pendiente":
            raise OperacionNoPermitidaError(
                "Solo se puede confirmar una reserva pendiente")
        try:
            # Intentamos usar el servicio y calcular el costo
            self._servicio.verificar_disponible()
            costo = self._servicio.calcular_costo(
                self._duracion, descuento, impuesto)
        except ErrorSoftwareFJ as error:
            # Guardamos el error y lanzamos uno nuevo "desde" el original
            logger.error("Falla al confirmar reserva " + str(self.id)
                         + ": " + str(error))
            raise ReservaInvalidaError(
                "No se pudo confirmar: " + str(error)) from error
        else:
            # Esto solo se ejecuta si NO hubo error
            self._costo = costo
            self._estado = "confirmada"
            logger.info("Reserva " + str(self.id)
                        + " confirmada. Costo: " + str(costo))
        finally:
            # Esto se ejecuta siempre, haya error o no
            logger.info("Fin del intento de confirmar reserva " + str(self.id))

    def cancelar(self):
        # No se puede cancelar dos veces
        if self._estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya está cancelada")
        self._estado = "cancelada"
        logger.info("Reserva " + str(self.id) + " cancelada")

    def procesar(self, descuento=0, impuesto=0):
        # Intenta confirmar sin detener el programa si falla
        try:
            self.confirmar(descuento, impuesto)
        except ErrorSoftwareFJ as error:
            logger.error("Reserva " + str(self.id)
                         + " no procesada: " + str(error))
            return False
        else:
            return True

    def describir(self):
        return ("Reserva " + str(self.id) + " | " + self._cliente.nombre
                + " | " + self._servicio.nombre
                + " | duración: " + str(self._duracion)
                + " | estado: " + self._estado
                + " | costo: $" + str(self._costo))