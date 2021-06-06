from .diomedes import diomedes

self.bot = bot
self.quotes = ["No foe shall see my mercy", "You are ready for war now", "You are ready to excel now", "You are well suited now for victory", "Be Stregnthened and be ready", "Might and Honor, Glory and Victory", "Steady yourself brother", "Rise renewed for battle", "You reek of fear and frailty", "You tremble because you are weak", "Your Weakness shows", "See what fight you have in you now", "Brother, I am Pinned Here!", "Orders? Moving Now", "Orks", "Death to his enemies all", "That noise cannot defeat me", "Ah, a warp spider", "ITS THE BANEBLADE!", "You dare?! YOU DARE!?", "Departing Now", "Moving Now", "Retreat now for victory later"]

def setup(bot):
    n = diomedes(bot)
    bot.add_listener(n.diomedes, "on_message")
    bot.add_cog(n)