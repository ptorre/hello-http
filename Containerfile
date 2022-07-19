FROM python:3-slim

WORKDIR /app

COPY hello-http.py .

EXPOSE 5000

CMD [ "python", "./hello-http.py" ]
