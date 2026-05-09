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
    # Bloque try para manejar posibles errores en el alquiler de equipos
    try:
        # Crea un servicio de alquiler de equipos llamado "Laptop" con costo de 30
        service2 = EquipmentRental("Laptop", 30)
# Crea una reserva para el cliente usando el servicio por 3 horas/días
        reservation2 = Reservation(client1, service2, 3)
# Procesa la reserva y guarda el resultado en la lista
        results.append(reservation2.process())
# Captura cualquier excepción que ocurra en el bloque try
    except Exception as e:
   # Registra el error en el sistema    
        log_error(e) 
        # Guarda el mensaje del error en la lista de resultados
        results.append(f"Error: {e}")

    # Consultar servicios
    # Guarda el mensaje del error en la lista de resultados
    try:
        # Crea un servicio de consultoría de software con costo de 100
        service3 = ConsultingService("Software Consulting", 100)
# Crea una reserva para el servicio de consultoría con duración de 2
        reservation3 = Reservation(client1, service3, 2)
# Procesa la reserva y almacena el resultado
        results.append(reservation3.process())
# Captura cualquier error generado
    except Exception as e:
       # Registra el error 
        log_error(e) 
        # Guarda el mensaje del error en los resultados
        results.append(f"Error: {e}")

    # Cancelar reserva
# Bloque try para cancelar una reserva    
    try:
# Crea una nueva reserva usando service1
        reservation4 = Reservation(client1, service1, 1)
# Cambia el estado de la reserva a cancelada
        reservation4.cancel()
# Guarda el estado actual de la reserva
        results.append(f"Reservation status: {reservation4.status}")
# Captura errores durante la cancelación
    except Exception as e:
 # Registra el error       
        log_error(e) 
# Guarda el mensaje del error
        results.append(f"Error: {e}")   

    # Confirmar reserva manualmente
# Bloque try para confirmar una reserva
    try:
# Crea una reserva usando el servicio service2
        reservation5 = Reservation(client1, service2, 1) 
# Cambia el estado de la reserva a confirmada
        reservation5.confirm()
# Guarda el estado actualizado de la reserva
        results.append(f"Reservation status: {reservation5.status}")
# Captura cualquier error
    except Exception as e:
# Registra el error        
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")   



    # Caso inválido para probar errores
 # Bloque try para validar datos incorrectos   
    try:
     # Crea un cliente con nombre vacío y correo inválido
        client2 = Client("", "bademail")  # ERROR
        # Captura errores del caso inválido
    except Exception as e:
        
        # Registra el error
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")

    # Correo inválido
 # Bloque try para validar un correo incorrecto   
    try:
    # Crea un cliente con formato de correo inválido
        bad_client2 = Client("Carlos", "invalid-email")
# Captura el error generado
    except Exception as e:
        # Registra el error
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")  

    # Duración inválida
    # Bloque try para validar duración incorrecta
    try:
        # Crea una reserva con duración igual a 0
        bad_reservation = Reservation(client1, service1, 0)
# Intenta procesar la reserva inválida
        results.append(bad_reservation.process())
# Captura errores de validación
    except Exception as e:
   # Registra el error     
        log_error(e) 
         # Guarda el mensaje del error
        results.append(f"Error: {e}")
    
    # Horas en negativo
   # Bloque try para validar valores negativos 
    try:
# Crea un servicio de sala de reuniones con costo de 40
        bad_service = RoomReservation("Meeting Room", 40)
# Intenta calcular el costo usando horas negativas
        results.append(bad_service.calculate_cost(-2))
# Captura el error generado
    except Exception as e:
        # Registra el error
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")

    # Duración de consulta inválida
# Bloque try para validar duración negativa en consultoría    
    try:
# Crea una reserva con duración negativa
        reservation10 = Reservation(client1, service3, -5)
# Intenta procesar la reserva inválida
        results.append(reservation10.process())
# Captura cualquier excepción generada
    except Exception as e:
  # Registra el error      
        log_error(e) 
        # Guarda el mensaje del error
        results.append(f"Error: {e}")



# Retorna todos los resultados obtenidos
    for r in results:
        # Imprime cada resultado en pantalla
        print(r)

# Verifica si el archivo se ejecuta directamente
if __name__ == "__main__":
     # Ejecuta la simulación
    run_simulation()
