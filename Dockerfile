FROM python:3.8-slim as builder

COPY ./requirements.txt /src/requirements.txt
COPY ./src /src/src

WORKDIR "/src"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN pip install -r /src/requirements.txt

CMD ["python", "-m", "uvicorn", "--app-dir", "src", "app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "2"]