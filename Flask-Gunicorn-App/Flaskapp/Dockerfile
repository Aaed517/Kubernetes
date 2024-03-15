FROM python:3

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install -r requirments.txt

CMD ["gunicorn" , "--bind","0.0.0.0:8000", "wsgi:app"]