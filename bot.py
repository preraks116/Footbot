import os
import logging

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.file import File

from cogs.emogif import EmoGifs
from cogs.news import News

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# load environment variables
load_dotenv()

bot = commands.Bot(command_prefix=';')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print("Ready")

bot.add_cog(News(bot))
bot.add_cog(EmoGifs(bot))

bot.run(os.environ.get("TOKEN"))
