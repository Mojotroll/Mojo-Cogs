import re
import aiohttp
import discord
from discord.ext import commands
from __main__ import send_cmd_help
try:   # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
try:   # Check if Tabulate is installed
    from tabulate import tabulate
    tabulateAvailable = True
except:
    tabulateAvailable = False


class bschar:
    """Character Search for Blade and Soul! Using BNSCoffee Character Search, show these guys some love!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def bs(self, ctx):
        """List of Options Avaliable for the Blade and Soul NA/EU Character Search."""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @bs.command(name="na", pass_context=False)  # NA Command Start
    async def _NA_BS(self, name):

        if len(name) > 1:
            url = "http://www.bnscoffee.com/character/NA/{name}".format(name=name.replace('_', '%20'))  # they allow spaces so I had to add underscore as a temporary resolution
            async with aiohttp.get(url) as response:
                soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:  # Looking for results, I am pulling all current needed fields per 6v6 and PvE
                CN = soupObject.find(class_='signature').find("span", 'name').get_text()
                #CN = soupObject.find(class_='profileAccount').find_all('p')[1].find('small').find('b').get_text()
                fixCN = re.sub('[^\w]', '', CN)
                img = soupObject.find(class_='signature').find(class_='desc').find_all('li')[0].get_text()
                LV = soupObject.find(class_='signature').find(class_="desc").find_all('li')[1].get_text()
                svr = soupObject.find(class_='signature').find(class_="desc").find_all('li')[2].get_text()
                fct = soupObject.find(class_='signature').find(class_="desc").find_all('li')[3].get_text()
                if fct is None:
                    fct = 'No Faction'
                else:
                    fct = soupObject.find(class_='signature').find(class_="desc").find_all('li')[3].get_text()
                gld = soupObject.find(class_='signature').find(class_="guild")
                if gld is None:
                    gld = 'No Guild'
                else:
                    gld = soupObject.find(class_='signature').find(class_="guild").get_text()
                AP = soupObject.find("div", 'attack').find("h3").find("span", 'stat-point').get_text()
                PRC = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[2].find("span", 'stat-point').get_text()
                ACC = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[3].find("span", 'stat-point').get_text()
                CH = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[5].find("span", 'stat-point').get_text()
                CD = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[6].find("span", 'stat-point').get_text()
                HP = soupObject.find(class_='defense').find("h3").find(class_="stat-point").get_text()
                Def = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[1].find(class_='stat-point').get_text()
                Eva = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[3].find(class_='stat-point').get_text()
                Blo = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[4].find(class_='stat-point').get_text()
                CrD = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[5].find(class_='stat-point').get_text()
                WP = soupObject.find(class_='wrapWeapon').find(class_='name').find('span').get_text()
                NK = soupObject.find(class_='wrapAccessory necklace').find(class_='name').find('span').get_text()
                ER = soupObject.find(class_='wrapAccessory earring').find(class_='name').find('span').get_text()
                RN = soupObject.find(class_='wrapAccessory ring').find(class_='name').find('span').get_text()
                BCL = soupObject.find(class_='wrapAccessory bracelet').find(class_='name').find('span').get_text()
                BLT = soupObject.find(class_='wrapAccessory belt').find(class_='name').find('span').get_text()
                SL = soupObject.find(class_='wrapAccessory soul').find(class_='name').find('span').get_text()
                CLT = soupObject.find(class_='wrapAccessory clothes').find(class_='name').find('span').get_text()
                WUT = soupObject.find(class_='wrapAccessory tire').find(class_='name').find('span').get_text()
                FCD = soupObject.find(class_='wrapAccessory faceDecoration').find(class_='name').find('span').get_text()
                CLD = soupObject.find(class_='wrapAccessory clothesDecoration').find(class_='name').find('span').get_text()
                pic = soupObject.find(class_='charaterView').find('img').get('src')
                if pic is None:
                    pic = 'https://www.southhills.edu/wp-content/uploads/2015/07/no-image-available.png'
                else:
                    pic = soupObject.find(class_='charaterView').find('img').get('src')
                thumb = soupObject.find(class_='classThumb').find('img').get('src')

                # Color lookup for classes for embed message
                color_value = self.color_lookup(img)

                # Here is where I make the Tables, I separated them out because holy crap thats a lot of info
                table1 = tabulate([["Name:", fixCN], ["Class:", img], ["Lvl:", LV], ["Server:", svr], ["Faction:", fct], ["Guild:", gld]], stralign='center')
                table2 = tabulate([["[AP]", int(AP)], ["[Prc]", int(PRC)], ["[ACC]", int(ACC)], ["[Crit]", int(CH)], ["[Crit Dmg]", int(CD)], ["[HP]", int(HP)], ["[Def]", int(Def)], ["[Eva]", int(Eva)], ["[Block]", int(Blo)], ["[Crit Def]", int(CrD)]], stralign='left')
                table3 = tabulate([["Weapon:", WP], ["Neck:", NK], ["Earring:", ER], ["Ring:", RN], ["Bracelet:", BCL], ["Belt:", BLT], ["Soul:", SL], ["Clothes:", CLT], ["Head:", WUT], ["Face:", FCD], ["Other:", CLD]])

                # Create the embeded message
                embed = discord.Embed(colour=color_value, description='Your NA Search Results, powered by BNSCoffee')
                embed.title = "BNS Coffee"
                embed.url = 'http://bnscoffee.com/'
                embed.set_thumbnail(url="{thumb}".format(thumb=thumb))
                #embed.set_thumbnail(url='http://static.bladeandsoul.com/img/global/footer-bns-logo.png')
                embed.set_image(url="{pic}".format(pic=pic))
                embed.add_field(name="Character Info", value=table1)
                #embed.add_field(name="Stats", value=table2)
                embed.add_field(name="Stats", value="```ini\n{}```".format(table2))
                embed.add_field(name="Equipment", value=table3)
                await self.bot.say(embed=embed)  # Print this information :D
            except:
                await self.bot.say("Couldn't find requested character's information. No character exists or there's an error.")  # oh holy crap we have a houston!

    @bs.command(name="eu", pass_context=False)  # NA Command Start
    async def _EU_BS(self, name):

        if len(name) > 1:
            url = "http://www.bnscoffee.com/character/EU/{name}".format(name=name.replace('_', '%20'))  # they allow spaces so I had to add underscore as a temporary resolution
            async with aiohttp.get(url) as response:
                soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:  # Looking for results, I am pulling all current needed fields per 6v6 and PvE
                CN = soupObject.find(class_='signature').find("span", 'name').get_text()
                fixCN = re.sub('[^\w]', '', CN)
                img = soupObject.find(class_='signature').find(class_='desc').find_all('li')[0].get_text()
                LV = soupObject.find(class_='signature').find(class_="desc").find_all('li')[1].get_text()
                svr = soupObject.find(class_='signature').find(class_="desc").find_all('li')[2].get_text()
                fct = soupObject.find(class_='signature').find(class_="desc").find_all('li')[3].get_text()
                if fct is None:
                    fct = 'No Faction'
                else:
                    fct = soupObject.find(class_='signature').find(class_="desc").find_all('li')[3].get_text()
                gld = soupObject.find(class_='signature').find(class_="guild")
                if gld is None:
                    gld = 'No Guild'
                else:
                    gld = soupObject.find(class_='signature').find(class_="guild").get_text()
                AP = soupObject.find("div", 'attack').find("h3").find("span", 'stat-point').get_text()
                PRC = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[2].find("span", 'stat-point').get_text()
                ACC = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[3].find("span", 'stat-point').get_text()
                CH = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[5].find("span", 'stat-point').get_text()
                CD = soupObject.find("div", 'attack').find(class_='stat-define').find_all('dt')[6].find("span", 'stat-point').get_text()
                HP = soupObject.find(class_='defense').find("h3").find(class_="stat-point").get_text()
                Def = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[1].find(class_='stat-point').get_text()
                Eva = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[3].find(class_='stat-point').get_text()
                Blo = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[4].find(class_='stat-point').get_text()
                CrD = soupObject.find(class_='defense').find(class_='stat-define').find_all("dt")[5].find(class_='stat-point').get_text()
                WP = soupObject.find(class_='wrapWeapon').find(class_='name').find('span').get_text()
                NK = soupObject.find(class_='wrapAccessory necklace').find(class_='name').find('span').get_text()
                ER = soupObject.find(class_='wrapAccessory earring').find(class_='name').find('span').get_text()
                RN = soupObject.find(class_='wrapAccessory ring').find(class_='name').find('span').get_text()
                BCL = soupObject.find(class_='wrapAccessory bracelet').find(class_='name').find('span').get_text()
                BLT = soupObject.find(class_='wrapAccessory belt').find(class_='name').find('span').get_text()
                SL = soupObject.find(class_='wrapAccessory soul').find(class_='name').find('span').get_text()
                CLT = soupObject.find(class_='wrapAccessory clothes').find(class_='name').find('span').get_text()
                WUT = soupObject.find(class_='wrapAccessory tire').find(class_='name').find('span').get_text()
                FCD = soupObject.find(class_='wrapAccessory faceDecoration').find(class_='name').find('span').get_text()
                CLD = soupObject.find(class_='wrapAccessory clothesDecoration').find(class_='name').find('span').get_text()
                pic = soupObject.find(class_='charaterView').find('img').get('src')
                if pic is None:
                    pic = 'https://www.southhills.edu/wp-content/uploads/2015/07/no-image-available.png'
                else:
                    pic = soupObject.find(class_='charaterView').find('img').get('src')
                thumb = soupObject.find(class_='classThumb').find('img').get('src')

                # Color lookup for classes for embed message
                color_value = self.color_lookup(img)

                # Here is where I make the Tables, I separated them out because holy crap thats a lot of info
                table1 = tabulate([["Name:", fixCN], ["Class:", img], ["Lvl:", LV], ["Server:", svr], ["Faction:", fct], ["Guild:", gld]], stralign='center')
                table2 = tabulate([["[AP]", int(AP)], ["[Prc]", int(PRC)], ["[ACC]", int(ACC)], ["[Crit]", int(CH)], ["[Crit Dmg]", int(CD)], ["[HP]", int(HP)], ["[Def]", int(Def)], ["[Eva]", int(Eva)], ["[Block]", int(Blo)], ["[Crit Def]", int(CrD)]], stralign='left')
                table3 = tabulate([["Weapon:", WP], ["Neck:", NK], ["Earring:", ER], ["Ring:", RN], ["Bracelet:", BCL], ["Belt:", BLT], ["Soul:", SL], ["Clothes:", CLT], ["Head:", WUT], ["Face:", FCD], ["Other:", CLD]])

                # Create the embeded message
                embed = discord.Embed(colour=color_value, description='Your EU Search Results, powered by BNSCoffee')
                embed.title = "BNS Coffee"
                embed.url = 'http://bnscoffee.com/'
                embed.set_thumbnail(url="{thumb}".format(thumb=thumb))
                #embed.set_thumbnail(url='http://static.bladeandsoul.com/img/global/footer-bns-logo.png')
                embed.set_image(url="{pic}".format(pic=pic))
                embed.add_field(name="Character Info", value=table1)
                #embed.add_field(name="Stats", value=table2)
                embed.add_field(name="Stats", value="```ini\n{}```".format(table2))
                embed.add_field(name="Equipment", value=table3)
                await self.bot.say(embed=embed)  # Print this information :D
            except:
                await self.bot.say("Couldn't find requested character's information. No character exists or there's an error.")  # oh holy crap we have a houston!

    def color_lookup(self, img):
        color_dict = {"Blade Master": 0x707B7C, "Destroyer": 0x7B241C, "Summoner": 0x145A32, "Force Master": 0x1B4F72,
                      "Kung Fu Master": 0x641E16, "Assassin": 0x17202A, "Blade Dancer": 0xB03A2E, "Warlock": 0x6C3483,
                      "Soul Fighter": 0x5DADE2}
        if img in color_dict.keys():
            color = color_dict[img]
            return color
        else:
            return 0x000000


def setup(bot):
    if soupAvailable is False:
        raise RuntimeError("You don't have BeautifulSoup installed, run\n```pip3 install bs4```And try again")
        return
    if tabulateAvailable is False:
        raise RuntimeError("You don't have tabulate installed, run\n```pip3 install tabulate```And try again")
        return
    bot.add_cog(bschar(bot))
