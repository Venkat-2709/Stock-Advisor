FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml README.md ./
COPY app/ ./app/

RUN uv pip install --system .

WORKDIR /app/app

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
