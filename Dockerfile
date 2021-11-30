FROM arm32v7/python:3.9-buster

WORKDIR /discord-bot

COPY . . 

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "discord-gis-bot.py"]