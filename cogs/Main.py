import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "!")

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @client.command()
    async def main(self, ctx):
        em = discord.Embed(title="Wahoo!", description="About Maturio")
        em.add_field(name="Who am I?", value="Only the most mature bot you'll ever meet.")
        em.add_field(inline=False, name="Who made me?", value="* Loud_Cat\n* Aryan\n * Moose")
        em.add_field(inline=False, name="Where can you find me?", value="[At my GitHub!](https://github.com/MedisonMan/Maturio)")
        em.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Main(client))
