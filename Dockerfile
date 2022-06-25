FROM python:3.9-slim-bullseye

WORKDIR app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# TODO: Change model download to URL
COPY . .

ENV FLASK_APP=predictor

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5013" ]