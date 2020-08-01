#Dockerfile

FROM python

WORKDIR /app

COPY . /app

RUN python -m pip install -r requirements.txt

# default Flask port
EXPOSE 5000

CMD ["mesa", "runserver", "./wolf_sheep"]
