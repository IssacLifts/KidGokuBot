import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        error = getattr(error, 'original', error)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to run this command")
            
    
            
        else:
            pass
            
        