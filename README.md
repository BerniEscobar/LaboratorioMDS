# IA7202 - Laboratorio de Programación Científica para Ciencia de Datos

Repositorio del curso MDS7202, Facultad de Ciencias Físicas y Matemáticas, Universidad de Chile.

## Integrantes

| Nombre | GitHub |
|--------|--------|
| Bernardita Escobar | [GitHub](https://github.com/BerniEscobar) |
| Lucas Gálvez | [GitHub](https://github.com/LucasGalvez) |

## Estructura del repositorio

```text
.
├── .github/
│   ├── workflows/
│   │   └── lint.yml
│   └── pull_request_template.md
├── labs/
│   ├── lab_1/
│   └── ...
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

## Configuración del entorno

```bash
uv sync --locked --all-groups
uv run pre-commit install
```
