FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN ls -la

CMD ["python", "app.py"]
