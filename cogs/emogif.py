import discord
from discord.ext import commands


class EmoGifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sk(self, ctx):
        """
        Sk ig
        """
        await ctx.send(
            "https://tenor.com/view/stryk-rainy-day-vfx-xmas-crown-sk-gif-15836072"
        )

    @commands.command()
    async def kk(self, ctx):
        """
        KK's daily haram
        """
        await ctx.send(
            "https://cdn.discordapp.com/attachments/814422269002121266/892488294292656129/60a9a274-f0fc-4588-a40d-7792934662a8.png"
        )

    @commands.command()
    async def kek(self, ctx):
        """
        Avg Kekw
        """
        await ctx.send("https://tenor.com/view/kekwtf-gif-18599263")
