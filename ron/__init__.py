from .ron import ron

def setup(bot):
    n = ron(bot)
    bot.add_cog(n)