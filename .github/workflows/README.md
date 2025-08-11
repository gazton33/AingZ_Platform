# GitHub Workflows

Esta carpeta contiene workflows de automatización para AingZ.

## Acción compuesta `aingz_pr_action`

La acción localizada en `.github/actions/aingz_pr_action` encapsula la generación del token de la GitHub App, el checkout del repositorio y la creación del Pull Request.

### Uso básico

```yaml
jobs:
  ejemplo:
    runs-on: ubuntu-latest
    steps:
      - name: Ejecutar acción de PR
        uses: ./.github/actions/aingz_pr_action
        with:
          reason: motivo-del-cambio
          branch-prefix: prefijo
          commit-message: "AingZ Agent: motivo-del-cambio"
          pr-body: descripcion del PR
          script: |
            # comandos que modifican el repo
            python ops/scripts/mi_script.py
```

### Inputs

- `reason`: motivo utilizado en el título del PR.
- `branch-prefix`: prefijo de la rama `bot/aingz/<prefijo>-<run_id>`.
- `commit-message`: mensaje del commit.
- `pr-body` (opcional): cuerpo del PR.
- `script` (opcional): comandos a ejecutar tras el checkout.

La acción realiza automáticamente:
1. Generar token con `tibdex/github-app-token@v2`.
2. `actions/checkout@v4` con ese token.
3. Ejecutar el script indicado.
4. Crear el PR vía `peter-evans/create-pull-request@v6`.
