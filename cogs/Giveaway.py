
import random
import discord
from discord.ext import commands
import time
import datetime
from typing import Tuple, List
import asyncio

Id = int

class Giveaway(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.giveaway_ongoing: bool = False
        self.rerollable: bool = False
        self.previous_giveaway_id: int = None
        self.users_in_previous_giveaway: Tuple(Id) = ()
        self.previous_embed: discord.Embed = None
        self.previous_giveaways: List[str] = []
    
    
        
    @commands.command()
    async def giveaway(self,
                       ctx: commands.Context,
                       *,
                       prize:str) -> None:
        self.giveaway_caller = ctx.message.author.id
        self.giveaway_ongoing = True
        answers = []

        while self.giveaway_ongoing:
            try:
                await ctx.send("```yaml\nHow many hours should the giveaway be (0 if 0 hours)\n```")
                hours: discord.Message = await self.client.wait_for('message', timeout=10)
                await ctx.send("```yaml\nHow many minutes\n```")
                minutes: discord.Message = await self.client.wait_for('message', timeout=10)
                
            except asyncio.TimeoutError:
                await ctx.send(f"Sorry! you didn't respond in time! <@{ctx.message.author.id}>")
                self.giveaway_ongoing = False
                continue
            
            answers.append(hours.content)
            answers.append(minutes.content)
            answers.append(int())
            
                            
                            
            
            red = discord.Colour.red()
            embeded = discord.Embed(title=prize,
                                    colour=red
                                    
    )

            #"\n"


            hours, minutes, seconds = answers[0], answers[1], answers[2]
            total_seconds = int(hours)*3600 + int(minutes)*60 + int(seconds)
            seconds_copy = total_seconds
            
            embeded.add_field(name="Giveaway ongoing", value="\n".join(message for message in ("React with 🎉 to enter!", f"Time Remaining: {datetime.timedelta(seconds=total_seconds)}.", f"Hosted by <@{ctx.message.author.id}>")), inline=False)
            message = await ctx.send(embed=embeded)
            await message.add_reaction("🎉")
            
            states: List[str, str, str] = ["Giveaway Ongoing", "Last chance to enter!!!", "Giveaway Ended"]
            state_index: int = 0
            
            while total_seconds != -1:
                if total_seconds == seconds_copy//2 or total_seconds <= seconds_copy//2 and total_seconds != 0:
                    state_index = 1
                    
                elif total_seconds == 0:
                    state_index = 2
                    
                else:
                    state_index=0
                
                
                timer = datetime.timedelta(seconds=total_seconds)
                embeded.remove_field(index=0)
                embeded.insert_field_at(index=0,
                                        name=f"{states[state_index]}",
                                        value="\n".join(message for message in ("React with 🎉 to enter!",
                                                                                f"Time Remaining: {timer}",
                                                                                f"Hosted by <@{ctx.message.author.id}>")),
                                        inline=False)
                await message.edit(embed=embeded)
                await asyncio.sleep(1)
                total_seconds -=1
            
            message1 = await message.channel.fetch_message(message.id)
            message1 = message1.reactions[0]
            users = [user.id async for user in message1.users() if user.id != 1013809775441629274]
            winner_id: int = random.choice(users)
            embeded.remove_field(index=0)
            embeded.insert_field_at(index=0,
                                    name="Giveaway Ongoing",
                                    value="\n".join(message for message in ("React with 🎉 to enter!",
                                                                            f"Time Remaining: {timer}",
                                                                            f"Hosted by <@{ctx.message.author.id}>",
                                                                            f"Winner: <@{winner_id}>")),
                                    inline=False)
            
            await message.edit(embed=embeded)
            await ctx.send(f"The winner is <@{winner_id}>!")
            self.previous_giveaway_id = message.id
            self.users_in_previous_giveaway = tuple(users)
            self.previous_embed = embeded
            self.rerollable = -1
            await asyncio.sleep(300)
            self.giveaway_ongoing = False
            self.rerollable = False
    
    @commands.command()    
    async def reroll(self, ctx: commands.Context) -> None:
        if self.rerollable == -1:
            message = await ctx.channel.fetch_message(self.previous_giveaway_id)
            new_winner = random.choice(self.users_in_previous_giveaway)
            self.previous_embed.remove_field(index=0)
            self.previous_embed.insert_field_at(index=0,
                                name="Giveaway Ended",
                                value="\n".join(message for message in ("React with 🎉 to enter!",
                                                                        f"Time Remaining: 0:00:00",
                                                                        f"Hosted by <@{ctx.message.author.id}>",
                                                                        f"Winner: <@{new_winner}>")),
                                inline=False)
            await message.edit(embed=self.previous_embed)
            await ctx.send(f"The new winner is <@{new_winner}>!")
        
        else:
            await ctx.send("There is no giveaway avaliable")
            
   