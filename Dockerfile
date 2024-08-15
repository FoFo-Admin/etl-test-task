FROM python:3.12

WORKDIR /app

COPY main.py /app
COPY application /app
COPY requirements.txt /app
COPY generated.csv /app
COPY config.ini /app

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]