# main.py
# Simulación de 14 operaciones del sistema Software FJ.

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import ErrorSoftwareFJ
from logger_config import logger

# Listas donde se guardan los objetos (no usamos base de datos)
clientes = []
servicios = []
reservas = []


def mostrar(numero, titulo):
    # Muestra en pantalla y guarda en el log el título de la operación
    print("\nOperación " + str(numero) + ": " + titulo)
    logger.info("Operación " + str(numero) + ": " + titulo)


def registrar_error(numero, error):
    # Muestra el error y lo guarda en el log
    print("   ERROR:", error)
    logger.error("Operación " + str(numero) + " falló: " + str(error))


logger.info("===== INICIO DE LA SIMULACIÓN =====")

# ---------- CLIENTES ----------

# Operación 1: cliente válido
mostrar(1, "Registrar cliente válido")
try:
    ana = Cliente(1, "Ana Torres", "ana@correo.com", "3001234567")
    clientes.append(ana)
    print("   OK:", ana.describir())
except ErrorSoftwareFJ as e:
    registrar_error(1, e)

# Operación 2: cliente con correo inválido
mostrar(2, "Registrar cliente con correo inválido")
try:
    luis = Cliente(2, "Luis Gómez", "correo-malo", "3001234567")
    clientes.append(luis)
    print("   OK:", luis.describir())
except ErrorSoftwareFJ as e:
    registrar_error(2, e)

# Operación 3: cliente con nombre vacío
mostrar(3, "Registrar cliente con nombre vacío")
try:
    sin_nombre = Cliente(3, "", "a@b.com", "3001234567")
    clientes.append(sin_nombre)
    print("   OK:", sin_nombre.describir())
except ErrorSoftwareFJ as e:
    registrar_error(3, e)

# Operación 4: otro cliente válido
mostrar(4, "Registrar otro cliente válido")
try:
    carlos = Cliente(4, "Carlos Pérez", "carlos@correo.com", "3109876543")
    clientes.append(carlos)
    print("   OK:", carlos.describir())
except ErrorSoftwareFJ as e:
    registrar_error(4, e)

# ---------- SERVICIOS ----------

# Operación 5: sala válida
mostrar(5, "Crear sala válida")
try:
    sala = ReservaSala(1, "Sala Norte", 10000, 12)
    servicios.append(sala)
    print("   OK:", sala.describir())
except ErrorSoftwareFJ as e:
    registrar_error(5, e)

# Operación 6: equipo válido
mostrar(6, "Crear alquiler de equipo válido")
try:
    equipo = AlquilerEquipo(2, "Proyector", 20000, "Video")
    servicios.append(equipo)
    print("   OK:", equipo.describir())
except ErrorSoftwareFJ as e:
    registrar_error(6, e)

# Operación 7: asesoría válida
mostrar(7, "Crear asesoría válida")
try:
    asesoria = Asesoria(3, "Asesoría Python", 50000, "Programación")
    servicios.append(asesoria)
    print("   OK:", asesoria.describir())
except ErrorSoftwareFJ as e:
    registrar_error(7, e)

# Operación 8: sala con precio negativo
mostrar(8, "Crear sala con precio negativo")
try:
    sala_mala = ReservaSala(4, "Sala Sur", -5000, 8)
    servicios.append(sala_mala)
    print("   OK:", sala_mala.describir())
except ErrorSoftwareFJ as e:
    registrar_error(8, e)

# ---------- RESERVAS ----------

# Operación 9: reserva exitosa (10% de descuento y 19% de impuesto)
mostrar(9, "Reserva exitosa de sala por 3 horas")
try:
    reserva1 = Reserva(1, ana, sala, 3)
    reservas.append(reserva1)
    reserva1.confirmar(10, 19)
    print("   OK:", reserva1.describir())
except ErrorSoftwareFJ as e:
    registrar_error(9, e)

# Operación 10: reserva con duración inválida
mostrar(10, "Reserva de equipo por 45 días (inválida)")
try:
    reserva2 = Reserva(2, carlos, equipo, 45)
    reservas.append(reserva2)
    print("   OK:", reserva2.describir())
except ErrorSoftwareFJ as e:
    registrar_error(10, e)

# Operación 11: reserva con cliente inválido
mostrar(11, "Reserva con cliente inválido")
try:
    reserva3 = Reserva(3, "texto", sala, 2)
    reservas.append(reserva3)
    print("   OK:", reserva3.describir())
except ErrorSoftwareFJ as e:
    registrar_error(11, e)

# Operación 12: reserva con servicio no disponible
mostrar(12, "Reserva de un servicio no disponible")
try:
    asesoria.disponible = False
    reserva4 = Reserva(4, carlos, asesoria, 2)
    reservas.append(reserva4)
    resultado = reserva4.procesar()
    if resultado:
        print("   OK:", reserva4.describir())
    else:
        print("   La reserva no se pudo procesar (servicio no disponible)")
except ErrorSoftwareFJ as e:
    registrar_error(12, e)
finally:
    # Dejamos el servicio disponible otra vez
    asesoria.disponible = True

# Operación 13: confirmar una reserva ya confirmada
mostrar(13, "Confirmar una reserva que ya está confirmada")
try:
    reserva1.confirmar()
    print("   OK")
except ErrorSoftwareFJ as e:
    registrar_error(13, e)

# Operación 14: cancelar la misma reserva dos veces
mostrar(14, "Cancelar una reserva dos veces")
try:
    reserva1.cancelar()
    print("   OK: primera cancelación")
    reserva1.cancelar()
    print("   OK: segunda cancelación")
except ErrorSoftwareFJ as e:
    registrar_error(14, e)

# ---------- RESUMEN ----------
print("\n===== RESUMEN FINAL =====")
print("Clientes registrados:", len(clientes))
print("Servicios creados:", len(servicios))
print("Reservas creadas:", len(reservas))
for r in reservas:
    print(" -", r.describir())

logger.info("===== FIN DE LA SIMULACIÓN =====")
print("\nEl programa terminó sin caerse. Revisa logs/eventos.log")