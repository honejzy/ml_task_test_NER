FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]
