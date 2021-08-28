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
            data = await response.read()
            print(data)
            data = json.loads(data)
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
        url = "https://api.artic.edu/api/v1/artworks"

        async with aiohttp.ClientSession().get(url) as response:
            #data = await json.loads(response.read())
            data = await response.read()
            data = data.decode("utf-8")
            data = json.loads(data)
            data = data.get("data")
            result = random.choice(data)
            print(result)

            for item in result:
                print(item["date_display"])
            
            tab = tabulate(["Date", result["date_display"]], ["Artist(s)",result["artist_display"]])

            embed = discord.Embed()
            embed.title = result["title"]
            embed.set_image(url='https://www.artic.edu/iiif/2/' + result["image_id"] + '/full/250,/0/default.jpg')
            embed.add_field(name="Information regarding " + result["title"], value=tab)

            await ctx.send(embed=embed)
