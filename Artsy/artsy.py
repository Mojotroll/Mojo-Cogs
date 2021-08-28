from redbot.core import commands
import discord
import random
import urllib.parse
import aiohttp
import json
import tabulate

class artsy(commands.Cog):
    """Sipping Tea with your pinkie finger up!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def artsy(self, ctx):
        """Commands for Artsy Cog"""
        pass
    
    @artsy.group(name="search")
    async def search(self, ctx, query):
        """Search for a specific masterpiece"""
        cleanquery = urllib.parse.quote(query)

        url = 'https://api.artic.edu/api/v1/artworks/search?q=' + cleanquery + '&limit=1&fields=title,date_display,artist_display,image_id'

        async with aiohttp.ClientSession().get(url) as response:
            data = json.loads(response.read())
            data = data.get("data")
            for list in data:
                tab = tabulate(["Date", list["date_display"]], ["Artist(s)",list["artist_display"]])

                embed = discord.Embed()
                embed.title = list["title"]
                embed.set_image(url='https://www.artic.edu/iiif/2/' + list["image_id" + '/full/250,/0/default.jpg'])
                embed.add_field(name="Information regarding " + list["title"], value=tab)

                await ctx.send(embed=embed)

    @artsy.group(name="random")
    async def random(self, ctx):
        """Search for a random piece of work to make your day"""
        url = "https://api.artic.edu/api/v1/artworks?limit=1000"

        async with aiohttp.ClientSession().get(url) as response:
            data = json.loads(response.read())
            data = data.get("data")
            result = random.choice(data)
            for list in result:
                tab = tabulate(["Date", list["date_display"]], ["Artist(s)",list["artist_display"]])

                embed = discord.Embed()
                embed.title = result["title"]
                embed.set_image(url='https://www.artic.edu/iiif/2/' + list["image_id" + '/full/250,/0/default.jpg'])
                embed.add_field(name="Information regarding " + list["title"], value=tab)

                await ctx.send(embed=embed)
