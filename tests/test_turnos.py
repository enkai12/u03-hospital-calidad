"""Suite AAA para la adaptación de TurnoManager.procesar de U01."""

import unittest
from contextlib import redirect_stdout
from io import StringIO

from hospital.turnos import TurnoManager


class TurnoManagerTest(unittest.TestCase):
    """Pruebas de procesar: cada una parte de un gestor nuevo."""

    def test_c01_nombre_nulo(self):
        """Nombre None: no registra el turno ni imprime nada."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar(None, 30, "OSDE", False)

        # Assert
        self.assertEqual(gestor.turnos, [])
        self.assertEqual(salida.getvalue(), "")

    def test_c02_nombre_vacio(self):
        """Nombre vacío: no registra el turno ni imprime nada."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("", 30, "OSDE", False)

        # Assert
        self.assertEqual(gestor.turnos, [])
        self.assertEqual(salida.getvalue(), "")

    def test_c03_edad_cero(self):
        """Edad cero: el turno se rechaza."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 0, "OSDE", False)

        # Assert
        self.assertEqual(gestor.turnos, [])
        self.assertEqual(salida.getvalue(), "")

    def test_c04_edad_negativa(self):
        """Edad negativa: el turno se rechaza."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", -1, "OSDE", False)

        # Assert
        self.assertEqual(gestor.turnos, [])
        self.assertEqual(salida.getvalue(), "")

    def test_c05_osde_urgente(self):
        """OSDE urgente: paciente premium y turno con -URGENTE."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 30, "OSDE", True)

        # Assert
        self.assertEqual(gestor.turnos, ["Ana-30-OSDE-URGENTE"])
        self.assertEqual(salida.getvalue(), "Paciente premium\nTurno agregado\n")

    def test_c06_swiss_normal(self):
        """SWISS sin urgencia: premium y turno sin sufijo."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 30, "SWISS", False)

        # Assert
        self.assertEqual(gestor.turnos, ["Ana-30-SWISS"])
        self.assertEqual(salida.getvalue(), "Paciente premium\nTurno agregado\n")

    def test_c07_publica_normal(self):
        """PUBLICA sin urgencia: paciente público y turno."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 30, "PUBLICA", False)

        # Assert
        self.assertEqual(gestor.turnos, ["Ana-30-PUBLICA"])
        self.assertEqual(salida.getvalue(), "Paciente publico\nTurno agregado\n")

    def test_c08_otra_obra_social(self):
        """Otra obra social: sin mensaje, pero se registra."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 30, "OTRA", False)

        # Assert
        self.assertEqual(gestor.turnos, ["Ana-30-OTRA"])
        self.assertEqual(salida.getvalue(), "Turno agregado\n")

    def test_c09_nombre_con_espacio_y_edad_uno(self):
        """Un espacio no es nombre vacío y la edad 1 es válida."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar(" ", 1, "PUBLICA", False)

        # Assert
        self.assertEqual(gestor.turnos, [" -1-PUBLICA"])
        self.assertEqual(salida.getvalue(), "Paciente publico\nTurno agregado\n")

    def test_c10_acumulacion_y_orden(self):
        """Dos turnos en el mismo gestor quedan en orden."""
        # Arrange
        gestor = TurnoManager()
        salida = StringIO()

        # Act
        with redirect_stdout(salida):
            gestor.procesar("Ana", 30, "OSDE", True)
            gestor.procesar("Luis", 20, "PUBLICA", False)

        # Assert
        self.assertEqual(gestor.turnos, ["Ana-30-OSDE-URGENTE", "Luis-20-PUBLICA"])
        self.assertEqual(
            salida.getvalue(),
            "Paciente premium\nTurno agregado\nPaciente publico\nTurno agregado\n",
        )


if __name__ == "__main__":
    unittest.main()
