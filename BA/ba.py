import discord
from redbot.core import checks, Config, commands, bot

class ba(commands.Cog):
    """For the Suave Gentlemen of the Abyss"""
    def __init__(self, bot):
        self.bot = bot
        self.image = "images/ltd.png"


    @commands.group()
    async def ba(self, ctx):
        """Commands for Burning Abyss Cog"""
        pass
    
    
    @ba.commands()
    async def inspiration(self, message):
        """Survive Plat One with Euphoric Inspiration"""

        # Ignore messages from the bot itself
        if message.author.id == self.bot.user.id:
            return

        await self.bot.send(file=discord.File(self.image))




    
