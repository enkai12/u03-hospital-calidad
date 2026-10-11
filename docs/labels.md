# Matriz de etiquetas del Hospital Central

Propongo cuatro etiquetas para clasificar los issues y los Pull Requests. Sirven para que, antes de integrar, se sepa qué tipo de trabajo se está revisando y en qué criterios de la DoD hay que poner más atención.

| Etiqueta | Definición | Qué controles orienta |
|---|---|---|
| bug | Fallo lógico o funcional confirmado que rompe un comportamiento esperado. | Las pruebas que comprueban la corrección y la cobertura del código modificado (criterios 2 y 3). |
| technical-debt | Refactorización, complejidad elevada o desvío de estilo que requiere corrección. | El estilo, la complejidad y las pruebas que muestran que el comportamiento se conserva (criterios 2, 4 y 5). |
| documentation | Actualización de contratos de APIs, diagramas de arquitectura o especificaciones técnicas. | Que la documentación describa la versión propuesta (criterio 6). |
| feature | Desarrollo de una nueva capacidad lógica del negocio. | Las pruebas, la cobertura y la documentación de lo nuevo (criterios 2, 3 y 6). |

La etiqueta technical-debt merece una aclaración. Agrupa la deuda técnica, es decir, los atajos que se toman para entregar más rápido, como copiar código o no escribir pruebas, y que después se pagan con tiempo extra cada vez que hay que agregar algo. Tenerla separada evita que esas mejoras internas se pierdan entre los defectos y las funcionalidades nuevas.

De todos modos, una etiqueta solo dice qué tipo de trabajo se está revisando, no que esté terminado: cualquier cambio, lleve la etiqueta que lleve, tiene que cumplir la DoD completa.
