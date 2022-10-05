FROM python:3.8-slim-buster

WORKDIR /reverse_polish_notation_flask

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app ./app
COPY migrations ./migrations
COPY wsgi.py .

COPY entry_point.sh .
RUN chmod +x entry_point.sh

ENV FLASK_ENV=dev

EXPOSE 5000

ENTRYPOINT ["./entry_point.sh"]
