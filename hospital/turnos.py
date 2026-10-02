"""Adaptación de TurnoManager.procesar de U01, sin nuevas reglas.

Alcance: nombre str o None, edad int, obra_social str y urgente bool.
La lista turnos permite observar el estado registrado en las pruebas.
"""


class TurnoManager:
    """Registra turnos con los mensajes del código original."""

    def __init__(self):
        self.turnos = []

    def procesar(
        self, nombre_paciente, edad, obra_social, urgente
    ):
        """Registra el turno si hay nombre y la edad es positiva."""
        if nombre_paciente is not None and nombre_paciente != "":
            if edad > 0:
                if obra_social == "OSDE":
                    print("Paciente premium")
                elif obra_social == "SWISS":
                    print("Paciente premium")
                elif obra_social == "PUBLICA":
                    print("Paciente publico")

                turno = f"{nombre_paciente}-{edad}-{obra_social}"
                if urgente:
                    turno += "-URGENTE"

                self.turnos.append(turno)
                print("Turno agregado")
