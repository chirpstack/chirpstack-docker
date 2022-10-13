FROM python:3.7-slim-buster
COPY requirements.txt ./

RUN apt-get update && apt-get install -y cmake
RUN pip install -r ./requirements.txt

COPY app.py ./

CMD ["python", "app.py"]

RUN adduser --system forwarder
USER forwarder