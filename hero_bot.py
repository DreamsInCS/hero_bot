import asyncio
import datetime
import discord
import os
import random
import time

THREE_SEC = 3.0
SEC_PER_MIN = 60
POWER_POST_WAIT_TIME = SEC_PER_MIN * 10
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

flushed_face = "\U0001f633"
bot_token = os.getenv('HERO_TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=intents)

fella_response_list = [
    "Hold it there a moment. Did my fella just say... ***fella***?! \U0001f499",  # blue heart
    flushed_face,
    "https://tenor.com/view/happy-hero-omori-hero-emotions-omori-happy-hero-omori-omori-gif-20095992",
    "https://www.youtube.com/watch?v=uX2mopyE5Z0",
    "Yay!"
]


@client.event
async def on_ready():
    print('Hero is here! Username is: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author != client.user and not isinstance(message.channel, discord.channel.DMChannel):
        itchy_id = os.getenv('ITCHY_DISCORD_ID')
        william_id = os.getenv('WILLIAM_DISCORD_ID')

        if itchy_id != None and william_id != None:
            itchy_id = int(itchy_id)
            william_id = int(william_id)

        if 'fella' in message.content.lower():
            yoan_id = os.getenv('YOAN_DISCORD_ID')

            if yoan_id != None:
                yoan_id = int(yoan_id)

            fella_elapsed_time = os.getenv('FELLA_ELAPSED_TIME')

            if fella_elapsed_time == None or time.time() - float(fella_elapsed_time) >= THREE_SEC:
                if message.author.id == yoan_id:
                    await good_fella_message(message)
                else:
                    await bad_fella_message(message)

                os.environ['FELLA_ELAPSED_TIME'] = str(time.time())
        elif message.author.id == william_id:
            if message.content.startswith('https://tenor.com/') and ('omni' in message.content.lower() or 'xehanort' in message.content.lower()):
                last_power_post = os.getenv('LAST_POWER_POST')

                if last_power_post == None or time.time() - float(last_power_post) >= POWER_POST_WAIT_TIME:
                    os.environ['LAST_POWER_POST'] = str(time.time())
                    await william_power_message(message)
        elif message.author.id == itchy_id:
            last_itchy_message = os.getenv('LAST_ITCHY_MESSAGE')

            if last_itchy_message == None:
                os.environ['LAST_ITCHY_MESSAGE'] = str(datetime.datetime.today)
                await itchy_daily_message(message)
            else:
                if str(datetime.datetime.today) > last_itchy_message:
                    os.environ['LAST_ITCHY_MESSAGE'] = str(
                        datetime.datetime.today)
                    itchy_daily_message(message)


async def good_fella_message(message):
    rdm_idx = random.randint(0, len(fella_response_list) - 1)

    await asyncio.sleep(1.0)
    await message.channel.send(fella_response_list[rdm_idx])


async def bad_fella_message(message):
    num_bad_fellas = os.getenv('BAD_FELLAS')

    if num_bad_fellas == None or int(num_bad_fellas) < 1:
        slight_smile = '\U0001f642'

        os.environ['BAD_FELLAS'] = '1'
        await asyncio.sleep(1.0)
        await message.add_reaction(slight_smile)
        await asyncio.sleep(2.0)
        await message.channel.send("Well... you're not that uncool, I guess!")
    elif int(num_bad_fellas) >= 3:
        os.environ['BAD_FELLAS'] = '0'
        await asyncio.sleep(1.0)
        await message.channel.send("OK.")
        await asyncio.sleep(2.0)
        await message.channel.send("https://tenor.com/view/kanye-west-stare-staring-funny-gif-13590085")
        await asyncio.sleep(2.0)

        neutral_face = '\U0001f610'
        await message.channel.send("Y'all are really trying, it's great! But... idk. Something's missing. " + neutral_face)
    else:
        weird_champ = '<:WeirdChamp:550166396449849344>'
        os.environ['BAD_FELLAS'] = str(int(
            os.environ['BAD_FELLAS']) + 1)

        await asyncio.sleep(1.0)
        await message.add_reaction(weird_champ)
        await asyncio.sleep(2.0)
        await message.channel.send("Ehh, you used a pretty cool word there, but...")


async def william_power_message(message):
    smirking_face = '\U0001f60f'

    await asyncio.sleep(1.2)
    await message.channel.send("Erm...")
    await asyncio.sleep(2.0)
    await message.channel.send("https://static.wikia.nocookie.net/omori/images/3/34/DWHERO11.png/revision/latest?cb=20210520085337")
    await asyncio.sleep(2.0)
    await message.channel.send("You really shouldn't lust for so much power, William!")
    await asyncio.sleep(1.2)

    await message.channel.send("Just don't forget...")
    await asyncio.sleep(2.0)
    await message.channel.send("https://static.wikia.nocookie.net/omori/images/6/6c/DWHERO14.png/revision/latest?cb=20210111034354")
    await asyncio.sleep(2.0)
    await message.channel.send("We're all friends here, after all! " + smirking_face)


async def itchy_daily_message(message):
    await asyncio.sleep(1.0)
    await message.channel.send("https://tenor.com/view/minion-but-despicable-me-pool-swim-gif-16227921")
    await asyncio.sleep(1.0)
    await message.channel.send("Isn't she cute!? " + flushed_face)


client.run(bot_token)
