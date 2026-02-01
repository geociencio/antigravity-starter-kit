# BOOTSTRAP: Cómo dar vida a tu proyecto

Sigue estos pasos una vez hayas generado tu repositorio desde este template:

## 1. Personalización con Bootstrap
Ejecuta el script de inicio para configurar el nombre de tu proyecto y el entorno automáticamente:
```bash
python bootstrap.py
```
El script reemplazará los placeholders en `pyproject.toml` y `README.md`, e inicializará el entorno con `uv sync`.

## 2. Configuración de Agentes
Edita `scaffold/AGENTS.md` para definir quiénes son los colaboradores (humanos e IA) y qué skills tienen asignados.

## 3. Primer Inicio de Sesión
Ejecuta el workflow de inicio para que el agente entienda el contexto:
```bash
/inicia-sesion
```

## 4. Estándares de Codificación
Copia `scaffold/skills/coding-standards.md` a tu directorio de trabajo real si deseas aplicar reglas de tipado y docstrings desde el día 1.

---
> [!IMPORTANT]
> Recuerda que el framework es **Local-First**. Toda la inteligencia reside en tu repositorio.
