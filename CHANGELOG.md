# Registro de cambios

Los cambios de cada versión, del más nuevo al más viejo. Las versiones siguen
[SemVer](https://semver.org/lang/es/): MAJOR rompe la compatibilidad, MINOR agrega de
forma compatible y PATCH corrige sin cambiar el uso.

## [1.0.1] - 2026-10-21

### Agregado
- Este registro de cambios, incluido en el paquete que publica cada Release.

### Sin cambios
- La aplicación (`hospital/`) es la misma de la 1.0.0.

## [1.0.0] - 2026-10-21

### Agregado
- Pipeline de CI: lint, pruebas con cobertura, auditoría de dependencias y build.
- Publicación por tag del artefacto validado y despliegue a staging y producción.
- Guía de contribución, plantilla de PR y ADR.

### Cambiado
- `TurnoManager.procesar` simplificado con cláusulas de guarda, con el mismo
  comportamiento.

### Seguridad
- `certifi` 2026.7.22 → 2026.10.19 (PYSEC-2026-4320) en las herramientas de desarrollo.
