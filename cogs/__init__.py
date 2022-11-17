import discord
from discord.ext import commands

from .Giveaway import Giveaway
from .backend import Backend
from .Admin import Admin
from .CommandErrorHandler import CommandErrorHandler
from .AmazingCommands import FAmazingCommands
from .help import Help


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Admin(client))
    await client.add_cog(Backend(client))
    await client.add_cog(CommandErrorHandler(client))
    await client.add_cog(AmazingCommands(client))
    # Removes built-in help command
    client.remove_command("help")
    await client.add_cog(Help(client))
    await client.add_cog(Giveaway(client))
    

    
