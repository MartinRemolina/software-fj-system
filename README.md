#Software FJ System

Descripción del Proyecto

Software FJ System es una aplicación desarrollada en Python bajo el paradigma de Programación Orientada a Objetos (POO), diseñada para gestionar clientes, servicios y reservas para una empresa ficticia llamada Software FJ.

El sistema permite administrar distintos tipos de servicios, incluyendo:

Reservas de salas
Alquiler de equipos
Asesorías especializadas

El proyecto fue desarrollado sin utilizar bases de datos, implementando el almacenamiento y manejo de información mediante objetos, listas y archivos de logs.

Objetivos del Proyecto

Este proyecto tiene como propósito aplicar los principales conceptos de Programación Orientada a Objetos y manejo avanzado de excepciones en Python.

Entre los objetivos principales se encuentran:

Aplicar abstracción, herencia, encapsulación y polimorfismo.
Implementar clases abstractas y clases derivadas.
Desarrollar un sistema modular y extensible.
Gestionar errores mediante excepciones personalizadas.
Registrar eventos y errores en archivos de logs.
Simular operaciones válidas e inválidas sin interrumpir la ejecución del sistema.


Tecnologías Utilizadas

Python 3
Programación Orientada a Objetos (POO)
Biblioteca estándar de Python
Manejo de archivos
Git y GitHub


Principales Características

Gestión de Clientes

La clase Client permite:

Registrar clientes.
Validar nombres y correos electrónicos.
Aplicar encapsulación de datos.
Servicios Especializados

El sistema implementa una clase abstracta llamada Service, de la cual heredan distintos tipos de servicios:

RoomReservation

Permite gestionar reservas de salas.

EquipmentRental

Permite gestionar alquileres de equipos.

ConsultingService

Permite gestionar asesorías especializadas.

Cada servicio implementa polimorfismo mediante la sobrescritura de métodos como:

calculate_cost()
description()
Gestión de Reservas

La clase Reservation integra:

Cliente
Servicio
Duración
Estado de la reserva

Además, permite:

Confirmar reservas
Cancelar reservas
Procesar operaciones
Validar errores durante la ejecución
Manejo de Excepciones

El sistema implementa manejo avanzado de excepciones utilizando:

try/except
try/except/else
try/except/finally
Excepciones personalizadas
Registro de errores en logs

Ejemplos de errores controlados:

Nombres vacíos
Correos inválidos
Duraciones negativas
Reservas incorrectas
Parámetros inválidos
Archivo de Logs

Todos los errores y eventos relevantes se registran automáticamente en:

logs/system.log

Esto permite mantener trazabilidad y robustez durante la ejecución del sistema.


Simulaciones Implementadas

El sistema incluye simulaciones de operaciones válidas e inválidas para demostrar:

Robustez del sistema
Continuidad de ejecución
Manejo de errores
Polimorfismo
Validaciones

Entre las simulaciones realizadas se incluyen:

Reservas exitosas
Cancelaciones
Confirmaciones manuales
Clientes inválidos
Correos incorrectos
Duraciones negativas
Servicios inválidos


Durante el desarrollo de este proyecto se aplicaron:

Abstracción
Encapsulación
Herencia
Polimorfismo
Modularidad
Manejo de excepciones
Validaciones
Persistencia mediante archivos
