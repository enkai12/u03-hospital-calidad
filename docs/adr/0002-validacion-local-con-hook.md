# ADR 0002: Validación local con un hook propio versionado

- **Estado:** Aceptado
- **Fecha:** 2026-10-21 (registra una decisión tomada el 2026-10-02, en el TP 3 de la U03)

## Contexto

La DoD exige formato (Black), linter (flake8) y pruebas en verde antes de integrar.
Correrlos a mano depende de la memoria de cada persona, y el error aparece tarde: en
la revisión o después del merge.

Un hook `pre-commit` de Git los corre antes de cada commit, pero tiene dos problemas
de distribución: Git no versiona `.git/hooks`, así que el hook no llega con el
`clone`, y cada persona tendría que copiarlo a mano.

Evaluamos tres formas de distribuirlo:

| Opción | A favor | En contra |
|---|---|---|
| **Husky** | Muy usado; se instala solo con `npm install` | Es una herramienta de Node: agrega `package.json` y `node_modules` a un proyecto Python sin una sola dependencia de JavaScript |
| **Framework `pre-commit`** (Python) | Estándar en Python; descarga y aísla cada herramienta | Una dependencia y un archivo de configuración más; las versiones de las herramientas se fijan en dos lugares (su configuración y `requirements-dev.txt`) |
| **Script propio en `hooks/` + `core.hooksPath`** | Sin dependencias; se lee en veinte líneas; usa el mismo `.venv` y las mismas versiones fijadas que el resto del proyecto | Hay que activarlo con un comando en cada copia |

## Decisión

El hook es un script POSIX en `hooks/pre-commit`, versionado con el resto del código,
que corre en orden Black (`--check`), flake8 y las pruebas, y aborta el commit si uno
falla. Cada copia lo activa con:

```bash
git config core.hooksPath hooks
```

El comando está en el [README](../../README.md) y en el
[CONTRIBUTING](../../CONTRIBUTING.md).

## Consecuencias

**Lo bueno**

- Los errores de estilo y las pruebas rotas se detectan en segundos, en la máquina de
  quien los produjo, antes de llegar al repositorio compartido.
- El hook se versiona: un cambio en los controles pasa por un PR como cualquier
  código.

**Lo malo**

- Se puede saltar (`git commit --no-verify`) o no activar. El hook es la primera línea
  de defensa, no la última: la validación que no se puede saltar es la del servidor,
  sobre cada PR (pipeline de CI y protección de `main`).
- Revisa la carpeta de trabajo y no solo lo preparado para el commit, así que en casos
  raros puede aprobar algo que no es exactamente lo que se commitea. La CI vuelve a
  validar sobre el commit real.
