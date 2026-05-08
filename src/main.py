#Importa la clase Client desde el módulo client
from src.models.client import Client
# Importa la clase RoomReservation
from src.models.room_reservation import RoomReservation
# Importa la clase Reservation
from src.models.reservation import Reservation
# Importa la función log_error para registrar errores
from src.utils.logger import log_error

from src.models.equipment_rental import EquipmentRental
from src.models.consulting_service import ConsultingService

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
    
    # Alquiler de equipamiento
    
    try:
        service2 = EquipmentRental("Laptop", 30)

        reservation2 = Reservation(client1, service2, 3)

        results.append(reservation2.process())

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")

    # Consultar servicios
    
    try:
        service3 = ConsultingService("Software Consulting", 100)

        reservation3 = Reservation(client1, service3, 2)

        results.append(reservation3.process())

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")

    # Cancelar reserva
    
    try:
        reservation4 = Reservation(client1, service1, 1)

        reservation4.cancel()

        results.append(f"Reservation status: {reservation4.status}")

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")   

    # Confirmar reserva manualmente
    
    try:
        reservation5 = Reservation(client1, service2, 1)

        reservation5.confirm()

        results.append(f"Reservation status: {reservation5.status}")

    except Exception as e:
        
        log_error(e)
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

    # Correo inválido
    
    try:
        bad_client2 = Client("Carlos", "invalid-email")

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")  

    # Duración inválida
    
    try:
        bad_reservation = Reservation(client1, service1, 0)

        results.append(bad_reservation.process())

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")
    
    # Horas en negativo
    
    try:
        bad_service = RoomReservation("Meeting Room", 40)

        results.append(bad_service.calculate_cost(-2))

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")

    # Duración de consulta inválida
    
    try:
        reservation10 = Reservation(client1, service3, -5)

        results.append(reservation10.process())

    except Exception as e:
        
        log_error(e)
        results.append(f"Error: {e}")



# Retorna todos los resultados obtenidos
    for r in results:
        print(r)

# Verifica si el archivo se ejecuta directamente
if __name__ == "__main__":
     # Ejecuta la simulación
    run_simulation()
