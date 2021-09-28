import discord
import logging
from discord import activity
from discord.ext import commands
from discord.file import File

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
TOKEN='ODkyNDgxODAyNzg1MTQ4OTY4.YVNicw.G1hxVzzsIYnrNBKDWtGSF-RGm2k'

bot = commands.Bot(command_prefix=';', help_command=None)

def helpGen():
    description = "`ineedhelp` : you just did it\n"
    return description

def helpFootball():
    description = "`news` : gives news related to football\n"

    return description

def helpGif():
    description = "`kek` : sends kek gif\n"
    description += "`sk` : its kinda cool ig\n"
    description += "`kk` : for all y'all liberals\n"
    return description


# a function to setup any general source
def source(key):
    sourcelist = sourcesdict[key]
    ##### this section should be replaced by function that returns the following list [news_link, news_heading, news_img_link]
    if(key == "skysports"):
        sourcelist += ["https://www.skysports.com/football/news/11688/12419667/championship-highlights-and-round-up","Championship highlights and round-up: West Brom hit four; Huddersfield, QPR win\n","https://e0.365dm.com/21/09/1600x900/skysports-karlan-grant-west-brom_5528633.jpg?20210928200231"]
    elif(key == "bbc"):
        sourcelist += ["https://www.skysports.com/football/news/11688/12419667/championship-highlights-and-round-up","Messi scores superb first PSG goal in win over Man City\n","https://ichef.bbci.co.uk/onesport/cps/800/cpsprodpb/11AC8/production/_120729327_messi-goal.jpg"]
    #####
    embed=discord.Embed(title=sourcelist[0], description = sourcelist[3], color=0xFF5733)
    embed.set_author(name="FootBot News", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://a.espncdn.com/combiner/i?img=/redesign/assets/img/icons/ESPN-icon-soccer.png&w=288&h=288&transparent=true")
    embed.set_thumbnail(url=sourcelist[1])
    embed.set_image(url=sourcelist[4])
    embed.add_field(name="**Link**", value=sourcelist[2], inline=False)
    return embed

sourcesdict = {'skysports': ["Sky Sports","https://seekvectorlogo.com/wp-content/uploads/2018/01/sky-sports-vector-logo.png"],
                'bbc': ["BBC News","https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1200px-BBC_News_2019.svg.png"]}

# sourcesdict = {'skynews': ["Sky Sports","https://seekvectorlogo.com/wp-content/uploads/2018/01/sky-sports-vector-logo.png",skySportsSource],
#                 'bbc': ["BBC News","https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1200px-BBC_News_2019.svg.png",bbcSource]} 
# 
# the scrapers will also be added to sourcesdict and will be used like `sourcelist[2]()`

@bot.command()
async def news(ctx, arg = 'null'):
    if(arg == "list"):
        sourcenames = ""
        for key in sourcesdict:
            sourcenames += f'**{sourcesdict[key][0]}** : `{key}`\n'
        
        embed=discord.Embed(title="List of Sources", description = sourcenames, color=0xFF5733)
        embed.set_author(name="FootBot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://a.espncdn.com/combiner/i?img=/redesign/assets/img/icons/ESPN-icon-soccer.png&w=288&h=288&transparent=true")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/3b/39/c9/3b39c9ea1f56edc75bdb093c1400e7a8.png")
        await ctx.send(embed=embed)
    elif(arg == "null" ):
        for key in sourcesdict:
                await ctx.send(embed=source(key))
    else:
        try:
            await ctx.send(embed=source(arg))
        except:
            await ctx.send(f'Error: cannot recognize source: {arg}\n')

@bot.command()
async def help(ctx, arg = 'null'):
    if(arg == "noob"):
        await ctx.send("Shut up you are noob")
    elif(arg == "null" ):
        embed=discord.Embed(title="**prefix : `;`**", description = "**A list of commands you can use**\n", color=0xFF5733)
        embed.set_author(name="FootBot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://a.espncdn.com/combiner/i?img=/redesign/assets/img/icons/ESPN-icon-soccer.png&w=288&h=288&transparent=true")
        embed.set_thumbnail(url="https://media.nesta.org.uk/images/good_help_bad_help.max-1200x600.png")
        embed.add_field(name="General", value=helpGen(), inline=False)
        embed.set_image(url="https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help.jpg")
        embed.add_field(name="Football", value=helpFootball(), inline=False)
        embed.add_field(name="Emojis & Gifs", value=helpGif(), inline=True)
        # embed.set_footer(text="sussy baka amogus uwu")
        await ctx.send(embed=embed)
    else:
        await ctx.send("```ARM\nError : invalid argument```")

@bot.command()
async def sk(ctx):
    await ctx.send("https://tenor.com/view/stryk-rainy-day-vfx-xmas-crown-sk-gif-15836072")
    

@bot.command()
async def kk(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/814422269002121266/892488294292656129/60a9a274-f0fc-4588-a40d-7792934662a8.png")
    

@bot.command()
async def kek(ctx):
    await ctx.send("https://tenor.com/view/kekwtf-gif-18599263")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print("Ready")

bot.run(TOKEN)
