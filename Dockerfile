FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

WORKDIR /app/src
ENTRYPOINT ["python3"]
CMD ["app.py"]