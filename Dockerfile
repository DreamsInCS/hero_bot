FROM python:3.8
# expose heroku port
EXPOSE ${PORT}
EXPOSE 3994
WORKDIR /hero_bot
COPY . .
RUN python -m pip install discord.py
CMD ["python", "hero_bot.py"]
