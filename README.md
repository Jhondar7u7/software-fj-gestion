# Software FJ - Sistema de Gestión de Clientes, Servicios y Reservas

Proyecto del curso Programación (213023), UNAD. Sistema orientado a objetos en Python, sin base de datos, con manejo de excepciones y registro de errores en un archivo de logs.

## Estructura

| Archivo | Qué contiene |
|---|---|
| `excepciones.py` | Excepciones personalizadas |
| `logger_config.py` | Configuración del archivo de logs |
| `entidad.py` | Clase abstracta base `Entidad` |
| `cliente.py` | Clase `Cliente` con validaciones |
| `servicios.py` | Clase abstracta `Servicio` y 3 servicios (sala, equipo, asesoría) |
| `reserva.py` | Clase `Reserva` (confirmar, cancelar, procesar) |
| `main.py` | Simulación de 14 operaciones |
| `logs/eventos.log` | Registro de eventos y errores |

## Conceptos aplicados

- Abstracción: clases abstractas `Entidad` y `Servicio`.
- Herencia y polimorfismo: tres servicios con su propio cálculo de costo.
- Encapsulación: atributos privados con propiedades y validaciones.
- Sobrecarga: `calcular_costo` con descuento e impuesto opcionales.
- Excepciones: personalizadas, `try/except/else/finally` y encadenamiento con `raise ... from`.

## Cómo ejecutarlo

```
py main.py
```

## Autor

Jhonatan David Rodríguez Alfonso