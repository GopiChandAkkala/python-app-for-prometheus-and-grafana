FROM python:3.8-slim

WORKDIR /

COPY . /

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python3","/app/app.py"]
