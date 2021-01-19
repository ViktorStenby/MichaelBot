# bot.py
import os
from dotenv import load_dotenv

from discord.ext import commands
import sys, traceback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands

import sys, traceback

# #Cogs to be imported.
# initial_extensions = ['cogs.simple', 'cogs.speech']
initial_extensions = ['cogs.speech']

bot = commands.Bot(command_prefix='_mb ', description='Michael Bot')

#Load all of the extensions.
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    #await bot.change_presence(game=discord.Game(name='Cogs Example', type=1, url='https://twitch.tv/kraken'))
    #print(f'Successfully logged in and booted...!')

bot.run(TOKEN, bot=True, reconnect=True)
