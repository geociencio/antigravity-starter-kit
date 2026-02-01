# Próximos Pasos (Next Steps) - 2026-02-01

## Estado Actual
- **CORREGIDO**: Regresión de `QgsDistanceArea` en `preview_service.py` resuelta.
- El proyecto `sec_interp` tiene ahora una infraestructura agentica alineada con los estándares 2025.
- La suite de tests (206) está operativa en Docker (`make docker-test`).

## Tareas Pendientes
- [x] Implementar un ejemplo de Skill para Data Science real en el scaffold.
- [ ] Publicar el Framework como una guía independiente en un repositorio template (Opcional).
- [ ] Abordar la alta complejidad ciclomática (CC 62) en `export_service.py` y `drillhole_service.py`.
- El script `skill_sync.py` debe ser verificado en entornos Windows si se pretende una compatibilidad total fuera de Linux.
