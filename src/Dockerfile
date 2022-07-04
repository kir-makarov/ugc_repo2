FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV HOME=/src

WORKDIR $HOME

COPY . $HOME
EXPOSE 5000
# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
CMD uvicorn main:app --host 0.0.0.0 --port 5000