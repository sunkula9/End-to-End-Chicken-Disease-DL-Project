FROM python:3.12.7-slim-buster

RUN apt udpate -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3","app.py" ]