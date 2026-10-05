# Hospital Central — Calidad de software en U03

Agustín Emiliano Sotelo Carmelich · Metodología de Sistemas II · Unidad 3

Retomé el método de turnos del Hospital Central trabajado en U01 y lo adapté a Python en el TP2. En el TP3 simplifiqué sus condiciones y agregué controles locales antes de cada commit. Conservé los mensajes, el registro de turnos y el sufijo `-URGENTE`.

## Preparación

Probé el proyecto con Python 3.14.8. Las herramientas se instalan en un entorno del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
git config core.hooksPath hooks
```

El último comando se ejecuta dentro del repositorio Git. Para una copia obtenida por ZIP, primero hay que inicializar Git si se quiere probar el hook. La comparación de líneas nuevas requiere la versión base en `main`; para reproducirla se usa el historial del repositorio.

## Pruebas y controles

```bash
python -m unittest discover -s tests -v
python -m black --check .
python -m flake8 .
python -m compileall -q hospital tests
```

El hook ejecuta Black, flake8 y las diez pruebas en ese orden. Si un paso falla, termina con error y Git aborta el commit. Revisa la carpeta de trabajo completa. Se instala en cada copia y no sustituye la revisión del PR.

## Cobertura y dependencias

```bash
python -m coverage run -m unittest discover -s tests -v
python -m coverage report -m
python -m coverage xml
python -m coverage json -o docs/tp3/coverage.json
python -m coverage html -d docs/tp3/cobertura-html
diff-cover docs/tp3/coverage.xml --compare-branch=main --fail-under=80
pip-audit -r requirements-dev.txt
python -m pip list --outdated
```

La medición cubre `hospital/`: 17 sentencias y 10 ramas, todas recorridas. La comparación del refactor frente a `main` cubre las 14 líneas ejecutables agregadas. El 80 % se aplica a estas líneas nuevas; el mapa de ramas se analiza por separado. La aplicación usa la biblioteca estándar; las dependencias auditadas son las 41 del manifiesto de herramientas. El 2 de octubre no había vulnerabilidades conocidas ni paquetes desactualizados. El 4 de octubre `pip list --outdated` informó cinco paquetes con una versión posterior (entre ellos Black 26.5.1 → 26.10.0): los actualicé, fijé las versiones nuevas en `requirements-dev.txt`, volví a pasar el hook y pip-audit, y quedaron sin vulnerabilidades ni paquetes desactualizados (`docs/tp3/logs/10-actualizacion-dependencias.txt`). Una versión antigua y una vulnerabilidad son comprobaciones distintas.

## Archivos

| Archivo o carpeta | Contenido |
|---|---|
| `hospital/turnos.py` | Lógica de turnos después del refactor. |
| `tests/test_turnos.py` | Diez casos con AAA y sus aseveraciones originales. |
| `hooks/pre-commit` | Secuencia de controles locales. |
| `setup.cfg` | Reglas del linter y alcance de cobertura. |
| `requirements-dev.txt` | Versiones de las herramientas y sus dependencias. |
| `sonar-project.properties` | Análisis local de la aplicación e importación de cobertura. |
| `docs/definition-of-done.md` | Seis criterios definidos en el TP1. |
| `docs/labels.md` | Categorías de trabajo del TP1. |
| `.github/ISSUE_TEMPLATE/reporte-de-defecto.md` | Plantilla de incidencia del TP1, con el encabezado que GitHub usa para ofrecerla en «New issue» una vez integrada a `main`. |
| `docs/tp2/` | Matriz, resultado y medición de sentencias y ramas del TP2. |
| `docs/tp3/` | Matriz actualizada y evidencias del TP3; los logs están numerados en orden en `docs/tp3/logs/`. |

## Diagnóstico estático

Comparé la base y el refactor con SonarQube Community Build 26.9.0.129388 y SonarScanner CLI 8.1.0.6389 locales. La complejidad cognitiva bajó de 12 a 6, se corrigió el hallazgo S1066 y la deuda técnica pasó de 5 minutos (0,9 %) a 0, con calificación A en mantenibilidad, confiabilidad y seguridad. SonarQube informa una complejidad ciclomática de 7 para el archivo en las dos versiones; medida por método con mccabe, la de `procesar` bajó de 7 a 6. No se detectaron bloques duplicados. Importé cobertura XML en los dos proyectos.

El gate local conserva las condiciones de Sonar way y suma controles de cero hallazgos de mantenibilidad, cobertura global mínima del 80 % y duplicación máxima del 3 %. La base fue rechazada y el refactor aprobó. La cobertura de líneas nuevas frente a `main` se comprueba por separado con diff-cover. Los resultados y las condiciones efectivas están en [el diagnóstico](docs/tp3/diagnostico-estatico.md) y sus archivos JSON.

## Trazabilidad

El [Issue #1](https://github.com/enkai12/u03-hospital-calidad/issues/1) describe la tarea con `technical-debt`; el [PR #2](https://github.com/enkai12/u03-hospital-calidad/pull/2) contiene `Closes #1` y mi [autorrevisión](https://github.com/enkai12/u03-hospital-calidad/pull/2#issuecomment-5962466520). Verifiqué el vínculo en los dos lados. Ambos siguen abiertos, sin merge: la integración requiere la revisión y aprobación de otra persona según la DoD.

## Límites y alternativas

Trabajé con nombre como cadena o `None`, edad entera, obra social como cadena y urgencia booleana. Conservé también la aceptación del nombre con un espacio y de una obra social desconocida. Otra alternativa habría sido separar la validación, la clasificación y el formato en clases propias, como hice en el TP1 de U01, pero preferí una corrección pequeña sobre el método existente y dejo esa extracción como paso siguiente. También junté en un mismo PR el refactor y los controles, aunque lo ideal es que un PR resuelva una sola cosa; la alternativa eran dos PR. Los controles locales pueden omitirse si se desactiva el hook; la integración sigue dependiendo de la revisión por otra persona establecida en la DoD.

## Material utilizado

Metodología II, Prácticos 1–3 y lecturas de Semana 1, 2 y 3; U01-A03, Clean Code y Code Review. Código original de `TurnoManager` de U01. Programación IV, U03-A01, pp. 2–4, como fundamento del uso de herramientas y pruebas en Python. Black y SonarQube aparecen en Semana 3; unittest, flake8, coverage.py, diff-cover, pip-audit y SonarScanner son elecciones para esta implementación.
