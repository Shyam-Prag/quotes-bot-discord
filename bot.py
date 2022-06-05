# bot.py
import os
import random
import requests

import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
channel = client.get_channel(982704426454229006)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
#
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)


@tasks.loop(hours=24)
async def sendMotivationalMessage():
    response = requests.get("https://zenquotes.io/api/today")
    quote_json = response.json()
    quote = quote_json[0]
    quoteFinal = quote['q']
    sendmessageFinal = "```Quote of the day is: {0}```".format(quoteFinal)
    channel = client.get_channel(772206231976411146)
    await channel.send(sendmessageFinal)


@client.event
async def on_ready():
    sendMotivationalMessage.start()

client.run(TOKEN)
#check