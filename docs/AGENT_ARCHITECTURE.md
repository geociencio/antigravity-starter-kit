# 🧠 Antigravity Agentic Architecture

Antigravity no es solo un conjunto de archivos; es un **sistema operativo para la colaboración Humano-IA**. Esta arquitectura permite que un agente de IA entienda el contexto del proyecto, ejecute tareas complejas y mantenga la calidad técnica de forma autónoma pero supervisada.

## 🏗️ Los Tres Pilares

### 1. Workflows (Flujos de Trabajo)
Ubicados en `.agent/workflows/`, son guías deterministas que el agente DEBE seguir para tareas críticas.
- **Propósito**: Asegurar repetibilidad y cumplimiento de estándares (ej: `/crea-commit`).
- **Formato**: Markdown con metadatos YAML que describen cuándo y cómo ejecutar el flujo.

### 2. Skills (Habilidades Especializadas)
Ubicados en `.agent/skills/` y `scaffold/skills/`, contienen el "conocimiento profundo" sobre dominios específicos.
- **Propósito**: Instruir al agente sobre cómo manejar datos, UI, o lógica de negocio (ej: `data-science`, `qgis-core`).
- **Componentes**: Prompting estructurado, scripts de validación y ejemplos de referencia.

### 3. Autoconsciencia y Memoria
El sistema utiliza archivos en `.agent/memory/` y metadatos continuos para saber:
- Quiénes son los colaboradores.
- Qué se ha hecho en la sesión actual.
- Qué estándares de codificación están activos.

## 🔄 Ciclo de Vida Local-First

1. **Bootstrap**: El proyecto nace con un ADN configurado (`bootstrap.py`).
2. **Sincronización**: Al iniciar, el agente lee el contexto (`/inicia-sesion`).
3. **Ejecución**: El agente utiliza sus Skills para proponer cambios y Workflows para validarlos.
4. **Persistencia**: Todo el conocimiento generado (planes, logs, evolución de la arquitectura) se queda dentro del repositorio Git.

## 🚀 Por qué es "Gen 2"

La Generación 2 se enfoca en la **personalización instantánea**. Al usar placeholders (`{{PROJECT_NAME}}`) y scripts de validación de entorno, el framework reduce el tiempo desde la idea hasta el primer commit de 15 minutos a menos de 1 minuto, garantizando que el entorno está listo para la IA.

---
*Antigravity: Software que no se siente pesado.*
