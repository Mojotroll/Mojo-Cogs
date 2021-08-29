from redbot.core import commands
import discord
import urllib.parse
import aiohttp
import json
import asyncio

class ron(commands.Cog):
    """My name is Ronald Ulysses Swanson"""
    def __init__(self, bot):
        self.bot = bot
        self._session = aiohttp.ClientSession()

    async def __unload(self):
        asyncio.get_event_loop().create_task(self._session.close())

    async def get(self, url):
        async with self._session.get(url) as response:
            data = await response.read()
            data = data.decode("utf-8")
            data = json.loads(data)
            return await data

    @commands.command()
    async def onwithron(self, ctx):
        """Get some fatherly advice from the big man himself"""
        url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

        data = await self.get(url)
        data = str(data[0])
        await ctx.send(data + " - Ron Swanson")

    @commands.command()
    async def searchRon(self, ctx, word):
        """Search for a random piece of work to make your day"""
        cleanquery = urllib.parse.quote(word)
        url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/" + cleanquery

        data = await self.get(url)
        if len(data) < 3:
            await ctx.send("No results found, please try again")
        else:
            data = str(data[0])
            await ctx.send(data)
