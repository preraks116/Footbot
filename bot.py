import discord
import logging
from discord import activity
from discord.ext import commands
from discord.file import File

from cogs.news import News
from cogs.emogif import EmoGifs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
TOKEN='ODkyNDgxODAyNzg1MTQ4OTY4.YVNicw.G1hxVzzsIYnrNBKDWtGSF-RGm2k'

bot = commands.Bot(command_prefix=';')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print("Ready")

bot.add_cog(News(bot))
bot.add_cog(EmoGifs(bot))

bot.run(TOKEN)
