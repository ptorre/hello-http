FROM docker.io/library/python:3.9.13-slim

WORKDIR /app

COPY hello-http.py .

EXPOSE 5000

CMD [ "python", "./hello-http.py" ]
