FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY ./app/app.py .

ENV PYTHONUNBUFFERED 1

CMD [ "fastapi", "run", "app.py", "--port", "5000" ]
