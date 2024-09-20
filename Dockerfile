FROM python:3.8

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt
COPY . .

# Exponer el puerto en el que Flask corre
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
