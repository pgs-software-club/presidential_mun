FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh","-c","flask db upgrade","gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "server:app"]