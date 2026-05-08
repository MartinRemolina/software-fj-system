#Importa la clase Client desde el módulo client
from src.models.client import Client
# Importa la clase RoomReservation
from src.models.room_reservation import RoomReservation
# Importa la clase Reservation
from src.models.reservation import Reservation
# Importa la función log_error para registrar errores
from src.utils.logger import log_error

# Función principal que ejecuta la simulación
def run_simulation():

    # Lista donde se guardarán los resultados del programa
    results = []
# Bloque para manejar posibles errores
    try:
        # Crea un cliente con nombre y correo
        client1 = Client("Martin", "martin@email.com") 
# Crea un servicio de reserva de sala
        service1 = RoomReservation("Conference Room", 50)
 # Crea una reserva con cliente, servicio y duración
        reservation1 = Reservation(client1, service1, 2) 
        # Procesa la reserva y guarda el resultado
        results.append(reservation1.process())
# Captura cualquier excepción que ocurra
    except Exception as e:
        # Guarda el error en el sistema de logs
        log_error(e) 
        # Agrega el mensaje de error a la lista de resultados
        results.append(f"Error: {e}")

    # Caso inválido para probar errores
    try:
     # Cliente con datos inválidos
        client2 = Client("", "bademail")  # ERROR
        # Captura errores del caso inválido
    except Exception as e:
        # Registra el error
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")
# Retorna todos los resultados obtenidos
    for r in results:
        print(r)

# Verifica si el archivo se ejecuta directamente
if __name__ == "__main__":
     # Ejecuta la simulación
    run_simulation()
