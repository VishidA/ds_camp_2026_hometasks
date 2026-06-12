FROM python:3.10

RUN apt-get update && apt-get install -y libgl1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3"]
CMD ["main.py"]

