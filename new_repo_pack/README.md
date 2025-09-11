# New Repo Pack

Este paquete contiene la estructura mínima y el ruleset integrado (v2) para recrear la arquitectura AingZ en un nuevo repositorio.

## Uso

1. Copiar el contenido de `new_repo_pack/` al directorio raíz del repositorio nuevo.
2. Inicializar git:

   ```bash
   git init
   ```

3. Ajustar archivos según necesidad.
4. Registrar la versión inicial:

   ```bash
   git add .
   git commit -m "feat: inicializar arquitectura AingZ y paquete ruleset full v2"
   ```

El folder `ruleset_full_v2/` incluye todas las reglas y contexto necesarios. Los directorios `main/`, `log/` y `scripts/` se proveen con archivos `.gitkeep` para preservar la estructura base.
