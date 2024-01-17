FROM python:3.11

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

WORKDIR ../api

ENV PYTHONPATH ..

CMD ["python", "main.py"]
