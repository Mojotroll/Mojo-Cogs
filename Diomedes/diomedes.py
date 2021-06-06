from redbot.core import commands
import random

class diomedes(commands.Cog):
    """You have Captain Diomedes."""

    async def diomedes(self, message):
        """Captain Diomedes with another banger"""
        if message.author.id == self.bot.user.id:
            return
        for x in message.content.split():
            if x.lower() == "captain diomedes":
                warpSpider = random.choice(self.quotes)  
                await self.bot.send_message(message.channel,warpSpider)
