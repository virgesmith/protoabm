#Dockerfile

FROM python

WORKDIR /app

COPY . /app

RUN python -m pip install -r requirements.txt

# default mesa port
EXPOSE 8521

CMD ["mesa", "runserver", "./conways_game_of_life"]
