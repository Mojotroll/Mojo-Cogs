from .artsy import artsy

def setup(bot):
    n = artsy(bot)
    bot.add_cog(n)