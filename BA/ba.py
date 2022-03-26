import discord
from redbot.core import checks, Config, commands, bot

UNIQUE_ID = 10002500321

class ba(commands.Cog):
    """For the Suave Gentlemen of the Abyss"""
    def __init__(self, bot):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=UNIQUE_ID, force_registration=True)
        self.conf.register_guild(channels=[])
        self.image = "images/ltd.png"
        self.keyword = "euphoria"


    @commands.group()
    async def ba(self, ctx):
        """Commands for Burning Abyss Cog"""
        pass
    
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Post the image to the selected channels"""

        # Attempt to load guild channel restrictions
        try:
            channels = await self.conf.guild(message.guild).channels()
            if message.channel.id not in channels:
                return
        except AttributeError:  # Not in a guild
            pass

        # Ignore messages from the bot itself
        if message.author.id == self.bot.user.id:
            return

        if (message.lower() == self.keyword):
            await self.bot.send(file=discord.File(self.image))
        else:
            pass


    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @ba.command()
    async def channelenable(self, ctx: commands.Context, channel: str = None):
        """ Enable the peasants to be graced by BA's Majesty"""
        await self.channels_update(channel or ctx.channel.id, ctx.guild, True)

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @ba.command()
    async def channeldisable(self, ctx: commands.Context, channel: str = None):
        """Deny the Peasants of Channel the grace of BA's Majesty"""
        await self.channels_update(channel or ctx.channel.id, ctx.guild, False)

    async def channels_update(self, channel, guild, add: bool = True):
        """ Update list of channels in which shall be graced with BA goodness"""
        channels = await self.conf.guild(guild).channels()
        if add:
            channels.append(int(channel))
        else:
            channels.remove(int(channel))
        await self.conf.guild(guild).channels.set(channels)


    
