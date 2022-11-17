import discord
from discord.ext import commands
import colorama
import os


intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix=".",
                      intents=intents
                      )
TOKEN = os.getenv("TOKEN")
BOTID = 1013809775441629274


@client.event
async def on_ready() -> None:
    await client.load_extension(f"cogs.__init__")
    # game = discord.Game(f"On {str(len(client.guilds))} servers.")
    await client.change_presence(activity=discord.Game("Development"))

    print("Bot ready!")

    
     

if __name__ == "__main__":
    os.system("cls")
    colorama.init(autoreset=True)    
    client.run(TOKEN)


