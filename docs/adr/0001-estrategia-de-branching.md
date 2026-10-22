# ADR 0001: GitHub Flow con Squash and Merge

- **Estado:** Aceptado
- **Fecha:** 2026-10-21

## Contexto

El Hospital Central es un proyecto chico: un módulo de turnos (`hospital/turnos.py`),
diez pruebas y una persona que escribe el código, con revisión de otra persona antes de
integrar (criterio 4 de la [DoD](../definition-of-done.md)). No hay versiones
instaladas en clientes que haya que mantener en paralelo ni fechas de lanzamiento
fijas: lo que está en `main` es la única versión viva.

Hasta ahora el trabajo se hizo en una rama por tarea (`refactor/1-complejidad-procesar`)
con un Pull Request vinculado a su issue, pero sin una regla escrita sobre qué
estrategia de ramas seguir ni cómo integrar.

Evaluamos tres opciones:

| Opción | A favor | En contra |
|---|---|---|
| **GitFlow** | Control fino de cada versión; soporta versiones viejas | `develop`, `release/*` y `hotfix/*` son ceremonia sin beneficio para un equipo de una o dos personas sin releases programados; ramas largas que acumulan deuda de integración |
| **GitHub Flow** | Una sola rama permanente; cada cambio pasa por un PR revisado; encaja con la DoD | Exige que `main` esté siempre en condiciones y que los PR se revisen rápido |
| **Trunk-based** | Integración diaria, conflictos mínimos | Exige ramas de horas, pruebas automáticas que respalden cada integración y feature flags; hoy el Hospital tiene pocas pruebas y recién arma su CI, así que le conviene llegar a eso de a poco |

## Decisión

Usamos **GitHub Flow**:

- `main` es la única rama permanente y siempre tiene que pasar los controles.
- Cada cambio nace de un issue, se hace en una rama corta `tipo/N-descripcion` y entra
  por un Pull Request revisado.
- Los PR se integran con **Squash and Merge**: cada PR queda como un único commit en
  `main`, con el título del PR como mensaje.

## Consecuencias

**Lo bueno**

- El historial de `main` se lee como una lista de cambios terminados, uno por PR, cada
  uno enlazado a su issue y a su revisión.
- Las ramas viven poco, así que la deuda de integración y los conflictos son chicos.
- La validación automática de cada PR (pipeline de CI) reemplaza la fase de prueba de
  una rama `release`.

**Lo malo**

- Con squash, los commits intermedios de cada rama no quedan en `main`. Siguen
  visibles en el PR, que es donde hay que buscarlos.
- Si algún día hubiera que mantener una versión vieja instalada en un cliente, este
  modelo no alcanza. Se reemplazaría este ADR por uno que adopte ramas de versión
  (GitLab Flow o GitFlow).
- Depende de que la revisión sea rápida: un PR esperando días frena todo.
