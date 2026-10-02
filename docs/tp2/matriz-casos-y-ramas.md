# Matriz de casos y ramas del TP2

Segmento: `hospital/turnos.py`, método `TurnoManager.procesar`. V significa verdadera y F falsa. Las decisiones no alcanzadas no se evalúan. Cada caso tiene su prueba en `tests/test_turnos.py`: C1 es `test_c01`, C2 es `test_c02`, y así hasta C10.

| Caso | Entrada y resultado esperado | Recorrido |
|---|---|---|
| C1 | (None, 30, OSDE, False). Sin turnos ni mensajes. | D1 F; el segundo operando no se evalúa. |
| C2 | (vacío, 30, OSDE, False). Sin turnos ni mensajes. | D1 F; ambos operandos se evalúan. |
| C3 | (Ana, 0, OSDE, False). Sin turnos ni mensajes. | D1 V → D2 F. |
| C4 | (Ana, −1, OSDE, False). Sin turnos ni mensajes. | D1 V → D2 F. |
| C5 | (Ana, 30, OSDE, True). Ana-30-OSDE-URGENTE; premium y turno agregado. | D1 V → D2 V → D3 V → D6 V. |
| C6 | (Ana, 30, SWISS, False). Ana-30-SWISS; premium y turno agregado. | D1 V → D2 V → D3 F → D4 V → D6 F. |
| C7 | (Ana, 30, PUBLICA, False). Ana-30-PUBLICA; público y turno agregado. | D1 V → D2 V → D3 F → D4 F → D5 V → D6 F. |
| C8 | (Ana, 30, OTRA, False). Ana-30-OTRA; solo turno agregado. | D1 V → D2 V → D3 F → D4 F → D5 F → D6 F. |
| C9 | (un espacio, 1, PUBLICA, False). Un espacio seguido de -1-PUBLICA; público y turno agregado. | Mismo recorrido que C7. |
| C10 | Dos llamadas: (Ana, 30, OSDE, True) y (Luis, 20, PUBLICA, False). Dos turnos, en ese orden, y mensajes de ambos. | Recorridos de C5 y C7 sobre una instancia nueva. |

| Decisión | Salida verdadera | Salida falsa |
|---|---|---|
| D1 Nombre no nulo y no vacío | C3–C10 | C1, C2 |
| D2 Edad mayor que cero | C5–C10 | C3, C4 |
| D3 Obra social OSDE | C5, C10 | C6–C9, C10 |
| D4 Obra social SWISS | C6 | C7–C9, C10 |
| D5 Obra social PUBLICA | C7, C9, C10 | C8 |
| D6 Urgencia | C5, C10 | C6–C10 |

Se identifican seis decisiones de control y dos salidas por decisión: 12 salidas. Los casos C1–C8 recorren las 12; C4 refuerza el límite negativo, C9 conserva el tratamiento original del espacio y C10 verifica la acumulación y el orden. El resultado es 12/12 = 100 % de las ramas del método. Lo calculé a mano a partir del código y los casos.

D1 tiene dos operandos: `nombre_paciente is not None` y `nombre_paciente != ""`. C1 hace falso el primero y omite el segundo; C2 hace verdadero el primero y falso el segundo; los nombres válidos hacen verdaderos ambos.
