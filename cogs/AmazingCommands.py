import discord
from discord.ext import commands
from Pandora import aquire_uuid
import random
from typing import List

class AmazingCommands(commands.Cog):
    
    messages: List[str] = [
            "P-eee-pa pig",
            "Love is great",
            "2 + 2 is 4; cool right!",
            "ashley's the best."
            ]
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.message.Message) -> None:
        global deleted_message, author
        deleted_message, author = message, message.author
    
     
    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message) -> None:
        if message.author.id != 1013809775441629274 and message.content.lower() == 'm':   
            channel = message.channel
            await channel.send(random.choice(AmazingCommands.messages))
            await message.add_reaction('👍' )
    
    
    @commands.command()
    async def searchuuid(self, ctx: commands.Context, *, name) -> None:
        await ctx.send(f"{name}'s UUID: {aquire_uuid(name)}")
        
        
    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send('Pong! {}ms'.format(round(self.client.latency * 1000)))
        
        
    @commands.command()
    async def snipe(self, ctx: commands.Context) -> None:
        await ctx.send(f'```yaml\n{deleted_message.content}\n``` \n<@{author.id}>')