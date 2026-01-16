FROM python:3.12

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app/version-api.py /code/version-api.py

CMD ["fastapi", "run", "version-api.py", "--port", "8080"]
