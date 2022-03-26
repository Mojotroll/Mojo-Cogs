from .ba import ba

def setup(bot):
    n = ba(bot)
    bot.add_cog(n)