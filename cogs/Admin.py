import discord
from discord.ext import commands
from typing import Optional
from types import NoneType


class Admin(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        

    @commands.command()
    @commands.has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: Optional[NoneType]=None) -> None:

        channel = await member.create_dm()
        if reason is None:
            await channel.send(f"You were banned from {member.guild}")
            try:
                await member.ban(reason="No Reason")
            except Exception:
                await ctx.send("I don't have permissions to perform this action.")
                return

            await ctx.send(f"{member.name} was banned for: No Reason Specified")
            return
        await channel.send(f"You were banned from {member.guild} for:\n{reason}")
        try:
            await member.ban(reason=reason)
        except Exception:
            await ctx.send("I don't have permissions to perform this action.")
            return
        await ctx.send(f"{member.name} was banned for {reason.capitalize()}")


    @commands.command()
    @commands.has_permissions(administrator=True, manage_messages=True, manage_roles=True)    
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:

        channel = await member.create_dm()
        if reason is None:
            await channel.send(f"You were kicked from {member.guild}")
            try: 
                await member.kick(reason="No Reason")
            except Exception:
                await ctx.send("I don't have permissions to perform this action.")
                return
            await ctx.send(f"{member.name} was kicked for: No Reason Specified")
            return
        await channel.send(f"You were kicked from {member.guild} for:\n{reason}")
        try:
            await member.kick(reason=reason)
        except commands.MissingPermissions:
            await ctx.send("I don't have permissions to perform this action.")
            return
        await ctx.send(f"{member.name} was kicked for: {reason.capitalize()}")

