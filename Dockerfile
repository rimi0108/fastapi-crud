FROM python:3.7

COPY ./app /app
WORKDIR /app

ADD requirements.txt . 
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]