import discord
from discord.ext import commands
from colorama import Fore
import random
from typing import List


class Backend(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        print(f"{Fore.MAGENTA}{member} has joined {member.guild.name}")
        
            
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None:
        print(f"{Fore.LIGHTGREEN_EX}Joined guild: {guild.name}")
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild) -> None:
        print(f"{Fore.LIGHTRED_EX}Pandora was kicked/banned/server was deleted from: {guild.name}")
        

        
            
