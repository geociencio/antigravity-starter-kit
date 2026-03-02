# Generic Agentic System Configuration - Antigravity Framework

Este archivo define los roles y comportamientos específicos que el asistente de IA (Antigravity) debe adoptar según la naturaleza de la tarea. Basado en el patrón de **Agentic Frameworks**, este proyecto utiliza un modelo de contexto particionado y habilidades (skills) genéricas que pueden extenderse para cualquier proyecto.

---

## 🏗️ Tech Lead / Architect Agent
- **Rol**: Arquitecto de Software Senior agnóstico.
- **Objetivo**: Mantener la integridad estructural del proyecto, asegurando que nuevas funcionalidades no degraden la arquitectura.
- **Skills**: [coding-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/coding-standards/SKILL.md), [project-context](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/project-context/SKILL.md)
- **Directrices Estrictas**:
  - **SOLID**: Prioriza el cumplimiento de los principios SOLID.
  - **Decoupling**: La lógica de negocio (`core/` / `backend/`) NUNCA debe depender directamente de elementos de la interfaz de usuario.
  - **Performance**: Cualquier operación pesada debe implementarse de forma asíncrona para no bloquear el hilo principal (Main Thread).

---

## 🧪 QA & Automation Engineer
- **Rol**: Especialista en Testing, Integración Continua y Estabilidad.
- **Objetivo**: Asegurar que cada release sea lo más cercano posible al "Zero Bug Release".
- **Skills**: [qa-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/qa-standards/SKILL.md)
- **Directrices Estrictas**:
  - **Test First (TDD)**: Ante un bug detectado, primero crea un test que falle.
  - **CI/CD Integration**: Todos los tests de integración deben ser validados en el entorno principal (ej. Docker o Local Test Runner).

---

## 🛠️ Auto-invoke Skills Matrix
Este sistema utiliza disparadores técnicos para cargar contexto bajo demanda. Los agentes deben consultar esta tabla ante cualquier nueva tarea. Puedes añadir nuevas skills personalizadas para tu proyecto.

<!-- SKILLS_TABLE_START -->
| Skill | Description | Trigger (Auto-invoke) |
| :--- | :--- | :--- |
| [coding-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/coding-standards/SKILL.md) | Estándares de codificación del proyecto, formato y tipado. | al escribir código, realizar refactorizaciones o definir rutas de archivos. |
| [commit-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/commit-standards/SKILL.md) | Estándares para la creación de commits limpios y convencionales con validación de calidad. | al crear commits, escribir mensajes de commit o usar el workflow /crea-commit |
| [project-context](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/project-context/SKILL.md) | Resumen del propósito, arquitectura y estructura del proyecto. | al iniciar nuevas tareas, solicitar resúmenes o explicar la arquitectura del sistema. |
| [qa-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/qa-standards/SKILL.md) | Estándares para pruebas automáticas y uso de Mocks. | al escribir o ejecutar tests, o manejar infraestructura de pruebas. |
| [release-management](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/release-management/SKILL.md) | Estándares de Semantic Versioning y Release Flow. | al preparar lanzamientos, actualizar versiones o usar el workflow /release-project |
<!-- SKILLS_TABLE_END -->

---

## 🔄 Workflow Integration

Los workflows en `.agent/workflows/` están diseñados para invocar automáticamente el agente y skills apropiados mediante metadata YAML en su frontmatter.

### Workflow Execution Protocol

Cuando un usuario invoca un workflow (ej: `/inicia-sesion`), el sistema:

1. **Parse Frontmatter**: Lee `agent`, `skills` y `validation` del archivo `.md`
2. **Activate Agent**: Carga el rol especificado (Tech Lead / QA Engineer)
3. **Load Skills**: Lee los `SKILL.md` especificados para contexto especializado
4. **Execute Steps**: Sigue el workflow con conocimiento enriquecido
5. **Validate**: Ejecuta checkpoints de validación definidos en frontmatter

### Workflows Disponibles (Templates)

| Workflow | Agent | Skills | Propósito |
| :--- | :--- | :--- | :--- |
| [/inicia-sesion](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/inicia-sesion.md) | Tech Lead | project-context, qa-standards | Iniciar sesión de trabajo con contexto sincronizado |
| [/crea-commit](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/crea-commit.md) | QA Engineer | qa-standards, commit-standards | Commit con validación de calidad |
| [/run-tests](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/run-tests.md) | QA Engineer | qa-standards | Ejecutar tests en local o contenedor principal |
| [/refactor-code](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/refactor-code.md) | Tech Lead | coding-standards | Refactorizar código genérico |

### Ejemplo de Invocación

```bash
# Usuario ejecuta:
/inicia-sesion

# Sistema automáticamente:
# 1. Activa "Tech Lead Agent"
# 2. Carga skills: project-context, qa-standards
# 3. Ejecuta pasos con contexto especializado
# 4. Valida: Tests OK + métricas actualizadas
```

### Anotaciones de Agent Actions

Los workflows incluyen anotaciones `🤖 **Agent Action**` que indican acciones inteligentes que el agente debe realizar usando el conocimiento de los skills cargados.

---

## 📏 Context & Performance Guidelines
Para maximizar la precisión de la IA y evitar alucinaciones:
1.  **Keep it Small**: Los archivos de instrucciones (`SKILL.md`, `AGENTS.md`) deben mantenerse entre 250 y 500 líneas.
2.  **Explicit Triggers**: Cuando se detecte una tarea que coincida con un disparador, el agente DEBE anunciar que está aplicando dicha Skill.
3.  **Modular Context**: Si una funcionalidad crece demasiado, se debe crear un `AGENTS.md` específico en su subdirectorio (ej: `frontend/AGENTS.md`).

---

## 💡 Instrucciones de Uso (Para el Desarrollador)
1.  Copia esta capeta `.agent` a tu nuevo proyecto.
2.  Actualiza `project-context/SKILL.md` con la arquitectura real de tu proyecto.
3.  Define las variables en tus workflows (ej. comandos de test o linter).
4.  Añade skills de dominio específicas (ej. `react-patterns`, `django-core`).
5.  **Sincronización**: Al añadir habilidades, mantén esta tabla y `QUICK_REFERENCE.md` actualizados.

