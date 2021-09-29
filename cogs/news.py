from typing import Optional

import discord
from discord.ext import commands

class News(commands.Cog):
    '''
    Daily dose of football news
    '''
    def __init__(self, bot):
        self.bot = bot  
        self.sourcesdict = {'skysports': ["Sky Sports","https://seekvectorlogo.com/wp-content/uploads/2018/01/sky-sports-vector-logo.png"],
                'bbc': ["BBC News","https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1200px-BBC_News_2019.svg.png"]}

    # a function to setup any general source
    def source(self,key):
        sourcelist = self.sourcesdict[key]
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
                sourcenames += f'**{self.sourcesdict[key][0]}** : `{key}`\n'
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