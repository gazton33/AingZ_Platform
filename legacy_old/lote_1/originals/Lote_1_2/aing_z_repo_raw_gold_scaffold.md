# Estructura de Directorios y Archivos — Scaffold Inicial RAW GOLD

> Esta estructura puede ser generada manualmente o por script, y sirve como primer paso de la migración para testear la cobertura y modularidad antes de poblar los contenidos con plantillas y archivos definitivos.

```plaintext
AingZ_Repo_RAW_GOLD/
│   README.md
│   changelog.md
│   master_plan_aingz_infrastructure.md
│   .gitignore
│
├── knowledge/
│   └── knowledge_demo.md
│
├── matrices/
│   └── matriz_demo.md
│
├── workflows/
│   └── workflow_demo.md
│
├── scripts/
│   ├── script_demo.py
│   └── README.md
│
├── logs/
│   └── logs_demo.log
│
├── doc/
│   ├── croquis_demo.md
│   ├── imagen_demo.png
│   └── README.md
│
├── config/
│   ├── config_demo.json
│   └── .env.example
│
├── backups/
│   └── backup_demo.zip
│
├── notebooks/
│   └── notebook_demo.ipynb
│
└── onboarding/
    ├── checklist_coverage.md
    └── template_demo.md
```

---

## Detalles de codificación y naming
- **README.md** en raíz y en cada carpeta principal.
- Todos los archivos demo pueden ser vacíos, con un simple placeholder de nombre, fecha, propósito.
- `.env.example` nunca debe contener credenciales reales.
- `onboarding/` para plantillas de checklist y templates base de rápido acceso.
- **Convención**: usar sufijos `_demo`, `_example`, `_template` hasta tener los archivos reales definitivos.

---

## Próximo paso
- Generar manualmente o vía script este scaffold en local.
- Confirmar coverage y acceso desde el entorno de trabajo.
- Iterar completando con templates y archivos reales.

