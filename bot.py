import discord
import logging
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix=';')

@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def ineedhelp(ctx, arg):
    if(arg == "noob"):
        await ctx.send("Shut up you are noob")
    else:
        await ctx.send(arg)

@bot.command()
async def sk(ctx):
    await ctx.send("https://tenor.com/view/stryk-rainy-day-vfx-xmas-crown-sk-gif-15836072")
    

@bot.command()
async def kk(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/814422269002121266/892488294292656129/60a9a274-f0fc-4588-a40d-7792934662a8.png")
    


bot.run('ODkyNDgxODAyNzg1MTQ4OTY4.YVNicw.G1hxVzzsIYnrNBKDWtGSF-RGm2k')
