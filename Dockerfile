FROM python:3.8.0

# Reference: https://stackoverflow.com/a/59812588/7639845
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements/* /app/requirements/
ARG BUILD_ENV=BUILD_ENV_this_value_must_be_pass_during_build_time
RUN pip install -r requirements/${BUILD_ENV}.txt --upgrade
# RUN echo ${BUILD_ENV}

COPY ./source /app

EXPOSE 8027

ARG IS_BUILDING_APP
RUN if [ -z "$IS_BUILDING_APP" ] ; then DJANGO_SETTINGS_MODULE=main.settings.${BUILD_ENV} python3 manage.py collectstatic --noinput && rm -rf /app/logs/* ; fi

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8027"]
