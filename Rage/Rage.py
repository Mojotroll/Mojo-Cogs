import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
import os
import aiohttp

class Rage:
    """Raging Demon"""
    #Use IRDuMb's examples for this >.<
    def __init__(self,bot):
        self.bot = bot
        self.url = "http://bensbargains.com/thecheckout/wp-content/uploads/2015/10/nerd-rage.jpg"
        self.imexist = os.path.exists('data/rage/nerd-rage-1024x535.jpg')
        self.image = "data/rage/nerd-rage-1024x535.jpg"
        self.serverinfo = fileIO("data/rage/servers.json", "load")

    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions(manage_roles=True)
    async def enpower(self, ctx):
        """Turn the Rage on/off for a server"""
        server = ctx.message.server
        if server.id not in self.serverinfo:
            self.serverinfo[server.id] = True
        else:
            self.serverinfo[server.id] = not self.serverinfo[server.id]
        fileIO("data/rage/servers.json", "save", self.serverinfo)
        if self.serverinfo[server.id]:
            await self.bot.say("Feel the Rage of the Firelands!")
        else:
            await self.bot.say("Mellowing out....")

    async def rage_check(self, message):
        server = message.server
        if message.author.id == self.bot.user.id:
            return
        if server != None:
            if server.id not in self.serverinfo:
                self.serverinfo[server.id] = False
            if not self.serverinfo[server.id]:
                return

        # comments explaining next section. seemed easier to read this way
        # check for a phrase in message
        #   if sadface isn't downloaded yet, dl it
        #       try
        #           get image from url
        #           write image to file
        #           it worked \o/
        #           send it
        #       except
        #           there was a problem, print an error then try to send the url instead
        #   else sadface image already downloaded, send it Pasted from sadface use this idea

        for x in message.content.split():
            if x.lower() == "rage":
                if not self.imexist:
                    try:
                        async with aiohttp.get(self.url) as r:
                            image = await r.content.read()
                        with open('data/rage/nerd-rage-1024x535.jpg','wb') as f:
                            f.write(image)
                        self.imexist = os.path.exists('data/rage/nerd-rage-1024x535.jpg')
                        await self.bot.send_file(message.channel,self.image)
                    except Exception as e:
                        print(e)
                        print("Hiccup in the Matrix! D: Using URL instead")
                        await self.bot.send_message(message.channel,self.url)
                else:   
                    await self.bot.send_file(message.channel,self.image)
              
#Special Thanks to Al for the help on this portion, need to figure out a way to get it to do it more than once, it seems to never go through again after the first play
			  # if "Audio" in self.bot.cogs and message.author.voice_channel:
                  #  audio = self.bot.get_cog("Audio")
                   # if audio._get_queue_nowplaying(server) is None:
                    #    voice_channel = message.author.voice_channel
                      #  url = "https://www.youtube.com/watch?v=04F4xlWSFh0"
                    #    if not audio.voice_connected(server):
                     #       try:
                     #           audio.has_connect_perm(message.author, server)
                       #     except AuthorNotConnected:
                         #       return
                        #    except UnauthorizedConnect:
                        #        return
                        #    except UnauthorizedSpeak:
                          #      return
                          #  else:
                           #     await audio._join_voice_channel(voice_channel)
                       # else: 
                        #    if audio.voice_client(server).channel != voice_channel:
                        #        await audio._stop_and_disconnect(server)
                        #        await audio._join_voice_channel(voice_channel)                                
                     #   return audio._add_to_queue(server, url)


def check_folders():
    if not os.path.exists("data/rage"):
        print("Creating data folder...")
        os.makedirs("data/rage")

def check_files():
    # create server.json if not there
    # put in default values
    default = {}
    if not os.path.isfile("data/rage/servers.json"):
        print("Creating servers.json...")
        fileIO("data/rage/servers.json", "save", default)


def setup(bot):
    check_folders()
    check_files()
    n = Rage(bot)
    # add an on_message listener
    bot.add_listener(n.rage_check, "on_message")
    bot.add_cog(n)
