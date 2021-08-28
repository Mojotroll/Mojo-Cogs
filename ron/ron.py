from redbot.core import commands
import discord
import urllib.parse
import aiohttp
import json

class ron(commands.Cog):
    """My name is Ronald Ulysses Swanson"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def onwithron(self, ctx, query):
        """Get some fatherly advice from the big man himself"""

        url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

        async with aiohttp.ClientSession().get(url) as response:
            data = await response.text()
            await ctx.send(data)
            response.close()

    @commands.command()
    async def searchRon(self, ctx, word):
        """Search for a random piece of work to make your day"""
        cleanquery = urllib.parse.quote(word)
        url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/" + cleanquery

        async with aiohttp.ClientSession().get(url) as response:
            data = await response.text()
            if data.count < 3:
                await ctx.send("No results found, please try again")
                response.close()
            else:
                await ctx.send(data)
                response.close()
