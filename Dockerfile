FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

# CMD ["sh","-c","flask db upgrade","gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "server:app"]