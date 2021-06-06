from .diomedes import diomedes

def setup(bot):
    n = diomedes(bot)
    bot.add_cog(n)