FROM python:latest
RUN apt-get update -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ADD ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
