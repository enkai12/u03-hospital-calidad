# Controles y resultados del TP3

Realicé la comprobación local el 2026-10-02, con Python 3.14.8. Conservé las diez pruebas del TP2 y sus aseveraciones. Black cambió únicamente su formato; la estructura sintáctica de las pruebas permanece igual.

| Control | Comando | Resultado |
|---|---|---|
| Sintaxis | `python -m compileall -q hospital tests` | Código de salida 0. |
| Formato | `python -m black --check .` | Tres archivos conformes. |
| Linter | `python -m flake8 .` | Código de salida 0. |
| Suite | `python -m unittest discover -s tests -v` | Diez pruebas correctas. |
| Cobertura de aplicación | `python -m coverage run -m unittest discover -s tests -v` y reportes | 17/17 sentencias y 10/10 ramas recorridas. |
| Líneas nuevas | `diff-cover docs/tp3/coverage.xml --compare-branch=main --fail-under=80` | 14/14 líneas ejecutables agregadas recorridas; 100 %. |
| Dependencias de herramientas | `pip-audit -r requirements-dev.txt` | 41 paquetes auditados; sin vulnerabilidades conocidas informadas. |
| Actualización de paquetes instalados | `python -m pip list --outdated --format=json` | Lista vacía: no se informaron versiones posteriores disponibles. |
| Análisis estático | SonarScanner, con cobertura XML importada | Complejidad cognitiva de 12 a 6; S1066 corregido; gate local OK con condiciones efectivas. |

## Qué demostré con el hook

Repetí la secuencia completa en el repositorio real el 2026-10-02. Las fechas de `01` a `05` siguen el orden de ejecución; los escenarios se ejecutaron uno después de otro.

En `logs/01-rechazo-formato.txt` introduje una alteración controlada en los espacios de la firma del método. Black la rechazó y el hook se detuvo antes del linter. Después restauré la firma válida.

En `logs/02-rechazo-linter.txt` agregué deliberadamente una importación sin uso. Black aprobó el formato y flake8 informó F401. No se ejecutaron las pruebas.

En `logs/03-rechazo-pruebas.txt` alteré deliberadamente un valor esperado. Los dos primeros controles pasaron y unittest informó una prueba fallida. Los dos cambios controlados se revirtieron después de registrar el resultado.

Los tres intentos de commit devolvieron código 1 y dejaron el historial sin cambios. `logs/04-controles-en-verde.txt` muestra la ejecución directa posterior a las restauraciones. `logs/05-commit-en-verde.txt` conserva la salida del hook durante el commit exitoso de documentación: tres controles correctos y diez pruebas aprobadas.

## Qué significa cada porcentaje

El reporte instrumental cubre solo la aplicación Python en `hospital/`; los tests se ejecutan, pero no forman parte del denominador del código de producción. El reporte de líneas nuevas cruza esa información con el cambio respecto de `main`. Los scripts y configuraciones tienen evidencia de ejecución, no se incluyen como código Python de aplicación en esa métrica.

En el TP2 identifiqué seis decisiones y doce salidas en el método anterior. Después del refactor identifiqué cinco decisiones y diez salidas. La matriz actual explica los mismos casos sobre las nuevas condiciones. Un porcentaje alto demuestra recorrido; también hacen falta aseveraciones que comprueben resultados.

## Alcance de la integración

El diagnóstico completo está en `diagnostico-estatico.md`, con los JSON exportados de SonarQube. La complejidad ciclomática se mantuvo en 7 y no se detectaron bloques duplicados. Conservé las condiciones de Sonar way y agregué tres controles sobre todo el código para evaluar este segmento; la base fue rechazada y el refactor aprobado.

La autorrevisión prepara el cambio para que otra persona lo examine. La DoD conserva ese requisito antes de integrar. Comprobé el vínculo entre [Issue #1](https://github.com/enkai12/u03-hospital-calidad/issues/1) y [PR #2](https://github.com/enkai12/u03-hospital-calidad/pull/2) en ambos lados. Ambos permanecen abiertos, sin merge. Los enlaces y la autorrevisión están en `trazabilidad-github.md`.

Fuentes: Semana 1, pp. 3–6; Semana 2, pp. 1–4; Semana 3, pp. 1–5.
