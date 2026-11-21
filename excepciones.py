# excepciones.py
# Aquí definimos los errores propios del sistema Software FJ.


class ErrorSoftwareFJ(Exception):
    """Error base: todos los demás errores heredan de este."""
    pass


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se lanza cuando los datos del cliente son inválidos."""
    pass


class ParametroFaltanteError(ErrorSoftwareFJ):
    """Se lanza cuando falta un dato obligatorio."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se lanza cuando el servicio no se puede usar."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se lanza cuando una reserva tiene datos incorrectos."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se lanza cuando se intenta una acción que no está permitida."""
    pass


class CalculoInconsistenteError(ErrorSoftwareFJ):
    """Se lanza cuando un cálculo da un resultado que no tiene sentido."""
    pass