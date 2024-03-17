FROM python:3

RUN mkdir /app 

WORKDIR /app
RUN  mkdir templates

COPY ["app.py", "db_create.py", "requirments.txt", "wsgi.py", "./"]

RUN apt update && \
    apt install -y libpq-dev gcc python3-dev && \
    pip install -r requirments.txt

WORKDIR /app/templates
COPY ["/templates","./"]

WORKDIR /app

CMD ["gunicorn" , "--bind","0.0.0.0:8000", "wsgi:app"]