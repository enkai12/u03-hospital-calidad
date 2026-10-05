# Definition of Done del Hospital Central

Para el Hospital Central definí una DoD que establece cuándo un cambio está en condiciones de integrarse a la rama principal. La propuesta es un acuerdo explícito, formal, público y vinculante: sus criterios deben ser conocidos por quienes trabajen en el sistema y cumplirse en su totalidad. Si uno falla, el cambio no se integra hasta corregirlo.

Aunque realizo este TP de manera individual, redacté la DoD para el equipo de trabajo, como pide la consigna. Se aplica a funcionalidades nuevas, correcciones y refactorizaciones, y se mantiene durante el ciclo de desarrollo.

La DoD no reemplaza los criterios de aceptación de cada tarea. Por ejemplo, que un turno urgente quede identificado como urgente es una condición del comportamiento del sistema. En cambio, que sus pruebas pasen y su documentación esté actualizada son controles de calidad que se exigen a todos los cambios. En Gestión de Desarrollos de Software vimos que los criterios de aceptación tienen que ser claros, específicos, medibles y verificables, y que se complementan con los criterios de calidad. Por eso la DoD y los criterios de aceptación se exigen juntos.

## 1 Integridad de compilación

Como el proyecto está en Python, que no tiene un paso de compilación visible como Java, propongo comprobarlo con python -m compileall y con flake8, que marca errores de sintaxis y nombres sin definir. Que el programa ande al probarlo a mano no reemplaza estos controles.

Un error de compilación o una advertencia crítica pendiente impide integrar el cambio. La evidencia debe ser la salida fechada del control, con el entorno y la versión del código examinada.

## 2 Pruebas automatizadas

El 100 % de las pruebas unitarias y funcionales locales asociadas al componente modificado debe finalizar correctamente. Una sola prueba fallida impide integrar el cambio, aunque las demás pasen.

La evidencia debe incluir el reporte y los logs de la corrida: identificación de los casos, fecha, entorno, operador, resultado y tiempo de ejecución. El informe tiene que corresponder al mismo código que se propone integrar.

## 3 Cobertura mínima

Elegí el 80 % de las líneas ejecutables nuevas como umbral mínimo, tomando el ejemplo de la lectura de Semana 1. Para medirlo, se deben identificar las líneas agregadas respecto de la versión anterior al cambio y contrastarlas con el reporte de cobertura de las pruebas automáticas.

El porcentaje se calcula dividiendo las líneas ejecutables nuevas recorridas por las pruebas por el total de líneas ejecutables nuevas, y multiplicando por 100. Si el resultado es menor al 80 %, el cambio no se integra. Si el cambio no agrega líneas ejecutables, se deja constancia de eso en el Pull Request.

La evidencia debe mostrar la comparación entre versiones y el reporte que permite comprobar qué líneas nuevas fueron ejecutadas. El porcentaje general del proyecto no basta para demostrar este criterio. Además, llegar al 80 % no garantiza que no haya errores.

## 4 Revisión por pares

Otra persona con participación técnica en el equipo debe revisar el cambio antes de integrarlo. La revisión debe controlar las malas prácticas, el respeto de los patrones adoptados y los incrementos innecesarios de complejidad.

Sin esa revisión y su aprobación, el cambio no se integra. La evidencia debe incluir las observaciones, las correcciones realizadas y la aprobación registrada en el Pull Request. Vincular el PR con un issue permite seguir el origen del cambio, pero no demuestra que otra persona lo haya revisado.

## 5 Gobernanza de estilo

El código debe cumplir las reglas de estilo configuradas para el proyecto y superar los controles del formatter y del linter. El objetivo es mantener una escritura uniforme y detectar los desvíos antes de integrar.

Si alguno de esos controles informa un incumplimiento pendiente, el cambio no se integra. La evidencia debe incluir sus salidas fechadas y la configuración utilizada, de modo que el resultado pueda comprobarse sobre la versión revisada.

## 6 Documentación técnica

Los cambios que alteren contratos de comunicación deben quedar documentados. También deben documentarse las funciones de alta complejidad y actualizarse los esquemas de datos y las especificaciones de interfaces cuando corresponda al cambio.

Si la documentación necesaria queda desactualizada o falta, el cambio no se integra. La evidencia debe ser la documentación modificada junto con el código y su revisión en el Pull Request. Para una firma pública usada por otros módulos, por ejemplo, debe quedar claro qué recibe, qué devuelve y qué cambió.

## Aplicación de los controles

Para la futura implementación en Python propongo unittest para las pruebas, coverage.py para la cobertura, Black como formatter y flake8 como linter. Las elegí para este proyecto, porque la lectura deja la métrica de cobertura y las reglas de estilo a cargo de cada proyecto.

Cada evidencia debe quedar fechada y asociada al cambio que demuestra. La DoD define las condiciones de integración; cumplirlas requiere ejecutar los controles y conservar sus resultados.

Estos criterios retoman lo que vimos en la U01 sobre code review. Los criterios de aceptación técnica piden que el código compile, pase todos los tests y cumpla los estándares del proyecto. Además, antes de aprobar un Pull Request se exigen como mínimo pruebas, estilo, documentación y atomicidad, es decir, que el PR resuelva una sola cosa.

## Lista de control para cada Pull Request

| Criterio | Condición para integrar | Evidencia |
|---|---|---|
| 1 Integridad de compilación | Sin errores de compilación ni advertencias críticas pendientes. | Salida fechada de compileall y flake8. |
| 2 Pruebas automatizadas | El 100 % de las pruebas del componente finaliza correctamente. | Reporte y logs de la corrida sobre el mismo código. |
| 3 Cobertura mínima | Al menos el 80 % de las líneas ejecutables nuevas recorridas. | Comparación entre versiones y reporte de cobertura. |
| 4 Revisión por pares | Otra persona revisa y aprueba el cambio. | Observaciones, correcciones y aprobación en el PR. |
| 5 Gobernanza de estilo | Formatter y linter sin incumplimientos pendientes. | Salidas fechadas y configuración utilizada. |
| 6 Documentación técnica | Contratos, funciones complejas y esquemas actualizados. | Documentación modificada y revisada en el PR. |
