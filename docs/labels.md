# Matriz de etiquetas del Hospital Central

Elegí las cuatro categorías de la lectura de Semana 1 para clasificar las incidencias y las propuestas de cambio. La definición de cada categoría procede del material; su relación con los controles de la DoD es mi aplicación al proyecto.

| Etiqueta | Definición y uso | Justificación y relación con la DoD |
|---|---|---|
| bug | Fallo lógico o funcional confirmado que rompe un comportamiento esperado. | Se usa para registrar y corregir un defecto. Orienta la revisión de las pruebas que comprueban la corrección y de la cobertura del código modificado. |
| technical-debt | Refactorización, complejidad elevada o desvío de estilo que requiere corrección. | Distingue mejoras internas de nuevas funcionalidades. Orienta los controles de estilo, la revisión de complejidad y las pruebas que comprueban la conservación del comportamiento. |
| documentation | Actualización de contratos de APIs, diagramas de arquitectura o especificaciones técnicas. | Permite identificar la documentación que debe acompañar un cambio. Orienta la revisión de contratos y documentos para comprobar que describan la versión propuesta. |
| feature | Desarrollo de una nueva capacidad lógica del negocio. | Distingue una funcionalidad nueva de un defecto o una mejora interna. Orienta la revisión de sus pruebas, cobertura y documentación antes de integrar. |

La etiqueta permite saber qué tipo de trabajo se está revisando, pero no acredita que esté terminado. Todas las categorías deben cumplir la DoD completa en los criterios que correspondan al cambio. La comprobación se hace con pruebas, reportes, documentación y revisión; no con el nombre o el color de la etiqueta.

Fuente: Semana 1, sección 3.2 B, página 6.
