FROM python:3.8.10
RUN mkdir /app
RUN mkdir /app/code
COPY . /app/code/
WORKDIR /app/code/
CMD ["python", "hello_world.py"]

