from redbot.core import commands
import discord
import random
import urllib.parse
import aiohttp
import json

class artsy(commands.Cog):
    """Sipping Tea with your pinkie finger up!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def artsy(self, ctx):
        """Commands for Artsy Cog"""
        pass
    
    @artsy.command(name="search")
    async def search(self, ctx, *, query):
        """Search for a specific masterpiece"""
        cleanquery = urllib.parse.quote(query)

        url = 'https://api.artic.edu/api/v1/artworks/search?q=' + cleanquery + '&limit=1&fields=title,artist_display,date_display,image_id'
        print(url)

        async with aiohttp.ClientSession().get(url) as response:
            data = await response.read()
            data = data.decode("utf-8")
            data = json.loads(data)
            date = data.get("data")[0].get("date_display")
            print(date)
            artist = data.get("data")[0].get("artist_display")
            print(artist)
            title = data.get("data")[0].get("title")
            print(title)
            image_id = data.get("data")[0].get("image_id")
            print(image_id)

            embed = discord.Embed()
            embed.title = title
            embed.set_image(url='https://www.artic.edu/iiif/2/' + image_id + '/full/250,/0/default.jpg')
            embed.add_field(name="Artist", value=artist)
            embed.add_field(name="Date:", value=date)

            await ctx.send(embed=embed)

    @artsy.command(name="random")
    async def random(self, ctx):
        """Search for a random piece of work to make your day"""
        page = random.choice(range(1,50,1))
        page = str(page)
        url = "https://api.artic.edu/api/v1/artworks?page=" + page + "&limit=100"
        print(url)

        async with aiohttp.ClientSession().get(url) as response:
            data = await response.read()
            data = data.decode("utf-8")
            data = json.loads(data)
            data = data.get("data")
            result = random.choice(data)
            date = result.get("date_display")
            print(date)
            artist = result.get("artist_display")
            print(artist)
            title = result.get("title")
            print(title)
            image_id = result.get("image_id")
            print(image_id)

            embed = discord.Embed()
            embed.title = title
            embed.set_image(url='https://www.artic.edu/iiif/2/' + image_id + '/full/250,/0/default.jpg')
            embed.add_field(name="Artist", value=artist)
            embed.add_field(name="Date:", value=date)

            await ctx.send(embed=embed)
