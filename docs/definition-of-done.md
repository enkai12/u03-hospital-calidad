# Definition of Done del Hospital Central

La DoD define cuándo un cambio del Hospital Central está terminado y puede integrarse a la rama principal. La pensé como un acuerdo formal, público y vinculante para todo el equipo: vale para funcionalidades nuevas, correcciones y refactorizaciones, y alcanza con que falle un criterio para que el cambio no se integre hasta corregirlo.

La DoD no reemplaza los criterios de aceptación de cada tarea, sino que los complementa. Los criterios de aceptación describen lo que una tarea puntual tiene que lograr, y por eso conviene que sean claros, específicos, medibles y verificables; por ejemplo, que un turno urgente quede registrado con la marca -URGENTE. La DoD, en cambio, fija las condiciones de calidad que se le piden a cualquier cambio, sea cual sea la tarea.

Los seis criterios quedan en una tabla que también uso como lista de control en cada Pull Request:

| Criterio | Qué exijo para integrar | Cómo lo compruebo |
|---|---|---|
| 1 Integridad de compilación | El código compila limpio en local, sin errores ni advertencias críticas pendientes. | Python no tiene un paso de compilación visible, así que uso python -m compileall y flake8, que marca errores de sintaxis y nombres sin definir. |
| 2 Pruebas automatizadas | Pasa el 100 % de las pruebas unitarias y funcionales del componente modificado. Una sola prueba fallida bloquea la integración. | El reporte de la corrida, con fecha y resultado, sobre el mismo código que se propone integrar. |
| 3 Cobertura mínima | Las pruebas recorren al menos el 80 % de las líneas ejecutables nuevas. | La comparación con la versión anterior y el reporte de cobertura. |
| 4 Revisión por pares | Otra persona del equipo revisa el cambio buscando malas prácticas, desvíos de los patrones adoptados y complejidad innecesaria, y lo aprueba. | Las observaciones, las correcciones y la aprobación registradas en el Pull Request. |
| 5 Gobernanza de estilo | El código pasa el formatter y el linter con las reglas del proyecto. | Las salidas de los dos controles y la configuración usada. |
| 6 Documentación técnica | Quedan documentados los cambios en contratos, las funciones complejas y los esquemas de datos o interfaces afectados. | La documentación modificada junto con el código y revisada en el Pull Request. |

Hay dos criterios que conviene explicar mejor. El umbral del 80 % se mide solo sobre las líneas ejecutables nuevas: se cuentan las líneas agregadas que las pruebas recorren y se dividen por el total de líneas agregadas. Por eso el porcentaje general del proyecto no alcanza para demostrarlo, y si un cambio no agrega líneas ejecutables, lo dejo indicado en el PR. Llegar al 80 % tampoco asegura que no haya errores: muestra que el código nuevo se ejecutó durante las pruebas, no que haga lo correcto en todos los casos.

La revisión por pares es el único criterio que depende de otra persona. Antes de aprobar, quien revisa controla que el cambio venga con sus pruebas, respete el estilo, tenga la documentación necesaria y resuelva una sola cosa, porque un PR demasiado grande es difícil de revisar. Vincular el PR con un issue muestra de dónde viene el trabajo, pero no prueba que otra persona lo haya revisado.

Para llevarla a la práctica en Python propongo unittest para las pruebas, coverage.py para la cobertura, Black como formatter y flake8 como linter. En Python, muchos errores que en Java frena el compilador pasan de largo hasta que se ejecuta el código, así que el rigor no viene puesto en el lenguaje: depende de las convenciones, del linter, de las pruebas y de la revisión del equipo. La métrica de cobertura y las reglas de estilo las define cada proyecto; estas son las que elegí para el Hospital Central.
