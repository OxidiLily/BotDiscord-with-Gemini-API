FROM python:3.12-alpine

WORKDIR /BotDiscord

COPY *.env .

RUN pip install discord.py google-generativeai python-dotenv

COPY . .

CMD [ "python","bot.py"]