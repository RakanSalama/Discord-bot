import discord
import os
from discord.ext.commands import Bot
import random
import math

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #Answer a msg 
    if message.content.startswith('Hello rakan\'s bot'):
        await message.channel.send('Hi :D')
    #Answer With a picture OR Gif
    if message.content.startswith('image'):
        await message.channel.send(file=discord.File('C:\\Users\\Admin\\Desktop\\T.jpg'))
    if message.content.startswith('gif'):
        await message.channel.send(file=discord.File('C:\\Users\\Admin\\Desktop\\1f2.gif'))
    #Answer With a sound
    if message.content.startswith('sound'):
        await message.channel.send(file=discord.File('C:\\Users\\Admin\\Desktop\\358-teemo-laugh.mp3'))
    #simple Game
    if message.content.startswith('game'):
        await message.channel.send('Guess a number from 1 to 10, if you get it from the first time you win')
        number = random.randint(1,10)
        def check(m):
            return m.author == message.author and m.channel == message.channel and m.content.isdigit()
        guess = await client.wait_for('message', check=check)
        if int(guess.content) == number:
            await message.channel.send('WOW!!!!!! YOU GOT IT')
        else:
            await message.channel.send('Not today:( the number is '+ str(number))
client.run('TOKEN')