from .diomedes import diomedes

def setup(bot):
    n = diomedes(bot)
    bot.add_listener(n.diomedes, "on_message")
    bot.add_cog(n)