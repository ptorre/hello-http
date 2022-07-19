FROM registry.access.redhat.com/ubi9/python-312:latest

WORKDIR /app

COPY hello-http.py .

EXPOSE 5000

CMD [ "python", "./hello-http.py" ]
