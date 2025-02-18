FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

COPY data/ /app/data/
COPY datagen.py main.py task_manager.py /app/

RUN uv pip install fastapi uvicorn requests --system

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]