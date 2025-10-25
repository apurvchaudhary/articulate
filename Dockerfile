FROM python:3.12.8-slim

WORKDIR /app/articulate

RUN apt-get update && apt-get install -y netcat-openbsd
RUN apt-get update && apt-get install -y build-essential libmariadb-dev libmariadb-dev-compat pkg-config python3-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . /app/articulate

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]