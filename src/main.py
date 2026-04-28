from src.models.client import Client
from src.models.room_reservation import RoomReservation
from src.models.reservation import Reservation
from src.utils.logger import log_error


def run_simulation():

    # Lista para guardar resultados
    results = []

    try:
        client1 = Client("Martin", "martin@email.com")
        service1 = RoomReservation("Conference Room", 50)

        reservation1 = Reservation(client1, service1, 2)
        results.append(reservation1.process())

    except Exception as e:
        log_error(e)
        results.append(f"Error: {e}")

    # Caso inválido
    try:
        client2 = Client("", "bademail")  # ERROR
    except Exception as e:
        log_error(e)
        results.append(f"Error: {e}")

    for r in results:
        print(r)


if __name__ == "__main__":
    run_simulation()