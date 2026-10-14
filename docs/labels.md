# Matriz de etiquetas del Hospital Central

Propongo seis etiquetas para clasificar los issues y los Pull Requests. Cinco dicen qué tipo de trabajo es y una dice en qué estado está, así que antes de integrar se sabe qué se está revisando, en qué criterios de la DoD hay que poner más atención y si todavía falta algo.

| Etiqueta | Definición | Qué controles orienta |
|---|---|---|
| bug | Fallo lógico o funcional confirmado que rompe un comportamiento esperado. | Las pruebas que comprueban la corrección y la cobertura del código modificado (criterios 2 y 3). |
| technical-debt | Refactorización, complejidad elevada o desvío de estilo que requiere corrección. | El estilo, la complejidad y las pruebas que muestran que el comportamiento se conserva (criterios 2, 4 y 5). |
| documentation | Actualización de contratos de APIs, diagramas de arquitectura o especificaciones técnicas. | Que la documentación describa la versión propuesta (criterio 6). |
| feature | Desarrollo de una nueva capacidad lógica del negocio. | Las pruebas, la cobertura y la documentación de lo nuevo (criterios 2, 3 y 6). |
| security | Vulnerabilidad del código o de una dependencia, o actualización de una biblioteca para corregirla. | El escaneo de dependencias y el análisis estático, además de las pruebas y la revisión (criterios 2 y 4). |
| needs-review | Estado: el cambio pasó los controles automáticos y espera la revisión y aprobación de otra persona. | Que nadie lo integre hasta que la aprobación quede registrada en el PR (criterio 4). Se saca cuando la revisión se aprueba. |

La etiqueta technical-debt merece una aclaración. Agrupa la deuda técnica, es decir, los atajos que se toman para entregar más rápido, como copiar código o no escribir pruebas, y que después se pagan con tiempo extra cada vez que hay que agregar algo. Tenerla separada evita que esas mejoras internas se pierdan entre los defectos y las funcionalidades nuevas.

Sumé dos etiquetas a las cuatro básicas. security separa los problemas de seguridad de los defectos comunes: una vulnerabilidad conocida que se deja sin corregir no es solo un error técnico, porque implementar así una aplicación puede generar responsabilidad. needs-review, en cambio, no describe el tipo de trabajo sino su estado: marca los cambios que ya pasaron los controles automáticos pero todavía esperan que otra persona los revise, que es el único criterio que no se puede comprobar con una herramienta.

De todos modos, una etiqueta solo dice qué tipo de trabajo se está revisando, no que esté terminado: cualquier cambio, lleve la etiqueta que lleve, tiene que cumplir la DoD completa.
