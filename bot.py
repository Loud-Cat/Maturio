import os
import discord
from discord.ext import commands
client = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(filename, "was loaded.")

@client.event
async def on_ready():
    print("Wahoo! Maturio!")
    channel = client.get_channel(867597108236386306)
    await client.change_presence(activity=discord.Game('Life'))
    await channel.send("Wahoo! Its a me, Maturio!")

client.run('TOKEN')
