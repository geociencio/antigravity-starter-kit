# Guía Rápida: Framework Agéntico Antigravity

**Versión**: 2.0 (Generic Template)

---

## 📋 Resumen Ejecutivo

El framework **Antigravity** proporciona un sistema base de **skills** y **workflows** integrados que automatizan la invocación de agentes especializados y conocimiento contextual para cualquier proyecto de desarrollo.

---

## 🛠️ Skills Base Disponibles

| Skill | Descripción | Cuándo Usar |
|:------|:------------|:------------|
| [commit-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/commit-standards/SKILL.md) | Estándares de Conventional Commits | Al crear commits, validar mensajes |
| [coding-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/coding-standards/SKILL.md) | Formateo, tipado y estilo de código | Al escribir o refactorizar código |
| [qa-standards](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/qa-standards/SKILL.md) | Testing, CI/CD y Mocks | Al escribir/ejecutar tests |
| [project-context](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/project-context/SKILL.md) | Arquitectura y propósito del proyecto | Al iniciar tareas o necesitar contexto global |
| [release-management](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/skills/release-management/SKILL.md) | Proceso de release y Semantic Versioning | Al preparar releases, versionar |

> 💡 **Nota:** Puedes añadir tus propias skills de dominio en la carpeta `.agent/skills/`.

---

## 🔄 Workflows Base Disponibles

### Desarrollo Diario

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/inicia-sesion](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/inicia-sesion.md) | Tech Lead | project-context, qa-standards | Iniciar sesión con contexto sincronizado |
| [/crea-commit](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/crea-commit.md) | QA Engineer | qa-standards, commit-standards | Commit con validación de calidad |
| [/run-tests](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/run-tests.md) | QA Engineer | qa-standards | Ejecutar tests con interpretación inteligente |
| [/cierra-sesion](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/cierra-sesion.md) | QA Engineer | qa-standards, commit-standards | Cerrar sesión con logs actualizados |

### Refactorización y Calidad

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/refactor-code](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/refactor-code.md) | Tech Lead | coding-standards, project-context | Refactorizar código con validación de complejidad |

### Release Management

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/release-project](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/workflows/release-plugin.md) | QA Engineer | release-management, qa-standards, commit-standards | Release completo del proyecto |

---

## 🎯 Casos de Uso Comunes

### Iniciar Sesión de Desarrollo
```bash
/inicia-sesion
```
**Qué hace**:
- Activa "Tech Lead Agent"
- Carga skills: project-context, qa-standards
- Sincroniza contexto base.
- Ejecuta los tests configurados en el proyecto.
- Valida métricas de calidad iniciales.

### Crear Commit con Validación
```bash
/crea-commit
```
**Qué hace**:
- Activa "QA Engineer Agent"
- Carga skills: qa-standards, commit-standards
- Ejecuta linters/formatters.
- Genera 2-3 opciones de mensaje siguiendo Conventional Commits.
- Valida formato y scope.

### Refactorizar Código Complejo
```bash
/refactor-code
```
**Qué hace**:
- Activa "Tech Lead Agent"
- Carga skills: coding-standards, project-context
- Analiza la complejidad del código.
- Aplica principios de diseño definidos en project-context.
- Valida que la complejidad bajó y los tests pasan.

---

## 🔧 Extensibilidad y Personalización

Para adaptar este framework a tu proyecto:

### Añadir Nueva Skill
1. Crear directorio: `.agent/skills/[nombre-skill]/`
2. Crear `SKILL.md` con frontmatter YAML:
   ```yaml
   ---
   name: nombre-skill
   description: Descripción breve
   trigger: cuándo auto-invocar
   scope: root
   ---
   ```
3. Ejecutar `skill_sync.py` (si está configurado) o actualizar `AGENTS.md` manualmente.

### Añadir Nuevo Workflow
1. Crear archivo: `.agent/workflows/[nombre].md`
2. Añadir frontmatter YAML:
   ```yaml
   ---
   description: Descripción del workflow
   agent: Tech Lead | QA Engineer
   skills: [skill1, skill2]
   validation: |
     - Checkpoint 1
     - Checkpoint 2
   ---
   ```
3. Añadir anotaciones `🤖 **Agent Action**` en pasos clave.

---

## 📚 Referencias

- [AGENTS.md](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/AGENTS.md) - Definición completa de agentes y matriz de skills.

---

**Última actualización**: 2026-03-01
**Versión del sistema**: 2.0 (Agnostic Template)

