FROM python:3.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN groupadd -g 1000 -r user \
    && useradd -m -u 1000 -s /bin/bash -g user user

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

RUN chown -R user:user /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /backend

RUN mkdir -p /backend/db /backend/static \
    && chown -R user:user /backend

RUN python manage.py collectstatic --noinput

USER user

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
