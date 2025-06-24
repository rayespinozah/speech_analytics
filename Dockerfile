FROM python:3.9-slim

# UPDATE APT-GET
RUN apt-get update

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 5000

CMD [ "gunicorn","-w","4","-b",":5000","app:app"]