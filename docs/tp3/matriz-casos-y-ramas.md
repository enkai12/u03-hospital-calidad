# Matriz de casos y ramas después del refactor

Analicé `TurnoManager.procesar` después de introducir cláusulas de guarda y agrupar OSDE con SWISS. Conservé los diez casos del TP2 y sus aseveraciones. El mapa original queda en `docs/tp2/`; este documento describe la versión del TP3.

| Decisión | Condición | Salida verdadera | Salida falsa |
|---|---|---|---|
| D1 | Nombre nulo o vacío: rechazar. | C1, C2 | C3–C10 |
| D2 | Edad menor o igual a cero: rechazar. | C3, C4 | C5–C10 |
| D3 | Obra social en OSDE o SWISS. | C5, C6, C10 | C7–C9, C10 |
| D4 | Obra social PUBLICA. | C7, C9, C10 | C8 |
| D5 | Urgencia. | C5, C10 | C6–C10 |

| Caso | Recorrido después del refactor | Resultado conservado |
|---|---|---|
| C1 | D1 V, retorno. El segundo operando del `or` se omite. | Sin registro ni mensajes. |
| C2 | D1 V, retorno. El primer operando es F y el segundo V. | Sin registro ni mensajes. |
| C3 | D1 F → D2 V, retorno. | Edad cero: sin registro ni mensajes. |
| C4 | D1 F → D2 V, retorno. | Edad negativa: sin registro ni mensajes. |
| C5 | D1 F → D2 F → D3 V → D5 V. | Ana-30-OSDE-URGENTE; premium y confirmación. |
| C6 | D1 F → D2 F → D3 V → D5 F. | Ana-30-SWISS; premium y confirmación. |
| C7 | D1 F → D2 F → D3 F → D4 V → D5 F. | Ana-30-PUBLICA; público y confirmación. |
| C8 | D1 F → D2 F → D3 F → D4 F → D5 F. | Ana-30-OTRA; solo confirmación. |
| C9 | Igual a C7. | Conserva el nombre con un espacio y edad 1. |
| C10 | Recorridos de C5 y C7 sobre el mismo gestor. | Dos registros en el orden de las llamadas. |

Se recorren las diez salidas de las cinco decisiones. D1 mantiene el cortocircuito: para un nombre nulo omite la comparación con la cadena vacía; para un nombre vacío la evalúa. Cambió la organización de las condiciones, no el comportamiento definido en el TP2.

La medición instrumental está en `coverage.xml` y `coverage.json`: 17 sentencias ejecutables de la aplicación, ninguna sin recorrer; 10 ramas, ninguna sin recorrer. Su alcance es `hospital/`. La cobertura de líneas ejecutables nuevas se calcula por separado con diff-cover frente a `main`.

Fuentes: Práctico 2, punto 3; Semana 2, sección 3, pp. 3–4; Práctico 3, punto 2.
