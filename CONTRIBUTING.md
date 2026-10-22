# Cómo contribuir al Hospital Central

Esta guía es para quien va a modificar el proyecto. Antes de escribir código, leé
también la [Definition of Done](docs/definition-of-done.md): un cambio que no la
cumple no se integra.

## 1. Preparar el entorno

Necesitás Python 3.14 o posterior y Git.

> **Aviso transitorio.** Mientras los PR #2, #4 y #6 sigan abiertos, `main` todavía no
> trae `requirements-dev.txt` ni `hooks/`: clonás la rama que los contiene con
> `-b docs/3-estandares-de-colaboracion`. Cuando se integren, alcanza con el clon
> normal y este aviso se borra.

```bash
git clone -b docs/3-estandares-de-colaboracion git@github.com:enkai12/u03-hospital-calidad.git
cd u03-hospital-calidad
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
git config core.hooksPath hooks
```

El último comando activa el hook `hooks/pre-commit` en tu copia. Git no versiona la
carpeta `.git/hooks`, por eso el hook vive en `hooks/` y cada copia lo activa con ese
comando ([ADR 0002](docs/adr/0002-validacion-local-con-hook.md)).

Para comprobar que todo funciona:

```bash
sh hooks/pre-commit
```

Tiene que terminar con «Controles locales aprobados.».

## 2. Estilo de código

| Regla | Herramienta | Configuración |
|---|---|---|
| Formato | Black | Por defecto; líneas de hasta 88 caracteres |
| Errores y malas prácticas | flake8 | `setup.cfg`: `max-line-length = 88`, ignora E203 para no chocar con Black |
| Nombres | — | `snake_case` para funciones y variables, `PascalCase` para clases, constantes en mayúsculas |
| Idioma | — | Código y mensajes al usuario en castellano, como el resto del proyecto |

No discutas estilo en la revisión: si Black y flake8 aprueban, el estilo está bien.

## 3. Flujo de Git

Usamos **GitHub Flow** ([ADR 0001](docs/adr/0001-estrategia-de-branching.md)):

1. Todo trabajo empieza en un **issue**. Si es un defecto, usá la plantilla «Reporte
   de defecto». Ponele una [etiqueta](docs/labels.md).
2. Creá una rama desde `main` con el formato `tipo/N-descripcion-corta`:

   | Tipo | Para qué | Ejemplo |
   |---|---|---|
   | `feature/` | Funcionalidad nueva | `feature/7-exportar-turnos` |
   | `fix/` | Corrección de un defecto | `fix/8-sufijo-urgente-duplicado` |
   | `refactor/` | Cambio interno sin cambiar el comportamiento | `refactor/1-complejidad-procesar` |
   | `docs/` | Solo documentación | `docs/3-estandares-de-colaboracion` |
   | `ci/` | Pipeline y automatización | `ci/5-pipeline-ci-cd` |

   `N` es el número del issue.
3. Commits chicos y con una sola responsabilidad. El mensaje va en primera persona y
   en presente, y dice qué cambia: «Simplifico los turnos y automatizo los
   controles». Si un commit mezcla dos cosas, separalo con `git add -p`.
4. Antes de abrir el PR, ordená tus commits locales (`git rebase -i`). Una vez que
   subiste la rama, no reescribas su historia salvo que nadie más la use.
5. Abrí el Pull Request contra `main`. La plantilla te pide lo necesario.

## 4. Requisitos del Pull Request

Un PR se integra cuando cumple **todo** esto:

- [ ] Está vinculado a su issue con `Closes #N`.
- [ ] Resuelve **una sola cosa**. Si tocaste dos temas, son dos PR.
- [ ] El pipeline de CI está en verde: formato, linter, pruebas, cobertura y
      auditoría de dependencias.
- [ ] Las pruebas pasan al 100 % y cubren al menos el **80 % de las líneas
      ejecutables nuevas** (criterios 2 y 3 de la DoD).
- [ ] La documentación afectada está actualizada en el mismo PR (criterio 6).
- [ ] **Otra persona** lo revisó y lo aprobó (criterio 4). La autorrevisión no
      alcanza.

Se integra con **Squash and Merge**: cada PR queda como un único commit en `main`,
con el título del PR como mensaje. Después se borra la rama.

## 5. Cómo revisar

Quien revisa no busca errores de formato (eso ya lo hizo la CI). Busca:

- **Legibilidad:** ¿se entiende sin que el autor lo explique?
- **Diseño:** ¿hay lógica duplicada (DRY)? ¿cada función tiene una sola
  responsabilidad (SOLID)?
- **Pruebas:** ¿prueban el comportamiento nuevo o solo suben el porcentaje?
- **Seguridad:** ¿se exponen datos de pacientes en mensajes o logs?

Los comentarios proponen; no ordenan. Si una discusión se repite, se registra la
decisión en un [ADR](docs/adr/).

## 6. Decisiones de arquitectura

Las decisiones que afectan a todo el proyecto se registran en `docs/adr/` con el
formato de [ADR 0001](docs/adr/0001-estrategia-de-branching.md): contexto, decisión,
estado y consecuencias. Un ADR aceptado no se edita; si la decisión cambia, se
escribe uno nuevo que lo reemplaza.
