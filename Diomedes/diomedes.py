from redbot.core import commands
import discord
import random

class diomedes(commands.Cog):
    """You have Captain Diomedes."""
    def __init__(self, bot):
        self.bot = bot
        self.quotes = ["No foe shall see my mercy", "You are ready for war now", "You are ready to excel now", "You are well suited now for victory", "Be Stregnthened and be ready", "Might and Honor, Glory and Victory", "Steady yourself brother", "Rise renewed for battle", "You reek of fear and frailty", "You tremble because you are weak", "Your Weakness shows", "See what fight you have in you now", "Brother, I am Pinned Here!", "Orders? Moving Now", "Orks", "Death to his enemies all", "That noise cannot defeat me", "Ah, a warp spider", "ITS THE BANEBLADE!", "You dare?! YOU DARE!?", "Departing Now", "Moving Now", "Retreat now for victory later"]

    @commands.Cog.listener()
    async def on_message(self, message):
        """Captain Diomedes with another banger"""
        if message.guild is None:
            return
        if message.author.bot:
            return
        if await self.bot.cog_disabled_in_guild(self, message.guild):
            return
        if await self.bot.is_automod_immune(message.author) is True:
            return
        for x in message.content.split():
            try:
                if x.lower() == "captain diomedes":
                    warpSpider = random.choice(self.quotes)
                    await message.channel.send(warpSpider)
            except discord.errors.Forbidden:
                pass