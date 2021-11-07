FROM python:3.6.9-alpine
WORKDIR /code

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2
EXPOSE 8082
COPY . .
CMD [ "python", "/code/src/router/router.py" ]