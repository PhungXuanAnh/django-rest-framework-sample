FROM python:3.8.0

# Reference: https://stackoverflow.com/a/59812588/7639845
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver

COPY . /app

EXPOSE 8027

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8027"]
