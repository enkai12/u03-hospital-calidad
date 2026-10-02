# TP 2 — Testing práctico y contratos

Agustín Emiliano Sotelo Carmelich · Metodología de Sistemas II · Unidad 3

Acá está el código del TP 2. Pasé a Python el método `procesar` del `TurnoManager` del
Hospital Central (U01) sin cambiarle las reglas, y le armé una suite con el patrón AAA.

## Cómo lo corro

Desde esta carpeta, con Python 3 y sin instalar nada:

```
python3 -m unittest discover -s tests -v
```

## Qué hay

| Archivo | Qué es |
|---|---|
| `hospital/turnos.py` | La adaptación de `TurnoManager.procesar` |
| `tests/test_turnos.py` | Las 10 pruebas, cada una con Arrange, Act y Assert marcados |
| `docs/tp2/matriz-casos-y-ramas.md` | Los casos C1 a C10 y qué rama recorre cada uno |
| `docs/tp2/resultado-unittest.txt` | La salida de la última corrida |

## Resultado

10 pruebas, las 10 en verde. Cubren el nombre nulo o vacío, la edad cero o negativa,
las tres obras sociales conocidas y una desconocida, la urgencia, el nombre con un
espacio y la edad 1, y dos turnos seguidos en el mismo gestor. Con C1 a C8 se recorren
las 12 salidas de las seis decisiones del método.
