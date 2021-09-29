from hashlib import new
from typing import Optional
from scrapers.skysports_getsource import skysports_getsource
from scrapers.bbc_getsource import bbc_getsource
import discord
import random
from discord.ext import commands

class News(commands.Cog):
    '''
    Daily dose of football news
    '''
    def __init__(self, bot):
        self.bot = bot  
        self.sourcesdict = {
            'skysports': {
                "name" : "Sky Sports",
                "logo" : "https://seekvectorlogo.com/wp-content/uploads/2018/01/sky-sports-vector-logo.png",
                "scraper" : skysports_getsource
            },
            'bbc': {
                "name" : "BBC News",
                "logo" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1200px-BBC_News_2019.svg.png"
                "scraper": bbc_getsource
            }
        }

    # a function to setup any general source
    def source(self,key):
        source = self.sourcesdict[key]
        news = source['scraper']()
        news = news[random.randint(0,len(news))]
        embed=discord.Embed(title=source['name'], description = news['title'], color=0xFF5733)
        embed.set_author(name="FootBot News", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://a.espncdn.com/combiner/i?img=/redesign/assets/img/icons/ESPN-icon-soccer.png&w=288&h=288&transparent=true")
        embed.set_thumbnail(url=source['logo'])
        print(news)
        embed.set_image(url=news['img'])
        embed.add_field(name = "Source" ,value=f"[Click Here]({news['link']})", inline=False)
        embed.set_footer(text=news['datetime'])
        return embed


    @commands.command()
    async def news(self,ctx, option: Optional[str]):
        '''
        Returns a list of latest news articles.
        Usage : ;news [OPTIONS]
        Options :
            list -- Prints a list of available sources
        '''
        if(option == "list"):
            sourcenames = ""
            for key in self.sourcesdict:
                sourcenames += f'**{self.sourcesdict[key]["name"]}** : `{key}`\n'
            embed=discord.Embed(title="List of Sources", description = sourcenames, color=0xFF5733)
            embed.set_author(name="FootBot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://a.espncdn.com/combiner/i?img=/redesign/assets/img/icons/ESPN-icon-soccer.png&w=288&h=288&transparent=true")
            embed.set_thumbnail(url="https://i.pinimg.com/originals/8f/23/bd/8f23bd594b6ad1be9fbe03a67c892f67.png")
            await ctx.send(embed=embed)
        elif(option == None ):
            for key in self.sourcesdict:
                    await ctx.send(embed=self.source(key))
        else:
            try:
                await ctx.send(embed=self.source(option))
            except:
                await ctx.send(f'Error: cannot recognize source: {option}\n')