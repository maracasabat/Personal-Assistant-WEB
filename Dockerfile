FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update \
  && apt-get install -y build-essential curl \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && chown python:python -R /app

USER python

COPY --chown=python:python requirements*.txt ./

RUN pip install -r requirements.txt

ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python . .

WORKDIR /app

RUN SECRET_KEY=nothing python assistant/manage.py tailwind install --no-input;
RUN SECRET_KEY=nothing python assistant/manage.py tailwind build --no-input;
RUN SECRET_KEY=nothing python assistant/manage.py collectstatic --no-input;

EXPOSE 8000

CMD ["python", "assistant/manage.py", "runserver", "0.0.0.0:8000"]