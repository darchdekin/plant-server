FROM python:3.10

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . plants
WORKDIR /plants

RUN python3 manage.py loaddata plants_data.json

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "SampleApp.wsgi:application"]