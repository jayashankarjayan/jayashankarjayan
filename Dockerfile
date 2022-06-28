FROM alpine:latest

RUN apk add python3

RUN python3 -m ensurepip

COPY application /home/application

WORKDIR /home/application

run pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "server.py"]

# eval $(minikube docker-env)