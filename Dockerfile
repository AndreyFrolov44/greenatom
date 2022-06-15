FROM python:3.9

WORKDIR /app

RUN apt-get -qq update

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

# RUN alembic upgrade head

EXPOSE 8000

# CMD ["alembic", "upgrade", "head"]
# CMD ["uvicorn", "main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]