import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    @commands.command()    
    async def help(self, ctx: commands.Context) -> None:
        embeded =  discord.Embed(title="Help command", description="Shows commands")
        embeded.add_field(name=".searchuuid", value="Fetches a minecraft players UUID", inline=False)
        embeded.add_field(name=".ping", value="Returns the ping of the bot", inline=False)
        embeded.add_field(name=".ban", value="Bans someone", inline=False)
        embeded.add_field(name=".kick", value="Kicks someone", inline=False)
        await ctx.send(embed=embeded)