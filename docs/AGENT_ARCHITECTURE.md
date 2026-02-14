# 🧠 Antigravity Agentic Architecture (Gen 3)

Antigravity es un **sistema operativo para la colaboración Humano-IA**. La Generación 3 introduce la **Capa de Consciencia**, permitiendo que los agentes aprendan, se autocritiquen y midan su propia efectividad.

## 🏗️ Los Pilares del Sistema (Gen 3)

### 1. Workflows (Procedimientos)
Guías deterministas en `.agent/workflows/` (ej: `/inicia-sesion`, `/ia-critic`).
- **Novedad**: Inclusión de pasos de auditoría automática.

### 2. Skills (Conocimiento)
Manuales expertos en `.agent/skills/`.
- **Novedad**: La skill `agentic-memory` permite la gestión autónoma del conocimiento del proyecto.

### 3. Memoria Semántica (Aprendizaje)
Ubicada en `.agent/memory/AGENT_LESSONS.md`.
- **Propósito**: Registro estructurado de lecciones, preferencias del usuario y patrones de error para evitar repeticiones.

### 4. Auditoría Proactiva (Autocrítica)
El rol **Agent Auditor** actúa como un filtro de calidad para cada plan propuesto, reduciendo el ruido y las alucinaciones.

### 5. Observabilidad (Métricas)
Tracking dinámico en `agent_metrics.json` para medir la efectividad, tasa de reintentos y estabilidad del sistema.

## 🔄 El Ciclo de Vida del Agente Gen 3

1.  **Contextualización**: Carga de historia y lecciones previas (`/inicia-sesion`).
2.  **Planificación**: Propuesta técnica basada en el estado actual.
3.  **Auditoría**: Validación del plan por el Agent Auditor (`/ia-critic`).
4.  **Ejecución**: Implementación con validación de estándares.
5.  **Capitalización**: Extracción de aprendizaje y cierre de sesión (`/cierra-sesion`).

---
*Antigravity: Evolución constante del desarrollo asistido por IA.*
