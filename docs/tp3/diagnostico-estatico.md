# Diagnóstico estático antes y después

Analicé las dos versiones de `hospital/turnos.py` con SonarQube Community Build 26.9.0.129388 y SonarScanner CLI 8.1.0.6389. Usé dos proyectos locales, porque esta edición trabaja con una rama principal por proyecto. En ambos identifiqué `hospital/` como código de aplicación y `tests/` como pruebas, e importé la cobertura XML de la versión correspondiente.

La base conserva el código del TP2 en `main`. La versión posterior corresponde a las cláusulas de guarda y a la agrupación de OSDE y SWISS. Las diez pruebas mantienen sus entradas y aseveraciones.

## Comparación

| Métrica del código de aplicación | Antes | Después |
|---|---:|---:|
| Líneas de código sin comentarios | 19 | 17 |
| Complejidad ciclomática del archivo | 7 | 7 |
| Complejidad ciclomática de `procesar` (mccabe) | 7 | 6 |
| Complejidad cognitiva | 12 | 6 |
| Bloques duplicados detectados | 0 | 0 |
| Densidad de líneas duplicadas | 0 % | 0 % |
| Hallazgos de mantenibilidad abiertos | 1 | 0 |
| Bugs detectados | 0 | 0 |
| Vulnerabilidades del código detectadas | 0 | 0 |
| Cobertura importada | 100 % | 100 % |
| Condiciones para cobertura de ramas | 12 | 10 |
| Deuda técnica (esfuerzo de corrección) | 5 min | 0 min |
| Relación de deuda técnica | 0,9 % | 0 % |
| Calificación de mantenibilidad, confiabilidad y seguridad | A | A |

SonarQube señaló `python:S1066` en la versión anterior: recomienda reunir el `if` de edad con el que lo contiene. Elegí cláusulas de guarda para quitar ese anidamiento y dejar el flujo válido seguido. La complejidad cognitiva bajó de 12 a 6 y la deuda técnica estimada por SonarQube pasó de 5 minutos a 0. La ciclomática que informa SonarQube es la del archivo completo y quedó en 7; medida por método con mccabe, la de `procesar` bajó de 7 a 6, porque pasó de seis a cinco decisiones (`logs/11-complejidad-mccabe.txt`). La deuda y las calificaciones las consulté el 4 de octubre por la API local sobre los mismos análisis y están en `sonar-deuda-tecnica.json`. La agrupación de los mensajes premium elimina código copiado, que es una forma de deuda técnica, aunque el analizador no lo detectó como bloque duplicado en ninguna versión porque se trataba de una sola línea. Las métricas son del código de aplicación y siguen las reglas del analizador; no se identifican con el conteo manual de decisiones del TP2.

## Condiciones efectivas del Quality Gate

La primera corrida con `Sonar way` devolvió OK sin condiciones de código nuevo evaluadas. Para obtener un control sobre este segmento pequeño, copié ese gate a `U03 Hospital Central`, conservé sus cuatro condiciones y agregué tres condiciones sobre todo el código. Es una elección de esta implementación; no cambia el umbral de líneas nuevas definido en la DoD.

| Condición agregada | Rechaza cuando | Antes | Después |
|---|---|---|---|
| Hallazgos de mantenibilidad | `code_smells > 0` | 1: ERROR | 0: OK |
| Cobertura importada | `coverage < 80` | 100 %: OK | 100 %: OK |
| Duplicación | `duplicated_lines_density > 3` | 0 %: OK | 0 %: OK |

También se evaluó `new_violations > 0`, con valor 0 en las dos versiones. Las condiciones heredadas de cobertura nueva, duplicación nueva y revisión de hotspots nuevos no tienen valores en estas corridas, porque la repetición del análisis no agregó código respecto de la primera versión de cada proyecto. La cobertura del cambio real frente a `main` se comprueba por separado con diff-cover: 14 líneas ejecutables cubiertas de 14.

Con el mismo gate, la base fue rechazada por S1066 y la versión refactorizada obtuvo OK. El scanner devolvió código 3 para el rechazo esperado de la base y 0 para la versión posterior. Exporté las métricas, los hallazgos y las condiciones mediante la API local en `sonar-antes.json` y `sonar-despues.json`. Los extractos de salida están en `logs/08-sonar-antes.txt` y `logs/09-sonar-despues.txt`.

## Dependencias y alcance

La aplicación utiliza la biblioteca estándar. La auditoría de `requirements-dev.txt` corresponde a las herramientas de desarrollo: 41 paquetes. El 2 de octubre no hubo vulnerabilidades conocidas y `python -m pip list --outdated --format=json` devolvió una lista vacía (`logs/07-auditoria-dependencias.txt`). El 4 de octubre la misma consulta informó cinco paquetes con una versión posterior: black 26.5.1 → 26.10.0, filelock 4.0.9 → 4.0.10, MarkupSafe 3.0.3 → 3.0.4, platformdirs 4.12.2 → 4.12.3 y pyflakes 4.0.1 → 4.0.2. Los actualicé, fijé las versiones en el manifiesto, comprobé que no quedaran dependencias incompatibles y volví a correr el hook, pip-audit y la consulta de versiones: diez pruebas correctas, ninguna vulnerabilidad conocida y ningún paquete desactualizado. Black 26.10.0 no reformateó ningún archivo. Todo el recorrido está en `logs/10-actualizacion-dependencias.txt`; `pip-audit.json` y `pip-outdated.json` corresponden al manifiesto actualizado.

pip-audit consulta vulnerabilidades conocidas; pip consulta si existe una versión más reciente. Una dependencia desactualizada no necesariamente es vulnerable. Si aparece una actualización, debo evaluar su compatibilidad y repetir los controles antes de cambiar el manifiesto; si hay una vulnerabilidad, debo buscar la versión corregida. SonarQube examina el código de aplicación y tiene un alcance distinto de estas consultas.

Fundamento: Semana 3, pp. 2–3; U01-A03, pp. 3–4. Herramientas, configuración, umbrales adicionales y refactor son decisiones propias. El servidor se utiliza en consola para esta evaluación local; la base H2 es de evaluación.
