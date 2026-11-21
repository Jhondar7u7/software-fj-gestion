# cliente.py
# Clase Cliente: guarda y valida los datos personales.

from entidad import Entidad
from excepciones import ClienteInvalidoError, ParametroFaltanteError
from logger_config import logger


class Cliente(Entidad):
    """Cliente de Software FJ."""

    def __init__(self, id_cliente, nombre, correo, telefono):
        super().__init__(id_cliente)
        # Al asignar se llaman los setters, que validan el dato
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        logger.info("Cliente creado: " + self._nombre)

    # ---------- Nombre ----------
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Si está vacío, falta el dato
        if valor is None or str(valor).strip() == "":
            raise ParametroFaltanteError("El nombre es obligatorio")
        # Mínimo 3 letras
        if len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre es muy corto")
        # Solo letras y espacios
        if not valor.replace(" ", "").isalpha():
            raise ClienteInvalidoError("El nombre solo puede tener letras")
        self._nombre = valor.strip()

    # ---------- Correo ----------
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ParametroFaltanteError("El correo es obligatorio")
        # Revisión simple: debe tener @ y un punto
        if "@" not in valor or "." not in valor:
            raise ClienteInvalidoError("El correo no es válido")
        self._correo = valor.strip()

    # ---------- Teléfono ----------
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ParametroFaltanteError("El teléfono es obligatorio")
        # Debe tener 10 números
        if not str(valor).isdigit() or len(str(valor)) != 10:
            raise ClienteInvalidoError("El teléfono debe tener 10 dígitos")
        self._telefono = str(valor)

    # ---------- Descripción ----------
    def describir(self):
        # Método obligatorio que viene de Entidad
        return ("Cliente " + str(self.id) + ": " + self._nombre
                + " | " + self._correo + " | " + self._telefono)