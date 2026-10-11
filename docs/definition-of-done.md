# Definition of Done del Hospital Central

La DoD define cuándo un cambio del Hospital Central está terminado y puede integrarse a la rama principal. La planteé como un acuerdo formal, público y vinculante para el equipo: vale para funcionalidades nuevas, correcciones y refactorizaciones, y si un solo criterio no se cumple, el cambio no se integra hasta corregirlo.

No reemplaza los criterios de aceptación de cada tarea. Que un turno urgente quede marcado con -URGENTE es un comportamiento que se pide para esa tarea; que las pruebas pasen y la documentación esté al día se le exige a cualquier cambio.

Los seis criterios quedan en una tabla, que también sirve como lista de control para cada Pull Request:

| Criterio | Qué exijo para integrar | Cómo lo compruebo |
|---|---|---|
| 1 Integridad de compilación | El código compila limpio en local, sin errores ni advertencias críticas pendientes. | Python no tiene un paso de compilación visible, así que uso python -m compileall y flake8, que marca errores de sintaxis y nombres sin definir. |
| 2 Pruebas automatizadas | Pasa el 100 % de las pruebas unitarias y funcionales del componente modificado. Una sola prueba fallida bloquea la integración. | El reporte de la corrida, con fecha y resultado, sobre el mismo código que se propone integrar. |
| 3 Cobertura mínima | Las pruebas recorren al menos el 80 % de las líneas ejecutables nuevas. | La comparación con la versión anterior y el reporte de cobertura. |
| 4 Revisión por pares | Otra persona del equipo revisa malas prácticas, respeto de los patrones y complejidad innecesaria, y aprueba el cambio. | Las observaciones, las correcciones y la aprobación registradas en el Pull Request. |
| 5 Gobernanza de estilo | El código pasa el formatter y el linter con las reglas del proyecto. | Las salidas de los dos controles y la configuración usada. |
| 6 Documentación técnica | Quedan documentados los cambios en contratos, las funciones complejas y los esquemas de datos o interfaces afectados. | La documentación modificada junto con el código y revisada en el Pull Request. |

Dos criterios necesitan una aclaración. El 80 % lo tomé del ejemplo de la lectura de Semana 1 y se refiere solo a las líneas nuevas: se calcula como líneas nuevas recorridas sobre líneas nuevas totales, así que el porcentaje general del proyecto no alcanza para demostrarlo. Si un cambio no agrega líneas ejecutables, lo dejo indicado en el PR. Llegar al 80 % tampoco garantiza que no haya errores. En cuanto a la revisión por pares, vincular el PR con un issue muestra de dónde viene el cambio, pero no prueba que otra persona lo haya revisado.

Para implementarla en Python propongo unittest para las pruebas, coverage.py para la cobertura, Black como formatter y flake8 como linter. La lectura deja la métrica de cobertura y las reglas de estilo a cargo de cada proyecto, y Black es el formatter que nombra la Semana 3.
