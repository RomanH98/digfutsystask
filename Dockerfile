FROM python:3.10
LABEL authors="rhalimov"

WORKDIR /usr/src/app
RUN cd /usr/src/app
COPY ./req.docker.txt ./
RUN pip install  -r req.docker.txt


COPY ./ ./


CMD ["python", "runner.py"]