
# Imagen base de Python
FROM python:3.13-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:0.11.16 /uv /usr/local/bin/uv

# Configurar el entorno
ENV UV_NO_CACHE=1
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copiar dependencias
COPY pyproject.toml uv.lock ./

# Instalar solo las dependencias del servicio
RUN uv sync --locked --only-group servicio --no-install-project

# Copiar el código fuente
COPY src/ ./src/

# Incluir el modelo entrenado en la imagen
COPY models/ ./models/

# Crear un usuario sin privilegios
RUN useradd --system --create-home appuser \
    && chown -R appuser:appuser /app

USER appuser

# Comprobar que la API responde
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=3)" || exit 1

# Exponer puertos de FastAPI y Streamlit
EXPOSE 8000 8501

# Iniciar FastAPI y Streamlit
CMD ["bash", "-c", "uvicorn src.aguaapr.main:app --host 0.0.0.0 --port 8000 & streamlit run src/aguaapr/ui.py --server.port 8501 --server.address 0.0.0.0 --server.headless true --browser.gatherUsageStats false & wait -n"]
