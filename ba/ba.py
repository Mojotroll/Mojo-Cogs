import discord
from redbot.core import checks, Config, commands, bot

class ba(commands.Cog):
    """For the Suave Gentlemen of the Abyss"""
    def __init__(self, bot):
        self.bot = bot
        self.image = "/images/ltd.png"

    
    
    @commands.command()
    async def platinspiration(self, ctx):
        """Survive Plat One with Euphoric Inspiration"""

        await ctx.send(file=discord.File(self.image))




    
