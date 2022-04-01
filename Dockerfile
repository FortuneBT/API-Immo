FROM python:3.8.10
RUN mkdir /app
RUN mkdir /app/code
COPY . /app/code/
WORKDIR /app/code/
RUN pip install requirements.txt
CMD ["python", "app.py"]

