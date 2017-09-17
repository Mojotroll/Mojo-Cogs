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


class hots:
    """Heroes of the Storm """
	
    def __init__(self, bot):
        self.bot = bot
		
    @commands.group(pass_context=True)
    async def alarak(self, ctx):
        """HIGHLORD OF THE TAL'DARIM"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @alarak.command(name="info", pass_context=False)
    async def _info_alarak(self):   
        """Basic Info about Alarak"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="abilities", pass_context=False)
    async def _abilities_alarak(self):   
        """Abilities for Alarak"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```"  + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```"  + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```"  + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="trait", pass_context=False)
    async def _trait_alarak(self):   
        """Trait for Alarak"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="heroics", pass_context=False)
    async def _heroics_alarak(self):   
        """Heroic Abilities for Alarak"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv1", pass_context=False)
    async def _talents1_alarak(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/79/Sustaining_Power_Icon.png?version=ed4d0b987f3e32c421525f6201691147')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5c/Extended_Lightning_Icon.png?version=6db1d4f5cfe77bcbb747d3dca36849f6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/69/Ruthless_Momentum_Icon.png?version=75d47522f5ad00934823012271f40792')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv4", pass_context=False)
    async def _talents4_alarak(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d1/Chaos_Reigns_Icon.png?version=0e74e61790742424c960bc2d193ac588')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5c/Extended_Lightning_Icon.png?version=6db1d4f5cfe77bcbb747d3dca36849f6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/95/Show_of_Force_Icon.png?version=38e1b12be5424eb4d9ffaed20308718f')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv7", pass_context=False)
    async def _talents7_alarak(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d1/Chaos_Reigns_Icon.png?version=0e74e61790742424c960bc2d193ac588')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/cf/Hindered_Motion_Icon.png?version=7147b3c0965b45a0505075ec722f494c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d1/Applied_Force_Icon.png?version=50f295cab00afd471f3acc419cd61eec')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv13", pass_context=False)
    async def _talents13_alarak(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/53/Blade_of_the_Highlord_Icon.png?version=dcb26805a38006466e4a012243ddfae6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/36/Pure_Malice_Icon.png?version=91c57ce5dd456acad9d4e129a57984ec')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6d/Rite_of_Rak%27Shir_Icon.png?version=ad174b6303333a5b2f3329df37a62aab')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv16", pass_context=False)
    async def _talents16_alarak(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a5/Lethal_Onslaught_Icon.png?version=3ccb6013129598940e5ba5f257d172c8')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/31/Lightning_Barrage_Icon.png?version=de94ecfbd8592dcb5d61b35aa72e49ea')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/43/Mocking_Strikes_Icon.png?version=a4a4719b3139ad30e6e719653b4ec658')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @alarak.command(name="tlv20", pass_context=False)
    async def _talents20_alarak(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Alarak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6d/Counter-Strike_Icon.png?version=8ba1e6498af68e0ee01418be0a940936')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/56/Deadly_Charge_Icon.png?version=5e7418a4617ebcf60e8481fd7d18f743')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/f/fa/Last_Laugh_Icon.png?version=85b8419988801e4113364ad5e3d20af8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/2b/Hasty_Bargain_Icon.png?version=f03f0f974f3e7e19bc15aceb2f07afc7')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
######################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def cassia(self, ctx):
        """The Nordic Warmatron"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @cassia.command(name="info", pass_context=False)
    async def _info_cassia(self):   
        """Basic Info about Cassia"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="abilities", pass_context=False)
    async def _abilities_cassia(self):   
        """Abilities for Cassia"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```"  + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```"  + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```"  + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="trait", pass_context=False)
    async def _trait_cassia(self):   
        """Trait for Cassia"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="heroics", pass_context=False)
    async def _heroics_cassia(self):   
        """Heroic Abilities for Cassia"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv1", pass_context=False)
    async def _talents1_cassia(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/56/Thunderstroke_Icon.png?version=0b5a69b0525dfd17c2ae03afdbc33c86')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/04/True_Sight_Icon.png?version=4c8f5cc6f336db099ab415c39f9b797d')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6b/Charged_Strikes_Icon.png?version=df034230929f1c8764a3e76b0a197e7e')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv4", pass_context=False)
    async def _talents4_cassia(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a8/Ring_of_the_Leech_Icon.png?version=0ab2882da19be6552bf51387863ebb4a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/54/Inner_Light_Icon.png?version=af65b199282ebf931b74da69810d59e6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/68/Plate_of_the_Whale_Icon.png?version=0abff63a651594f4486ed0d629abf06e')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv7", pass_context=False)
    async def _talents7_cassia(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/84/Impale_Cassia_Icon.png?version=a535ab96c083adfdd3bc59173068988b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/c2/War_Traveler_Icon.png?version=b2e531b986b64f02356eb27811556363')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/4a/Surge_of_Light_Icon.png?version=e005ea24af4592a1d594693bec2accc2')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv13", pass_context=False)
    async def _talents13_cassia(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b3/Grounding_Bolt_Icon.png?version=b1a980d11d1e189c564c1800951d2f77')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/f/fc/Thundergod%27s_Vigor_Icon.png?version=12ed8e899936d5c2852d6f7792386407')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/93/Seraph%27s_Hymn_Icon.png?version=f4bcf672fe4a4469aa1b33aa361f548c')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5f/Lunging_Strike_Icon.png?version=455d5dedf6acb26a1df670df5cb3b3b7')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv16", pass_context=False)
    async def _talents16_cassia(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3e/Pierce_Cassia_Icon.png?version=fd519aa01882fdb7ed177061369f213b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b1/Penetrate_Icon.png?version=cccd8cfef255840631c1ba3f1d792074')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3a/Martial_Law_Icon.png?version=bda99fa5ab59c1ada25bea60d7404fc1')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @cassia.command(name="tlv20", pass_context=False)
    async def _talents20_cassia(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Cassia"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/83/Infinite_Lightning_Icon.png?version=21eb88440df1173f5a7f1feeedc25746')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/1d/Imprisoning_Light_Icon.png?version=b15f53532c4945f4f7153f7d55162f77')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/0b/Titan%27s_Revenge_Icon.png?version=7b196ace1f6f0b4bf60bdfbca4af90ec')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")				
######################################################################################################################################################################################################################################		
    @commands.group(pass_context=True)
    async def chromie(self, ctx):
        """The Keeper of Time"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @chromie.command(name="info", pass_context=False)
    async def _info_chromie(self):   
        """Basic Info about Chromie"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="abilities", pass_context=False)
    async def _abilities_chromie(self):   
        """Abilities for Chromie"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```"  + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```"  + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```"  + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="trait", pass_context=False)
    async def _trait_chromie(self):   
        """Trait for Chromie"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="heroics", pass_context=False)
    async def _heroics_chromie(self):   
        """Heroic Abilities for Chromie"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv1", pass_context=False)
    async def _talents1_chromie(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d8/Compounding_Aether_Icon.png?version=39e4b044d6035290c31890d6b6a78c91')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b9/Deep_Breathing_Icon.png?version=bfb0988ff13cb0e4e9c3f9a5a33bd1d2')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6a/Peer_Into_The_Future_Icon.png?version=4c7c9af8ee03b1e13066697ce4613b07')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv2", pass_context=False)
    async def _talents2_chromie(self):   
        """Level 2 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/dd/Piercing_Sands_Icon.png?version=3ad95b450b0420df01d053b86fd6994d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/ba/Bronze_Talons_Icon.png?version=b49b537040d5766911d3119e7bddc5d5')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/e9/Enveloping_Assault_Icon.png?version=aa45d4858d62f625e11033bc4ed497a8')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv5", pass_context=False)
    async def _talents5_chromie(self):   
        """Level 5 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/41/Mobius_Loop_Icon.png?version=78b988ab7ed06fdbaa76a9f7fc014a89')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/e5/Dragon%27s_Eye_Icon.png?version=5101c7a0bc1054c595f002d72eccf584')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/51/Chrono_Sickness_Icon.png?version=d8d4c537a2e02b32471ae3ec953074e1')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv11", pass_context=False)
    async def _talents13_chromie(self):   
        """Level 11 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/8d/Bye_Bye_Icon.png?version=8aaf4fbc6629fd60dfa05b8cc2c39089')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/76/Reaching_through_Time_Icon.png?version=d48b1db9f285b67ffb79e0b59ef5d1dd')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/eb/Time_Out_Icon.png?version=cc262e237fed5e4a18e56fe63f4f8565')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv14", pass_context=False)
    async def _talents14_chromie(self):   
        """Level 14 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/07/Shifting_Sands_Icon.png?version=e52cd9d95c8a4ea62fa92edf719a1f95')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/f/fc/Fast_Forward_Icon.png?version=8354a7104b2a47e11b1dab5159f96619')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/97/Quantum_Overdrive_Icon.png?version=908e46ec11e5c7deddb945ca521a6d4d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @chromie.command(name="tlv18", pass_context=False)
    async def _talents18_chromie(self):   
        """Level 18 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Chromie"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/97/Pocket_of_Time_Icon.png?version=ed5a7b56220e011c48777eb9b4af844a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/8d/Loophole_Icon.png?version=811908d23e5c0227df92b0285d56b04f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/0c/Past_and_Future_Me_Icon.png?version=ee316799d1a50dc6411b1bdb55e8f16a')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/ad/Andorhal_Anomaly_Icon.png?version=e8dd2a5c860ef17751e8b90b4a3baf9e')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")	
###############################################################################################################################################################################################################################################	
    @commands.group(pass_context=True)
    async def falstad(self, ctx):
        """The Wildhammer Thane"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @falstad.command(name="info", pass_context=False)
    async def _info_falstad(self):   
        """Basic Info about Falstad"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="abilities", pass_context=False)
    async def _abilities_falstad(self):   
        """Abilities for Falstad"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```"  + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```"  + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```"  + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="trait", pass_context=False)
    async def _trait_falstad(self):   
        """Trait for Falstad"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")

    @falstad.command(name="mount", pass_context=False)
    async def _mount_falstad(self):   
        """Mount for Falstad"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            mount = skill.find_all(class_='skill')[6]
			
            timg = mount.find(class_='skill-image').find('img').get('src')
            tname = mount.find(class_='skill-heading').find('span').get_text()
            tdesc = mount.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Mount"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="heroics", pass_context=False)
    async def _heroics_falstad(self):   
        """Heroic Abilities for Falstad"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv1", pass_context=False)
    async def _talents1_falstad(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/e6/Gathering_Storm_Icon.png?version=299cca830b58e3e13b63052af37d3acc')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/2f/Seasoned_Marksman_Icon.png?version=85cca0454b198d26d5f6b37baf9e0d08')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3f/Bribe_Icon.png?version=f55d9b2cb1d1200311c0960217e3eb27')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv4", pass_context=False)
    async def _talents4_falstad(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5c/Static_Shield_Icon.png?version=e050fb560cf4442d22975efbff2692c5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/62/Updraft_Icon.png?version=31b3745e476c8572400a2c3f2b7f43b0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/f/f3/Hammer_Gains_Icon.png?version=7d07aff447f031f71bf7d55a51cfd0be')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv7", pass_context=False)
    async def _talents7_falstad(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/c1/Secret_Weapon_Icon.png?version=3de4a4fa98d6d658a87971918aceb431')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/2a/BOOMerang_Icon.png?version=a25d4ed69db0c4af2d5e91f789bddb63')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/97/Charged_Up_Icon.png?version=07f933b93ea613cef886257f0dd78a90')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv13", pass_context=False)
    async def _talents13_falstad(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b6/Thunderstrikes_Icon.png?version=2fcd0049abf8ba7e508294e62a1e25aa')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b4/Flow_Rider_Icon.png?version=644d9bbe83cedfa96dbb5affaa5cbc9c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/bd/Giant_Killer_Icon.png?version=c6fcfe06d8ee9a4ba4975bed3c77158b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv16", pass_context=False)
    async def _talents16_falstad(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a1/Crippling_Hammer_Icon.png?version=9a9bd069d420a6526f3bdf8bed6243f0')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a4/Aerie_Gusts_Icon.png?version=e889ff3db6ca7c52fc713e7e5cc3fe12')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/17/Afterburner_Icon.png?version=8706ef1d540a16ad67cf90dc9e08144f')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @falstad.command(name="tlv20", pass_context=False)
    async def _talents20_falstad(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Falstad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3d/Call_of_the_Wildhammer_Icon.png?version=39bed6f8d8cb2184c933ecf91de1afca')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d8/Wind_Tunnel_Icon.png?version=5dd49860951b432df5d1cf31234b9031')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d9/Nexus_Frenzy_Icon.png?version=bf19475140040d1eccd774275daa7313')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d8/Epic_Mount_Icon.png?version=9fa93653b271230751860ff2b2a3ad90')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")	
###############################################################################################################################################################################################################################################	
    @commands.group(pass_context=True)
    async def gall(self, ctx):
        """Twilight's Hammer"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @gall.command(name="info", pass_context=False)
    async def _info_gall(self):   
        """Basic Info about Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="abilities", pass_context=False)
    async def _abilities_gall(self):   
        """Abilities for Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="trait", pass_context=False)
    async def _trait_gall(self):   
        """Trait for Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")

    @gall.command(name="mount", pass_context=False)
    async def _mount_gall(self):   
        """Mount for Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            mount = skill.find_all(class_='skill')[8]
			
            timg = mount.find(class_='skill-image').find('img').get('src')
            tname = mount.find(class_='skill-heading').find('span').get_text()
            tdesc = mount.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Mount"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="Eye", pass_context=False)
    async def _eye_gall(self):   
        """Eye of Kilrogg for Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            eye = skill.find_all(class_='skill')[7]
			
            timg = eye.find(class_='skill-image').find('img').get('src')
            tname = eye.find(class_='skill-heading').find('span').get_text()
            tdesc = eye.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Eye of Kilrogg"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="heroics", pass_context=False)
    async def _heroics_gall(self):   
        """Heroic Abilities for Gall"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
            ab6 = skill.find_all(class_='skill')[6]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4desc = ab5.find(class_='skill-description').get_text()	

            ab5img = ab6.find(class_='skill-image').find('img').get('src')
            ab5sk = ab6.find(class_='skill-key').get_text()
            ab5name = ab6.find(class_='skill-heading').find('span').get_text()
            ab5cd = ab6.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab5desc = ab6.find(class_='skill-description').get_text()			

            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4desc + "```"
            mpF = "```" + ab5cd + "\n" + ab5desc + "```"			
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)
			
            embed6 = discord.Embed()
            embed6.title = "{ab5sk}".format(ab5sk=ab5sk)
            embed6.set_image(url='{ab5img}'.format(ab5img=ab5img))
            embed6.add_field(name="{ab5name}".format(ab5name=ab5name), value=mpF)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)	
            await self.bot.say(embed=embed6)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv1", pass_context=False)
    async def _talents1_gall(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d5/Shove_Icon.png?version=554303cd06ecab3fad79c4620a867695')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/31/Taskmaster_Icon.png?version=221caa91f0e28f3f1c367f206e1739c9')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/64/Eye_of_Kilrogg_Icon.png?version=dc8db1faf8acf2bb9ae5ece7a51112e1')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv4", pass_context=False)
    async def _talents4_gall(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/ea/Speed_of_Twilight_Icon.png?version=1188931d4c46d8914d946ca620a314ee')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/1f/Runic_Persistence_Icon.png?version=61f907226a4e70dcb6afb1ba2121f7d6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/57/Bomb%27s_Away_Icon.png?version=9ee0564e71eda139906c8c45f5e1b9f6')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv7", pass_context=False)
    async def _talents7_gall(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/af/Edge_of_Madness_Icon.png?version=f636cfab7618300fbb5fe49e6a010a9f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/33/Double_Trouble_Icon.png?version=23afe59c2595ac37ddd05300af80c6e8')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/7d/Ogre_Rampage_Icon.png?version=139045aa32e5bfec458fca37c9a96eaa')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv13", pass_context=False)
    async def _talents13_gall(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/af/Edge_of_Madness_Icon.png?version=f636cfab7618300fbb5fe49e6a010a9f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/88/Rising_Dread_Icon.png?version=ece94ffbf0c5b5d722849952c044cd6d')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/ea/Speed_of_Twilight_Icon.png?version=1188931d4c46d8914d946ca620a314ee')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv16", pass_context=False)
    async def _talents16_gall(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/af/Edge_of_Madness_Icon.png?version=f636cfab7618300fbb5fe49e6a010a9f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/88/Rising_Dread_Icon.png?version=ece94ffbf0c5b5d722849952c044cd6d')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/1f/Runic_Persistence_Icon.png?version=61f907226a4e70dcb6afb1ba2121f7d6')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @gall.command(name="tlv20", pass_context=False)
    async def _talents20_gall(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d1/Shadowfury_Icon.png?version=483fa0ddd3851f7be246002521ac8d5d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/00/The_Nether_Calls_Icon.png?version=1c3655b17b8b781c9ab76f731ff60dec')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/7d/Ogre_Rampage_Icon.png?version=139045aa32e5bfec458fca37c9a96eaa')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/62/Hour_of_Twilight_Icon.png?version=f3362dcf3c79586793fe9ff4784b41f4')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")	
###############################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def genji(self, ctx):
        """Cybernetic Ninja"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @genji.command(name="info", pass_context=False)
    async def _info_genji(self):   
        """Basic Info about Genji"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="abilities", pass_context=False)
    async def _abilities_genji(self):   
        """Abilities for Genji"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()					

            mpA = "```"  + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```"  + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```"  + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="trait", pass_context=False)
    async def _trait_genji(self):   
        """Trait for Genji"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="heroics", pass_context=False)
    async def _heroics_genji(self):   
        """Heroic Abilities for Genji"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv1", pass_context=False)
    async def _talents1_genji(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/31/Swift_as_the_Wind_Icon.png?version=9294ead50c12d8af147d9d263430d41a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/bd/Agile_Dismount_Icon.png?version=53372bcc1fd88460146c7701289005da')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/c4/Pathfinder_Icon.png?version=28c5b9c8f05ac1b0975cde03c5c9e189')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv4", pass_context=False)
    async def _talents4_genji(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/8a/Shuriken_Mastery_Icon.png?version=bc9fae34195c1005fb637e60733a638a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/be/Dragon_Claw_Icon.png?version=4d21f6bd46aebe8076876922857c71e3')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/ab/Strike_at_the_Heart_Icon.png?version=9385e37df5715a589ac0a90ad03e7812')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv7", pass_context=False)
    async def _talents7_genji(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/56/Augmented_Guard_Icon.png?version=e91d023a3c3caf687365e6bda2ac7eca')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3f/Perfect_Defense_Icon.png?version=c6f40d5d9a0fa455c792e0a58118a8eb')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/d/d8/Dodge_Icon.png?version=60c543fd47d7b3f558d955baa59fbe8f')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/10/Cyber_Shield_Icon.png?version=176cbf5183b0bc949da1cf269d6978ef')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv13", pass_context=False)
    async def _talents13_genji(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5b/Shingan_Icon.png?version=88b5d6eb4a0fd1419ebd2c313519cf56')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/1c/Flow_Like_Water_Icon.png?version=115696f2e64dc043852a2816d4d8e4f3')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/7d/Double_Jump_Icon.png?version=ae1703441ad637324056264839aff89e')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv16", pass_context=False)
    async def _talents16_genji(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/ae/Reflect_Icon.png?version=e34bac5d66b8c03b60e3e0775b82e9b9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/36/Final_Cut_Icon.png?version=a3874c3bec1087d4b519f00dc86165c3')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/c9/Steady_Blade_Icon.png?version=8271700845a1cf30a7db7a0fd9d3c9bb')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @genji.command(name="tlv20", pass_context=False)
    async def _talents20_genji(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Genji"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/00/The_Dragon_Becomes_Me_Icon.png?version=d58305970366c6f53a0865de6dd8fd5b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a8/Living_Weapon_Icon.png?version=4152053987d2a8434055ff0d4a9f58da')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/91/Sharpened_Stars_Icon.png?version=50a4a5c544c5945fcea0e07e04050a54')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/84/Zanshin_Icon.png?version=55310e319ad2c18d03174e52b3c6f97b')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
###############################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def greymane(self, ctx):
        """Lord of the Worgen"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @greymane.command(name="info", pass_context=False)
    async def _info_greymane(self):   
        """Basic Info about Greymane"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="abilities", pass_context=False)
    async def _abilities_greymane(self):   
        """Abilities for Greymane"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()	

            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            #ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	#Keeping this here JUUUUST in case
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	#Keeping this here JUUUUST in case
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"		
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
	
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="trait", pass_context=False)
    async def _trait_greymane(self):   
        """Trait for Greymane"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="heroics", pass_context=False)
    async def _heroics_greymane(self):   
        """Heroic Abilities for Greymane"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[6]
            ab5 = skill.find_all(class_='skill')[7]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv1", pass_context=False)
    async def _talents1_greymane(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/20/Wolfheart_Icon.png?version=3c03d3c96d80cc859f02e8b92cac74e5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3f/Perfect_Aim_Icon.png?version=de5f064ce5d7f0570654aa7ca6d8484f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/4b/Viciousness_Icon.png?version=5015996765b93f6a845e1e16f2b57229')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv4", pass_context=False)
    async def _talents4_greymane(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/68/Thick_Skin_Icon.png?version=d423e477009c8cdfbe13bcb0f21b5ce9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/c5/Eyes_in_the_Dark_Icon.png?version=87dfca70346e7eb1dacd480a4752b433')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/bf/Insatiable_Icon.png?version=d7508005840414cd57e1f2c61f8239ee')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/f/fd/Draught_Overflow_Icon.png?version=8b2e96111f49b90ed718dd5f4f32030c')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv7", pass_context=False)
    async def _talents7_greymane(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/94/Quicksilver_Bullets_Icon.png?version=b3b0cb30ffcef6931fb4f5190067caa4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6a/Incendiary_Elixir_Icon.png?version=140ce6a212606421c29be7f1f6731fcb')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/26/Wizened_Duelist_Icon.png?version=27dc804907747183c37e69a46d3616fa')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv13", pass_context=False)
    async def _talents13_greymane(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3f/Running_Wild_Icon.png?version=a45547974c9103978b0464d1128ef976')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6d/Visceral_Attacks_Icon.png?version=d1b554e245c37751e0c24e44d8cdaff2')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/56/On_the_Prowl_Icon.png?version=fa9d859ae62a3e70be6909f3502c6edf')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/92/Unfettered_Assault_Icon.png?version=cb5d6d26fe9216816010b0ea83911062')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv16", pass_context=False)
    async def _talents16_greymane(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/9a/Eager_Wolf_Icon.png?version=700eb09d9adf3273e54db864ec8f79ec')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/e0/Executioner_Icon.png?version=8f389f5e93251232c2d354d62073c9cc')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/1f/Alpha_Killer_Icon.png?version=f42b069da266451607d422a869500169')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @greymane.command(name="tlv20", pass_context=False)
    async def _talents20_greymane(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Greymane"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a6/Unleashed_Icon.png?version=b14c8ab1fbea9cd1e2fbf343e96f5799')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/b7/Gilnean_Roulette_Icon.png?version=cffd618cc2078336d28467180210e0f9')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/28/Hunter%27s_Blunderbuss_Icon.png?version=ff95755641d5dd895cb9c7020bb1bcf8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/b/bb/Tooth_and_Claw_Icon.png?version=b68e56ed09c46c874e08d7a9dab7718d')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
###############################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def guldan(self, ctx):
        """Darkness Incarnate"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @guldan.command(name="info", pass_context=False)
    async def _info_guldan(self):   
        """Basic Info about Gul'dan"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="abilities", pass_context=False)
    async def _abilities_guldan(self):   
        """Abilities for Gul'dan"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="trait", pass_context=False)
    async def _trait_guldan(self):   
        """Trait for Gul'dan"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="heroics", pass_context=False)
    async def _heroics_guldan(self):   
        """Heroic Abilities for Gul'dan"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv1", pass_context=False)
    async def _talents1_guldan(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/ae/Pursuit_of_Flame_Icon.png?version=ea787f359d017e98cc9e9a226943b7d5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/20/Glyph_of_Drain_Life_Icon.png?version=396041707e110da4ac9fbb22a0ae7597')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/95/Echoed_Corruption_Icon.png?version=7ef6823ef375795b42ad6f64943e9122')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/55/Chaotic_Energy_Icon.png?version=1867cf6b7f1d41ff124304581fcf5bb5')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv4", pass_context=False)
    async def _talents4_guldan(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/a4/Health_Funnel_Icon.png?version=ed64e7216a3e87be4cf06a6736235dd8')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/75/Improved_Life_Tap_Icon.png?version=d132c614aee67c70a4f1a53cbe41d8f8')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/00/Consume_Soul_Icon.png?version=fd8f44528b371f805a037d18ea889078')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv7", pass_context=False)
    async def _talents7_guldan(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/00/Bound_by_Shadow_Icon.png?version=0998d233c44193eb52150d4fbdca2369')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/38/Devour_the_Frail_Icon.png?version=26266aca219add8bd1ce4265467cbff5')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/32/Curse_of_Exhaustion_Icon.png?version=a16bc5c4e0fbd82e9ecfc4a81b082375')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/85/Hunger_for_Power_Icon.png?version=b3f65bb85ec1ecb447897f9aeb3ac5d0')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv13", pass_context=False)
    async def _talents13_guldan(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/89/Fel_Armor_Icon.png?version=c6a5fdd861254fbcdc4efda9a36783c1')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/cd/Harvest_Life_Icon.png?version=fa5cb58a6d573cb3ac3a45214b6cd50c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/3/3e/Dark_Bargain_Icon.png?version=41cbc32a862a4761503ccf49daaf43b1')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/73/Healthstone_Icon.png?version=ba0592678361392ccac7d572bcc8bcd0')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv16", pass_context=False)
    async def _talents16_guldan(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/ee/Rampant_Hellfire_Icon.png?version=ba12fcbbf493cda4f7b051362168b1e8')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/8/89/Ruinous_Affliction_Icon.png?version=83958b7f27f206c482befbdb00a59308')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6c/Darkness_Within_Icon.png?version=a01b4881779c9d936b3f05f71d41607f')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @guldan.command(name="tlv20", pass_context=False)
    async def _talents20_guldan(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Gul%27dan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/62/Haunt_Icon.png?version=7ac7e98676d95e8e3c5ec20c943d7963')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/97/Deep_Impact_Icon.png?version=a75b2c7a2584d18038bdde4ad3882ff9')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/4f/Demonic_Circle_Icon.png?version=feac1cb813eb58c8d398a931db0d1154')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def illidan(self, ctx):
        """The Betrayer"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @illidan.command(name="info", pass_context=False)
    async def _info_illidan(self):   
        """Basic Info about Illidan"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="abilities", pass_context=False)
    async def _abilities_illidan(self):   
        """Abilities for Illidan"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="trait", pass_context=False)
    async def _trait_illidan(self):   
        """Trait for Illidan"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="heroics", pass_context=False)
    async def _heroics_illidan(self):   
        """Heroic Abilities for Illidan"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv1", pass_context=False)
    async def _talents1_illidan(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/49/Immolation_Icon.png?version=03726584ec6ffb3d21e330bf921cbf68')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/6d/Battered_Assault_Icon.png?version=30f1d7d18506494b6c6b2be0c4763577')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/20/Unending_Hatred_Icon.png?version=273e5ce76f71d83e58b86723bb7bcc6d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv4", pass_context=False)
    async def _talents4_illidan(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/e/e1/Rapid_Chase_Icon.png?version=e631885dc7cafcfdc9a5825d84e82895')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/1/17/Friend_or_Foe_Icon.png?version=0f60abeff9f9f648018cfed6dde62186')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/01/Unbound_Icon.png?version=23d7945762f98cab3dafaa5c7092478c')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv7", pass_context=False)
    async def _talents7_illidan(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/2/23/Reflexive_Block_Icon.png?version=78804a4e50ad838cf7379b3cad779d5a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/c/cc/Thirsting_Blade_Icon.png?version=14d71d233c69ed4f024c3b3e6949cbf0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/6/66/Hunter%27s_Onslaught_Icon.png?version=fe7abfca9e99be3e6006ddc5d858505a')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv13", pass_context=False)
    async def _talents13_illidan(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/0/0e/Nimble_Defender_Icon.png?version=2ff9800f3b21d03c407e0fa151f8b374')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/a/ae/Elusive_Strike_Icon.png?version=3eb5a005fd5eb922f357076bd7667a38')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/9/98/Sixth_Sense_Icon.png?version=5f46c1d5b4dbebfbe2282571e842f11b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv16", pass_context=False)
    async def _talents16_illidan(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/71/Marked_for_Death_Icon.png?version=851df6868e62d0eff8c5871334e74952')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/4/40/Fiery_Brand_Icon.png?version=6cd933d19dd997b25d7c3b58b35d2320')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/5/5a/Blades_of_Azzinoth_Icon.png?version=89bf6f34232608ba72983f5132028c3e')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @illidan.command(name="tlv20", pass_context=False)
    async def _talents20_illidan(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Illidan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://hydra-media.cursecdn.com/heroesofthestorm.gamepedia.com/7/79/Demonic_Form_Icon.png?version=b435d6302d040a14d55429b1fbd36dc6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/62/Nowhere_to_Hide_Icon.png?version=83329dfffaa526a4cc4bbd147a5be4ef')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Bolt_of_the_Storm_Icon.png?version=5182d16aedf5509a69101d1efb9929cb')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def jaina(self, ctx):
        """The Archmage"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @jaina.command(name="info", pass_context=False)
    async def _info_jaina(self):   
        """Basic Info about Jaina"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="abilities", pass_context=False)
    async def _abilities_jaina(self):   
        """Abilities for Jaina"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="trait", pass_context=False)
    async def _trait_jaina(self):   
        """Trait for Jaina"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="heroics", pass_context=False)
    async def _heroics_jaina(self):   
        """Heroic Abilities for Jaina"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv1", pass_context=False)
    async def _talents1_jaina(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7d/Winter%27s_Reach_Icon.png?version=e1190d288af44f42f84d75214d632509')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9e/Lingering_Chill_Icon.png?version=8f790d9746618a59d0a448716686ec53')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4e/Deep_Chill_Icon.png?version=80bf87536b68a666c54d9efb90345432')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/dd/Conjurer%27s_Pursuit_Icon.png?version=408d95846a05d88ab876b29de4be03e5')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv4", pass_context=False)
    async def _talents4_jaina(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7d/Winter%27s_Reach_Icon.png?version=e1190d288af44f42f84d75214d632509')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cd/Arcane_Intellect_Icon.png?version=933c8de99cf7c857a26a081686e0577c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d0/Frost_Armor_Icon.png?version=943320d4bdcd59784060ca3d94e2f2de')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv7", pass_context=False)
    async def _talents7_jaina(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a4/Ice_Floes_Icon.png?version=ff4d8619ea5701442c5631f6bcaeebed')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/10/Frostbitten_Icon.png?version=e865b03dfedf43b1326e7fcb65c76426')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a3/Ice_Lance_Icon.png?version=6ee5ca65859aed687fe41f2746d2baaf')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv13", pass_context=False)
    async def _talents13_jaina(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/49/Storm_Front_Icon.png?version=8912c0c577c8b357febcc2daed7c1c62')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/46/Ice_Barrier_Icon.png?version=7ab82097eb6b11722a3ac1762b141369')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/42/Icy_Veins_Icon.png?version=44e1a23039bfb3d5bfa0a0ffe0921834')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv16", pass_context=False)
    async def _talents16_jaina(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/34/Snowstorm_Icon.png?version=8a1f9d750d3cbceae91f41647d764f57')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/01/Northern_Exposure_Icon.png?version=9deb606b69f23ee454963a75714ddd79')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/74/Numbing_Blast_Icon.png?version=59c49eba16e3223e2ad115df3c207173')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @jaina.command(name="tlv20", pass_context=False)
    async def _talents20_jaina(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Jaina"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/86/Cold_Snap_Icon.png?version=4d83d0bc0b5c8f2ff69b019528eb9240')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/97/Wintermute_Icon.png?version=6d0a7792b7cccb9d5d50df4b8e5f2672')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9b/Improved_Ice_Block_Icon.png?version=60ad8de7aebbee32853a5137d84ffc84')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a3/Arcane_Power_Icon.png?version=b992fa0c40040f8b76dc300124bd8521')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def kaelthas(self, ctx):
        """The Sun King"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @kaelthas.command(name="info", pass_context=False)
    async def _info_kaelthas(self):   
        """Basic Info about Kael'thas"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="abilities", pass_context=False)
    async def _abilities_kaelthas(self):   
        """Abilities for Kael'thas"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="trait", pass_context=False)
    async def _trait_kaelthas(self):   
        """Trait for Kael'thas"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="heroics", pass_context=False)
    async def _heroics_kaelthas(self):   
        """Heroic Abilities for Kael'thas"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv1", pass_context=False)
    async def _talents1_kaelthas(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/75/Convection_Icon.png?version=c3b1a35bbf55e23bb614959fe41bad16')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/74/Fel_Infusion_Icon.png?version=2aaa4181b762d051cf5d42367b868f10')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/41/Mana_Addict_Icon.png?version=b7f636e8f14521ec531d440963ecd796')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv4", pass_context=False)
    async def _talents4_kaelthas(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/84/Nether_Wind_Icon.png?version=e317f10086069475c688a55c3d2b4ad1')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2c/Energy_Roil_Icon.png?version=f098affe093c308661ff07adbf41a4b6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6a/Mana_Tap_Icon.png?version=c10ba590536e4f7eb5dfd12e754a4d34')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv7", pass_context=False)
    async def _talents7_kaelthas(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/34/Burned_Flesh_Icon.png?version=b267ec3e9846e8774e7efbbbb28794f1')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7a/Sun_Kings_Fury_Icon.png?version=cf3ba734cbfac0aeeb8db13237065fea')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e5/Sunfire_Enchantment_Icon.png?version=a3f8d3d9a96784f6867e9b661862e48c')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv13", pass_context=False)
    async def _talents13_kaelthas(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a0/Pyromaniac_Icon.png?version=5c5589814a6bfc45a6c1083105a3a4f8')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/90/Backdraft_Icon.png?version=4cf206eff87b520d37c22b60270f9587')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1c/Fission_Bomb_Icon.png?version=8c4f08326e4c653ef2a8a9f8b5cdff7b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv16", pass_context=False)
    async def _talents16_kaelthas(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3f/Fury_of_the_Sunwell_Icon.png?version=75f4237f1c928b35f4c3b60950ef807a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/02/Twin_Spheres_Icon.png?version=4c81ea4e1ee6537b56542fa860b42cd7')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a3/Arcane_Power_Icon.png?version=b992fa0c40040f8b76dc300124bd8521')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kaelthas.command(name="tlv20", pass_context=False)
    async def _talents20_kaelthas(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kael%27thas"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/28/Rebirth_Icon.png?version=6868a46891876d445d21a1447c1827ef')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9f/Presence_Of_Mind_Icon.png?version=9cb739f2d39b9dfcfeaedb33455e8a72')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/88/Master_of_Flames_Icon.png?version=9cac7a39a2a92c6d3c087572a819487c')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/32/Flamestrike_Icon.png?version=5ccd53aa99f1db22985f42908329095f')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def kerrigan(self, ctx):
        """The Queen of Blades"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @kerrigan.command(name="info", pass_context=False)
    async def _info_kerrigan(self):   
        """Basic Info about Kerrigan"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="abilities", pass_context=False)
    async def _abilities_kerrigan(self):   
        """Abilities for Kerrigan"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="trait", pass_context=False)
    async def _trait_kerrigan(self):   
        """Trait for Kerrigan"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="heroics", pass_context=False)
    async def _heroics_kerrigan(self):   
        """Heroic Abilities for Kerrigan"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv1", pass_context=False)
    async def _talents1_kerrigan(self):   
        """Level 1 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2b/Siphoning_Impact_Icon.png?version=dd9c9282149f08bf994e36512d019bc4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/39/Sharpened_Blades_Icon.png?version=01031b856bb0bdf1e9f9817f04461316')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/28/Energizing_Grasp_Icon.png?version=2eec3ea2552f29780ebfaf3b4e612d52')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/53/Block_Icon.png?version=ce8c2cda2e2b84ad3cceec15d1d71bfe')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv4", pass_context=False)
    async def _talents4_kerrigan(self):   
        """Level 4 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/30/Clean_Kill_Icon.png?version=e5d2b3bc7f9107498599b3b19b65d078')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/91/Psionic_Pulse_Icon.png?version=bd3cada332237f27a7199dd4db8a4408')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/22/Fury_of_the_Swarm_Icon.png?version=dbd7c36b679d8d72a464aa3267b5ddd0')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/25/Envenom_Icon.png?version=dba30cd814f0b80dc818684c983cf6db')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv7", pass_context=False)
    async def _talents7_kerrigan(self):   
        """Level 7 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/65/Adaptation_Icon.png?version=489bc7ac9536176da3baf892b36af67c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ea/Blade_Torrent_Icon.png?version=a170cb14a3812be291885c2cead40963')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0b/Assimilation_Mastery_Icon.png?version=1f969aa607e9ab17edc176073b07f572')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cf/Bladed_Momentum_Icon.png?version=24e10fc5b1cb7d349e64363c98c30083')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv13", pass_context=False)
    async def _talents13_kerrigan(self):   
        """Level 13 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/34/Lingering_Essence_Icon.png?version=085ebbab96b6aaf2edb9904bb3d3d794')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/44/Eviscerate_Icon.png?version=acbeb9af52e484d8380aa9174d2bbdf8')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8b/Double_Strike_Icon.png?version=7324c3eefbdead598903f627a4536b86')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3e/Queen%27s_Rush_Icon.png?version=cbac00514c84768a57d0d5e884e937bc')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv16", pass_context=False)
    async def _talents16_kerrigan(self):   
        """Level 16 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/76/Aggressive_Defense_Icon.png?version=701fadee1f3a1e87cf07adc8a62f7c1b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a4/Essence_for_Essence_Icon.png?version=2d51e255e30ef4c4bec021bab222bd74')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c0/Overdrive_Icon.png?version=ae7760a0b6857ff03a553dc61365d948')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kerrigan.command(name="tlv20", pass_context=False)
    async def _talents20_kerrigan(self):   
        """Level 20 Talents"""
        url = "http://heroesofthestorm.gamepedia.com/Kerrigan"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/24/Omegastorm_Icon.png?version=c51662ff0f4620e0bd0b60943b2f3a14')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e5/Torrasque_Icon.png?version=f6b7912190c4ae6d6b6ef3c33935ad9b')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Bolt_of_the_Storm_Icon.png?version=5182d16aedf5509a69101d1efb9929cb')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def liming(self, ctx):
        """The Rebellious Wizard"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @liming.command(name="info", pass_context=False)
    async def _info_liming(self):   
        """Basic Info about Li-Ming"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="abilities", pass_context=False)
    async def _abilities_liming(self):   
        """Abilities for Li-Ming"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="trait", pass_context=False)
    async def _trait_liming(self):   
        """Trait for Li-Ming"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="heroics", pass_context=False)
    async def _heroics_liming(self):   
        """Heroic Abilities for Li-Ming"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv1", pass_context=False)
    async def _talents1_liming(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1f/Astral_Presence_Icon.png?version=a36dadbdd2aea757f8c99c2b6c65748b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2a/Power_Hungry_Icon.png?version=da9f83a83887c806a9fc843d2caea617')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/02/Force_Armor_Icon.png?version=ca87df34c5f77ca327c0c88b8b97b9a0')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/03/Aether_Walker.png?version=3668fd5bd7893e42a8d145c243dd7e6a')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv4", pass_context=False)
    async def _talents4_liming(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ee/Charged_Blast_Icon.png?version=20df2b177469067a6bbc659f6a58f5c5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fb/Triumvirate_Icon.png?version=a9784fd927d5d82226cd5a445657e949')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/26/Dominance_Icon.png?version=daf37c82b05c9fbc1df425801b2bad00')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv7", pass_context=False)
    async def _talents7_liming(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/44/Seeker_Icon.png?version=0610337357d748e9397882f84d93769a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3a/Zeis_Vengeance_Icon.png?version=4771fe5978503c831f2427e8021b1b8b')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cc/Calamity_Icon.png?version=0a4e4ee6f7e0117a555228a2041d9eec')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv13", pass_context=False)
    async def _talents13_liming(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c8/Cannoneer_Icon.png?version=5952ac4d3af4dc0c8893708344678fbb')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/87/Glass_Cannon_Icon.png?version=8d68871322b1c76173250e54b5509b0a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/19/Illusionist_Icon.png?version=65e6adaa5cabe5f17ce113a8717347d7')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv16", pass_context=False)
    async def _talents16_liming(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
            tl4 = t6.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cb/Fireflies_Icon.png?version=fbe962f2cbc6828e3ed0a15e26185bb4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/84/Mirrorball_Icon.png?version=ba93b77bf42650b74618eb791daaecc0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d5/Arcane_Orbit_Icon.png?version=b90f5b524b8a5db5f44d50f8ecddcb76')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/25/Diamond_Skin_Icon.png?version=78c19a8cfd48fdcd2a5c3fb0432f333e')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @liming.command(name="tlv20", pass_context=False)
    async def _talents20_liming(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Li-Ming"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1b/Temporal_Flux_Icon.png?version=db36c84892c1da2ba49ce1a7020b03e6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0e/Repulsion_Icon.png?version=9d2031ebbf3e70c6afa398c87c82b351')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Tal_Rashas_Elements.png?version=07e124a029b1e69246c511f65917ce7d')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6d/Archon_Pure_Power_Icon.png?version=fe0c2ba694d9dbba801705994216d8c0')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")			
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def lunara(self, ctx):
        """The First Daughter of Cenarius"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @lunara.command(name="info", pass_context=False)
    async def _info_lunara(self):   
        """Basic Info about Lunara"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="abilities", pass_context=False)
    async def _abilities_lunara(self):   
        """Abilities for Lunara"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
            ab4 = skill.find_all(class_='skill')[4]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()	
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()	
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()	
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()	

            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()		
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()				

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"			
            mpD = "```" + ab3cd + "\n" + ab3desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="trait", pass_context=False)
    async def _trait_lunara(self):   
        """Trait for Lunara"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")

    @lunara.command(name="mount", pass_context=False)
    async def _mount_lunara(self):   
        """Mount for Lunara"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            mount = skill.find_all(class_='skill')[7]
			
            timg = mount.find(class_='skill-image').find('img').get('src')
            tname = mount.find(class_='skill-heading').find('span').get_text()
            tdesc = mount.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Mount"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="heroics", pass_context=False)
    async def _heroics_lunara(self):   
        """Heroic Abilities for Lunara"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[5]
            ab5 = skill.find_all(class_='skill')[6]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()			

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"		
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv1", pass_context=False)
    async def _talents1_lunara(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9b/Blossom_Swell_Icon.png?version=13f3b6d2d4bec9b35507dfbb2ddd90b9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/79/Photosynthesis_Icon.png?version=45c99927ad40facf30269e633761413f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/54/Natural_Perspective_Icon.png?version=b95ea2ed593c718f22b2ab7e45179e73')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl3name}".format(tl3name=tl3name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2e/Cruel_Spores_Icon.png?version=b8b2cfe648dee18255f9a5af395c5680')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv4", pass_context=False)
    async def _talents4_lunara(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e4/Nimble_Wisp_Icon.png?version=200db259a8b09550c419167c978ec685')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6a/Timelost_Wisp_Icon.png?version=515280f80ecae41612dbb2cdeb96769b')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Skybound_Wisp_Icon.png?version=03efd811601d44321ca7bfff88ee41ba')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3b/Dividing_Wisp_Icon.png?version=17c79dbbfe668f61ad125bee97fee07f')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv7", pass_context=False)
    async def _talents7_lunara(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/19/Siphoning_Toxin_Icon.png?version=95dc341d55cfb86126bcde0ef6ab7c45')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/66/Wild_Vigor_Icon.png?version=191010e772c35c76479d520e145676f3')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b8/Splintered_Spear_Icon.png?version=30d5de35425fc416dcf993c78eceb1d8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e8/Nature%27s_Culling_Icon.png?version=d5bdf8baa9b4f6362e25336871158138')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv13", pass_context=False)
    async def _talents13_lunara(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/15/Pestering_Blossom_Icon.png?version=e614ec00b90f2d4ca31904b9b0f3e564')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/23/Unfair_Advantage_Icon.png?version=b4babd79fca911bae9455ebbff89486d')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bd/Giant_Killer_Icon.png?version=263665046749adbc51a7830777c4f585')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d3/Greater_Spell_Shield_Icon.png?version=cf693e79eb9d1f230ebaf30ee98cfdf7')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv16", pass_context=False)
    async def _talents16_lunara(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
            tl4 = t6.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f5/Choking_Pollen_Icon.png?version=d8257c23bd7bcb0556ebefa76521ef3a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/00/Star_Wood_Spear_Icon.png?version=9092bfe1d71bd45fe00208b1c39d48c1')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/19/Invigorating_Spores_Icon.png?version=311813c1764369078b9543b43715beea')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f9/Let_Them_Wither_Icon.png?version=9f70f9ed2f556ff55fc5441003e1c77e')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @lunara.command(name="tlv20", pass_context=False)
    async def _talents20_lunara(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Lunara"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e8/Forest%27s_Wrath_Icon.png?version=b5741e64f0300c75a2c4a90b9416bbe5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6b/Boundless_Stride_Icon.png?version=750452362e2d3f69fc74f22f2a96d439')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/48/Galloping_Gait_Icon.png?version=8458a98faf399b4846887dc4cb81ccb5')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/86/Abolish_Magic_Icon.png?version=f12ef5ed7b871898c2a1062cfbce2140')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")	
##################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def malthael(self, ctx):
        """The Aspect of Death"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @malthael.command(name="info", pass_context=False)
    async def _info_malthael(self):   
        """Basic Info about Malthael"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="abilities", pass_context=False)
    async def _abilities_malthael(self):   
        """Abilities for Malthael"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="trait", pass_context=False)
    async def _trait_malthael(self):   
        """Trait for Malthael"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="heroics", pass_context=False)
    async def _heroics_malthael(self):   
        """Heroic Abilities for Malthael"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv1", pass_context=False)
    async def _talents1_malthael(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1c/Death%27s_Reach_Icon.png?version=ce0d16991775a2515c5584c6ba71f9f3')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/On_a_Pale_Horse_Icon.png?version=30be69ae0b175afaae4637609d75e793')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4b/Fear_the_Reaper_Icon.png?version=0a3a0cd72f56a2431c620293db22b7ba')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv4", pass_context=False)
    async def _talents4_malthael(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1c/Die_Alone_Icon.png?version=da1787224b31dac64b77973e6c9d2330')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/69/Throwing_Shade_Icon.png?version=b884887c4e33b7aa56405a67208fb1fd')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1a/Black_Harvest_Icon.png?version=66ecbe7fac5bc91fae5918f6ab439807')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv7", pass_context=False)
    async def _talents7_malthael(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/06/Cold_Hand_Icon.png?version=1ce453f378c5b156aff007e7282360b7')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/79/Mortality_Icon.png?version=966188c6fdf7243bfee977567ad6dc42')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/77/Touch_of_Death_Icon.png?version=9915d517702da7472229a7a483a8792f')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv13", pass_context=False)
    async def _talents13_malthael(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/58/Soul_Siphon_Icon.png?version=52c8d8668d136514268946350c49b84c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/18/Ethereal_Existence_Icon.png?version=8d5d9bfc1ce3f77b80eb46f36f758109')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ef/Inevitable_End_Icon.png?version=10ce1f4b88c03a3dd259776aeb0ac7dc')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1e/Shroud_of_Wisdom_Icon.png?version=7b8eafd73d1e4d9ae0936971e760652a')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv16", pass_context=False)
    async def _talents16_malthael(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b5/Soul_Collector_Icon.png?version=8542ea98785fa92e3a49e9fe066ceb9a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/00/Massacre_Icon.png?version=a31df8bc6cf7a8bc4130c8b3f418f525')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0e/Memento_Mori_Icon.png?version=69e78197ce9f614f045df471a1d0d1fb')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @malthael.command(name="tlv20", pass_context=False)
    async def _talents20_malthael(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Malthael"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/73/Reaper_of_Souls_Icon.png?version=1c78fa84bb6d08002c37dbf4f93dfcd3')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/13/Angel_of_Death_Icon.png?version=4bc8808b65d6485f28189795543733be')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6f/Final_Curtain_Icon.png?version=a8e6b523d6fbb3f7e752792f2756462a')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8c/No_One_Can_Stop_Death_Icon.png?version=e840f8e6f92b314c762389704e394553')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def nova(self, ctx):
        """The Dominion Ghost"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @nova.command(name="info", pass_context=False)
    async def _info_nova(self):   
        """Basic Info about Nova"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="abilities", pass_context=False)
    async def _abilities_nova(self):   
        """Abilities for Nova"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="trait", pass_context=False)
    async def _trait_nova(self):   
        """Trait for Nova"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()						
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=tdesc)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="heroics", pass_context=False)
    async def _heroics_nova(self):   
        """Heroic Abilities for Nova"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv1", pass_context=False)
    async def _talents1_nova(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/17/Advanced_Cloaking_Icon.png?version=62f67b51692ba22fa212c1124e3a2033')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b0/Longshot_Icon.png?version=fb2e7057b22ce0e55254c3fda131b15f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/05/Covert_Ops_Icon.png?version=a1bf3f726c0ddcd0c1a0b8346c6d4d9d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv4", pass_context=False)
    async def _talents4_nova(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7b/Remote_Delivery_Icon.png?version=9dc23d47ddcc57271b5cda6b15137628')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7b/Rapid_Projection_Icon.png?version=086eb30713bf87062be8dfbfddad36ed')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e5/Holo_Stability_Icon.png?version=eb239fc04a6fd61056abf48397d065aa')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3f/Bribe_Icon.png?version=3af6c6990e3932d4e01e7872803e80f8')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv7", pass_context=False)
    async def _talents7_nova(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3e/One_in_the_Chamber_Icon.png?version=74837948de96ce4315db7f3ebc4ff254')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/07/Anti-Armor_Shells_Icon.png?version=06857e89c8a832bbd1ef56786e148af0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fb/Snipe_Master_Icon.png?version=a8ae22c9cb5151d2c4b189d6088a7536')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv13", pass_context=False)
    async def _talents13_nova(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ce/Double_Tap_Icon.png?version=7a438f8a73f8629963a415b618f940b5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/35/Psionic_Efficiency_Icon.png?version=846b29b53e9ba004ecf8ce281dabeee7')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ce/Explosive_Round_Icon.png?version=d25fe05866cca2655d164fd417d27156')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv16", pass_context=False)
    async def _talents16_nova(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/27/Perfect_Shot_Icon.png?version=6a94472a2e8fe8443dad9e5ac02206be')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ea/Crippling_Shot_Icon.png?version=e86c91f3847cb849ef1728d847b965fc')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/23/Double_Fake_Icon.png?version=45f887a68de2ee19fae46725ce12c036')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @nova.command(name="tlv20", pass_context=False)
    async def _talents20_nova(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Nova"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a4/Fast_Reload_Icon.png?version=4a29fc67ee4092183db828c61e8f2a1f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/21/Precision_Barrage_Icon.png?version=e3ae435468ea6d88c7289d2a3ef2a3a9')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Rewind_Icon.png?version=ccb98d8dd3e038c3031daf217ed40bb7')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/95/Ghost_Protocol_Icon.png?version=c680fa74de5a23b4687e03da4bbbfe37')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def ragnaros(self, ctx):
        """The Firelord"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @ragnaros.command(name="info", pass_context=False)
    async def _info_ragnaros(self):   
        """Basic Info about Ragnaros"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="abilities", pass_context=False)
    async def _abilities_ragnaros(self):   
        """Abilities for Ragnaros"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
            ab6 = skill.find_all(class_='skill')[6]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()	

            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()
			
            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()	

            ab5img = ab6.find(class_='skill-image').find('img').get('src')
            ab5sk = ab6.find(class_='skill-key').get_text()
            ab5name = ab6.find(class_='skill-heading').find('span').get_text()
            ab5cd = ab6.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab5desc = ab6.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpD = "```" + ab3cd + "\n" + ab3desc + "```"	
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
            mpF = "```" + ab5cd + "\n" + ab5desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)
			
            embed6 = discord.Embed()
            embed6.title = "{ab5sk}".format(ab5sk=ab5sk)
            embed6.set_image(url='{ab5img}'.format(ab5img=ab5img))
            embed6.add_field(name="{ab5name}".format(ab5name=ab5name), value=mpF)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)
            await self.bot.say(embed=embed5)
            await self.bot.say(embed=embed6)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="trait", pass_context=False)
    async def _trait_ragnaros(self):   
        """Trait for Ragnaros"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tcd + "\n" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="heroics", pass_context=False)
    async def _heroics_ragnaros(self):   
        """Heroic Abilities for Ragnaros"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[7]
            ab5 = skill.find_all(class_='skill')[8]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv1", pass_context=False)
    async def _talents1_ragnaros(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ca/Sulfuras_Hungers_Icon.png?version=45de6004759a1723d6aafe3c81cb45ca')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/13/Shifting_Meteor_Icon.png?version=8de2566dedd2a1bbde5465d6a521e0a2')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f5/Engulfing_Flame_Icon.png?version=a80986a674ff0e0fe61841468cd19e97')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv4", pass_context=False)
    async def _talents4_ragnaros(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/02/Fire_Ward_Icon.png?version=45d07c964d737c9cc0f30456adf4a970')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/be/Slow_Burn_Icon.png?version=4e57987087cbc0f761f41609496f03c5')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0d/Catching_Fire_Icon.png?version=9438b6374ffa86fcc49e26c02024ae65')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv7", pass_context=False)
    async def _talents7_ragnaros(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b3/Hand_of_Ragnaros_Icon.png?version=d5c71ceecd89f7fbe0bc29a07bf10701')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/80/Molten_Power_Icon.png?version=e02ed6334dbfa9197578a80e96aa1086')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/39/Superheated_Icon.png?version=183b3494c8092ea1e54c408171f3e411')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv13", pass_context=False)
    async def _talents13_ragnaros(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b1/Cauterized_Wounds_Icon.png?version=2dc72815d974d9632c137c642cd40df7')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3f/Tempered_Flame_Icon.png?version=ba982339804a3779ee1eeb8086d389db')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8d/Resilient_Flame_Icon.png?version=fb3a2c374aa19294cc02f7fd797e7b35')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv16", pass_context=False)
    async def _talents16_ragnaros(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/65/Giant_Scorcher_Ragnaros_Icon.png?version=5e9d53edacecd867bc4ff18a6f66ea85')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d3/Meteor_Bomb_Icon.png?version=3419ffb400c0878d762b50a2bb20da29')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ee/Blast_Echo_Icon.png?version=f18fd1f02e6d9af950295027131e3b05')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @ragnaros.command(name="tlv20", pass_context=False)
    async def _talents20_ragnaros(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Ragnaros"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Flames_of_Sulfuron_Icon.png?version=7b00e25df6a5444c1f04e4b55c97159c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b9/Lava_Surge_Icon.png?version=c08663c3a2291a08b481599f06d765f4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/42/Heroic_Difficulty_Icon.png?version=fe659faa42829c1de43eccdf1dfc6a16')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/92/Submerge_Icon.png?version=2d174437cb039b5da3da3a446e84db46')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################			
    @commands.group(pass_context=True)
    async def raynor(self, ctx):
        """The Renegade Commander"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @raynor.command(name="info", pass_context=False)
    async def _info_raynor(self):   
        """Basic Info about Raynor"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="abilities", pass_context=False)
    async def _abilities_raynor(self):   
        """Abilities for Raynor"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="trait", pass_context=False)
    async def _trait_raynor(self):   
        """Trait for Raynor"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="heroics", pass_context=False)
    async def _heroics_raynor(self):   
        """Heroic Abilities for Raynor"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv1", pass_context=False)
    async def _talents1_raynor(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/96/Give_Me_More%21_Icon.png?version=ffefee745edb7981458c80e62f5ac2f4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2f/Seasoned_Marksman_Icon.png?version=924f3f27956d02caa0ec86e0f1500680')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4f/Scouting_Drone_Icon.png?version=6671e630a72da6794f835c94e9ef2a7e')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv4", pass_context=False)
    async def _talents4_raynor(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ce/Focused_Attack_Icon.png?version=26e6813701e30bfb9ddc4612fb9d6ac5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/95/Vigorous_Assault_Icon.png?version=ca2674bc69e495869b2460cd0d05e975')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7f/Confident_Aim_Icon.png?version=258551541146857c487dcb1587da0cf0')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f0/Relentless_Leader_Icon.png?version=11525d694780a5f73dcad0e407a770ff')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv7", pass_context=False)
    async def _talents7_raynor(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4b/Hamstring_Shot_Icon.png?version=a80baca655c7c0c6b6ce61bae66c19d5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Revolution_Overdrive_Icon.png?version=3c697b47543dbf5832be705ca5828253')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/23/Fight_or_Flight_Icon.png?version=0a19ecb9580fb4fb8b22093a2af9837a')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/dd/Puttin%27_On_a_Clinic_Icon.png?version=00b110d70da48f921d6914e5104ff25f')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv13", pass_context=False)
    async def _talents13_raynor(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bd/Giant_Killer_Icon.png?version=263665046749adbc51a7830777c4f585')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/41/Double-Barreled_Icon.png?version=c18f04e6629bf06f1dde9341c38a8165')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d6/Steel_Resolve_Icon.png?version=dbb1fd159f40d54b01036deb4c0a7a37')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv16", pass_context=False)
    async def _talents16_raynor(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e0/Executioner_Icon.png?version=27bc5a5ac360fc827bf2a50ae107eec8')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/62/Cluster_Round_Icon.png?version=36d74de96672d13a92155262becd4047')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/52/Bullseye_Icon.png?version=1b8f48e20bea591e5cfbed95abcbe6b0')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @raynor.command(name="tlv20", pass_context=False)
    async def _talents20_raynor(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Raynor"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
            tl5 = t7.find_all(class_='matched-height talent')[4]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            tl5name = tl5.find(class_='talent-name').get_text()
            tl5desc = tl5.find(class_='talent-description').get_text()				
            mpE = "```" + tl5desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/85/Scorched_Earth_Icon.png?version=bcb50b652ce716668d14f0cef8155fb4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/31/Dusk_Wings_Icon.png?version=c7ea2b7894ff824fd9c8f7a526aef275')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/73/A_Card_to_Play_Icon.png?version=fd212c754f6a5a8ba40015a683b27fc5')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d9/Nexus_Frenzy_Icon.png?version=d1569eeaeefbc7e5362ff13e09131a74')
            embed3.add_field(name="Description", value=mpD)
			
            embed4 = discord.Embed()
            embed4.title = "{tl5name}".format(tl5name=tl5name)
            embed4.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Bolt_of_the_Storm_Icon.png?version=5182d16aedf5509a69101d1efb9929cb')
            embed4.add_field(name="Description", value=mpE)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)	
            await self.bot.say(embed=embed4)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def samuro(self, ctx):
        """The Blademaster"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @samuro.command(name="info", pass_context=False)
    async def _info_samuro(self):   
        """Basic Info about Samuro"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="abilities", pass_context=False)
    async def _abilities_samuro(self):   
        """Abilities for Samuro"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="trait", pass_context=False)
    async def _trait_samuro(self):   
        """Trait for Samuro"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="heroics", pass_context=False)
    async def _heroics_samuro(self):   
        """Heroic Abilities for Samuro"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv1", pass_context=False)
    async def _talents1_samuro(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1c/Way_of_Illusion_Icon.png?version=9ad83018ffe4d15095ebe80437d171a1')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5e/Way_of_the_Blade_Icon.png?version=d01223c85c2b8981ac733d169791ec79')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0e/Way_of_the_Wind_Icon.png?version=5e068bd8885a615ee513dbca453e69f9')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv4", pass_context=False)
    async def _talents4_samuro(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/44/Mirage_Icon.png?version=60d72dd799dbbf957c8116cecb8b8acb')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0d/One_with_the_Wind_Icon.png?version=b0166e231abedff04f005049a8001bdf')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d5/Deflection_Icon.png?version=78a21781ee8252a9ec8a001ceeb1629d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv7", pass_context=False)
    async def _talents7_samuro(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0c/Burning_Blade_Icon.png?version=e437a16c98d560c8986666348830e37d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/89/Phantom_Pain_Icon.png?version=13b9b4d7ceac4c2407abcf5fed720bde')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/62/Crushing_Blows_Icon.png?version=782797096055110f8e33a26a0af30ec0')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv13", pass_context=False)
    async def _talents13_samuro(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2a/Mirrored_Steel_Icon.png?version=e4884349797bd503917fc36aedb1bc03')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/87/Kawarimi_Icon.png?version=df1d867b87bd92f84d66f1d99a5257f4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8a/Shukuchi_Icon.png?version=4696798190bdcae190b596dfac1f2a18')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv16", pass_context=False)
    async def _talents16_samuro(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0b/Merciless_Strikes_Icon.png?version=f33fe49559ccc3dca93663ca10672228')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/27/Harsh_Winds_Icon.png?version=3142e59c93447c4a861c48e0b23a8276')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/21/Press_the_Attack_Icon.png?version=b55c88b38b4c66876bc7c85b601873d5')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @samuro.command(name="tlv20", pass_context=False)
    async def _talents20_samuro(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Samuro"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a2/Dance_of_Death_Icon.png?version=6750ae39f17c7ab610cd7d100bf7580f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/36/Three_Blade_Style_Icon.png?version=ef1c40a8e4211bc96448f5d677cc15b1')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/75/Wind_Strider_Icon.png?version=3ed9c1d930456321f9bbdde5e52a8b72')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/80/Blademasters_Pursuit_Icon.png?version=8f3603bac0d64213461d87e785940d88')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def butcher(self, ctx):
        """The Flesh Cleaver"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @butcher.command(name="info", pass_context=False)
    async def _info_butcher(self):   
        """Basic Info about The Butcher"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="abilities", pass_context=False)
    async def _abilities_butcher(self):   
        """Abilities for The Butcher"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="trait", pass_context=False)
    async def _trait_butcher(self):   
        """Trait for The Butcher"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="heroics", pass_context=False)
    async def _heroics_butcher(self):   
        """Heroic Abilities for The Butcher"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv1", pass_context=False)
    async def _talents1_butcher(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5d/Invigoration_Icon.png?version=95cbd1276a113a26350168f804e3ecbd')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/53/Block_Icon.png?version=ce8c2cda2e2b84ad3cceec15d1d71bfe')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1a/Chop_Meat_Icon.png?version=9149021375302a9261855ade39725fea')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv4", pass_context=False)
    async def _talents4_butcher(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0c/Flail_Axe_Icon.png?version=888bc63e6448b6052967a7bba263ff54')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/88/Unrelenting_Pursuit_Icon.png?version=3f2f1eb144c1c0cef3ccb17d3ae0661a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a8/Cheap_Shot_Icon.png?version=b9701e098a153137cf6a2733e9a5257b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv7", pass_context=False)
    async def _talents7_butcher(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bc/Insatiable_Blade_Icon.png?version=89cdb52fdee3fe4b68fb2c574aedf248')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/62/Victuals_Icon.png?version=1935afa99f00bd4d2b7eb92ad8938d6c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/62/Meat_Shield_Icon.png?version=7b410f9d0d6000a1cfd1e04f742fe226')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv13", pass_context=False)
    async def _talents13_butcher(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cf/Cleaver_Icon.png?version=c5e221100449ae408a11b01f954b57b9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/04/Savage_Charge_Icon.png?version=dada4e896b44bc0e2a6fdadcb86a6db5')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/71/Brutal_Strike_Icon.png?version=a15d9e50d392b4972a43661c5ea3e13d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv16", pass_context=False)
    async def _talents16_butcher(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/16/Crippling_Slam_Icon.png?version=2d2a9bcf653763189bc12639363f1d06')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e6/Enraged_Icon.png?version=17a64e80ffc44e2a3ba6c4ac26d85949')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bc/Blood_Frenzy_Icon.png?version=ef05d6f2ef1461d7b3785d46c5f18d5d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @butcher.command(name="tlv20", pass_context=False)
    async def _talents20_butcher(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/The_Butcher"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b2/Fires_of_Hell_Icon.png?version=12acd8b1b657b31ca7ea654599f0c8b4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/21/Slaughterhouse_Icon.png?version=1fe7fe54759149fff0a45f04d48877c2')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Bolt_of_the_Storm_Icon.png?version=5182d16aedf5509a69101d1efb9929cb')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def thrall(self, ctx):
        """The Warchief of the Horde"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @thrall.command(name="info", pass_context=False)
    async def _info_thrall(self):   
        """Basic Info about Thrall"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="abilities", pass_context=False)
    async def _abilities_thrall(self):   
        """Abilities for Thrall"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="trait", pass_context=False)
    async def _trait_thrall(self):   
        """Trait for Thrall"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="heroics", pass_context=False)
    async def _heroics_thrall(self):   
        """Heroic Abilities for Thrall"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv1", pass_context=False)
    async def _talents1_thrall(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d8/Echo_of_the_Elements_Icon.png?version=56257bd25bb0257d6d9cd4fc1e72ad34')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8c/Crash_Lightning_Icon.png?version=1e613b8582a28db7a5cd979b79e7b132')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/93/Rolling_Thunder_Icon.png?version=c91fd4fa6da6f4d474f4f5372aadc4cc')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv4", pass_context=False)
    async def _talents4_thrall(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2f/Feral_Resilience_Icon.png?version=50c4e1435dbc12c660fe4b3085fce94c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bd/Frostwolf_Pack_Icon.png?version=5c604a9a7d5fd9ca9b07bdc07f119c21')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/28/Mana_Tide_Icon.png?version=560aa6b89b37a1e61c20e198b8ab2338')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv7", pass_context=False)
    async def _talents7_thrall(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/da/Maelstrom_Weapon_Icon.png?version=c5b819f1e76ef8f62fb67c8ffc766956')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5c/Ancestral_Wrath_Icon.png?version=54d2c8eba9decc12dfb5525b6ed0d7eb')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Follow_Through_Icon.png?version=83af95095a828d88cf00a7013785e931')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv13", pass_context=False)
    async def _talents13_thrall(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f3/Grace_Of_Air_Icon.png?version=7bb9f54fc1691f0ea798a96486bd38d4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/45/Frostwolf%27s_Grace_Icon.png?version=f849f6208f003d0db73423f29ca263ba')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/74/Spirit_Shield_Icon.png?version=56d163a4d3c76e39595f56a748185720')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv16", pass_context=False)
    async def _talents16_thrall(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e0/Tempest_Fury_Icon.png?version=eb9230bf10f6831fc1cfb51d1d782b56')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/57/Thunderstorm_Icon.png?version=1edbaee18f8a314d2c98dafc668d8fff')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9c/Alpha_Wolf_Icon.png?version=bb66de9e49a4d9bcb403e5531d86b9d9')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @thrall.command(name="tlv20", pass_context=False)
    async def _talents20_thrall(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Thrall"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c6/Worldbreaker_Icon.png?version=b2ea815e28d04a364e4c5dd2b2cfcaa3')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a1/Earthen_Shields_Icon.png?version=c64a056e7bbb9ef54539baa2ec5de53b')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/db/Wind_Rush_Icon.png?version=c748bdf82b10b8ba5d91a8780370fa2a')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def tracer(self, ctx):
        """The Agent of Overwatch"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @tracer.command(name="info", pass_context=False)
    async def _info_tracer(self):   
        """Basic Info about Tracer"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="abilities", pass_context=False)
    async def _abilities_tracer(self):   
        """Abilities for Tracer"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cd + "\n" + ab2desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="trait", pass_context=False)
    async def _trait_tracer(self):   
        """Trait for Tracer"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tsk = trait.find(class_='skill-key').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tcd + "\n" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait({tsk})".format(tsk=tsk)
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="heroic", pass_context=False)
    async def _heroics_tracer(self):   
        """Heroic Abilities for Tracer"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()					

            mpD = "```" + ab3desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)

            await self.bot.say(embed=embed4)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv1", pass_context=False)
    async def _talents1_tracer(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/54/Pulse_Strike_Icon.png?version=7d7b86351859cfb0f546755ee83f52ca')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ef/Slipstream_Icon.png?version=c5026543862c1a9bd6ed1df8c049add4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Tracer_Rounds_Icon.png?version=9abc0ca6188a48360dde246c0d70aa43')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv4", pass_context=False)
    async def _talents4_tracer(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b2/Parting_Gift_Icon.png?version=9b8a5e1c58b63f56b244c2bd90ec71ac')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/60/Is_That_a_Health_Pack_Icon.png?version=e633d6f1fbdf44072b98c844c0d8166d')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/13/Untouchable_Icon.png?version=a920231d931d31938cd970ff4bf11d0b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv7", pass_context=False)
    async def _talents7_tracer(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/11/Jumper_Icon.png?version=181fe3a4dfe65b1aa6eb4abb92f471c2')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/03/Bullet_Time_Icon.png?version=64f7e0d1415619643f76606021dd88f1')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c1/Spatial_Echo_Icon.png?version=9a85cc5a0975fd482dc4f053085fdf1d')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv10", pass_context=False)
    async def _talents10_tracer(self):   
        """Level 10 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[3]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/37/Sticky_Bomb_Icon.png?version=0c4f994001fe2c5fcd2683aa2773a770')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/09/Quantum_Spike_Icon.png?version=c097c7d8f9fb533002ef4e943b2596d3')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a2/Pulse_Rounds_Icon.png?version=e92b748ab7efedb51b37f9938b234765')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv13", pass_context=False)
    async def _talents13_tracer(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/77/Bullet_Spray_Icon.png?version=365ff74b828c5d7842a2e34417a0f4ec')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b2/Ricochet_Icon.png?version=9252d489d7e3390d355852678dd83811')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d0/Leeching_Rounds_Icon.png?version=9feb1ffadd0263f37508b2827340b498')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv16", pass_context=False)
    async def _talents16_tracer(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/46/Sleight_of_Hand_Icon.png?version=0a928ef20eb7142b9c2bb3219ea8a143')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e8/Focus_Fire_Icon.png?version=1b502ba7de69313177deff81645c927b')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/13/Locked_and_Loaded_Icon.png?version=c545b4f939f4687bde843fc499e5b7ea')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tracer.command(name="tlv20", pass_context=False)
    async def _talents20_tracer(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tracer"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/04/Get_Stuffed%21_Icon.png?version=5fae3f1e015efcac5794e93a5030b682')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d3/Total_Recall_Icon.png?version=f916ab41a8a7a6ba23afa910d5fdcd71')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ca/Composition_B_Icon.png?version=d4083a401006b6b97a5b8131960cf23a')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def tychus(self, ctx):
        """The Notorious Outlaw"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @tychus.command(name="info", pass_context=False)
    async def _info_tychus(self):   
        """Basic Info about Tychus"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="abilities", pass_context=False)
    async def _abilities_tychus(self):   
        """Abilities for Tychus"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
            ab6 = skill.find_all(class_='skill')[6]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()			
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()	

            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()
			
            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()	

            ab5img = ab6.find(class_='skill-image').find('img').get('src')
            ab5sk = ab6.find(class_='skill-key').get_text()
            ab5name = ab6.find(class_='skill-heading').find('span').get_text()
            ab5cd = ab6.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab5desc = ab6.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"
            mpB = "```" + ab1cd + "\n" + ab1desc + "```"
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"
            mpF = "```" + ab5cd + "\n" + ab5desc + "```"			  
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)
			
            embed6 = discord.Embed()
            embed6.title = "{ab5sk}".format(ab5sk=ab5sk)
            embed6.set_image(url='{ab5img}'.format(ab5img=ab5img))
            embed6.add_field(name="{ab5name}".format(ab5name=ab5name), value=mpF)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)
            await self.bot.say(embed=embed5)
            await self.bot.say(embed=embed6)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="trait", pass_context=False)
    async def _trait_tychus(self):   
        """Trait for Tychus"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcst = trait.find(class_='skill-details').find(class_='skill-cost').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tcst + "|" + tcd + "\n" + tdesc + "```"				
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="heroics", pass_context=False)
    async def _heroics_tychus(self):   
        """Heroic Abilities for Tychus"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[7]
            ab5 = skill.find_all(class_='skill')[8]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv1", pass_context=False)
    async def _talents1_tychus(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e4/Press_the_Advantage_Icon.png?version=b66e652403ab027befa360b4649187c1')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/ac/Dash_Icon.png?version=9fa8868df768d969846e6856c11d46e4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/72/Combat_Tactician_Icon.png?version=055efabf2596b4fd350004989561cde7')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv4", pass_context=False)
    async def _talents4_tychus(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/39/In_the_Rhythm_Icon.png?version=667c711ebe5a889161722dd9a6a26b75')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b6/Fully_Loaded_Icon.png?version=8815e1267c6cc0bbd1b49ad9dcf9f0dc')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/20/The_Bigger_They_Are_Icon.png?version=6a5394c88d25e9b6c4bc94bdf809d613')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/40/Master_Assassin_Icon.png?version=fb68a0690b184c622697845f89b8469a')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv7", pass_context=False)
    async def _talents7_tychus(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b4/Quarterback_Icon.png?version=ead69b597d5b8d8ed3680df69fcc2698')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Concussion_Grenade_Icon.png?version=0c3f76d909d2c141467a84d352ab0eb8')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9e/Relentless_Soldier_Icon.png?version=dbeca9d5d1a16965264632b0e0d40025')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv13", pass_context=False)
    async def _talents13_tychus(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e7/That%27s_the_Stuff%21_Icon.png?version=362984190342017cf1051b1c0523c179')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0d/Neosteel_Coating_Icon.png?version=b5ccb409fe27f010b8443eb20476eeec')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8c/Spray_%27n%27_Pray_Icon.png?version=c4f2167c5c692ec3e92ec2c30d669d12')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv16", pass_context=False)
    async def _talents16_tychus(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/69/Titan_Grenade_Icon.png?version=44757e0ff49e1b3eec6857f8f22c8af4')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a1/Lead_Rain_Icon.png?version=fa21862c4bc0239b3c5cd3ce41107554')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Armor_Piercing_Rounds_Icon.png?version=140a8e2079b9a1fa3bbff165897b2cec')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @tychus.command(name="tlv20", pass_context=False)
    async def _talents20_tychus(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Tychus"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
		
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f5/Big_Red_Button_Icon.png?version=0d622ae184b89cef7fa77b0b9cc9fd2e')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/03/Focusing_Diodes_Icon.png?version=23997736bfe6f879315f4ebe4bf478cd')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/28/Sizzlin_Attacks_Icon.png?version=880919dfc7585e639e171af7d2a7a2b8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/04/Bob_and_Weave_Icon.png?version=3f54813d666b56669ba68de2601a3b0e')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def valeera(self, ctx):
        """The Shadow of the Uncrowned"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @valeera.command(name="info", pass_context=False)
    async def _info_valeera(self):   
        """Basic Info about Valeera"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="abilities", pass_context=False)
    async def _abilities_valeera(self):   
        """Abilities for Valeera"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
            ab6 = skill.find_all(class_='skill')[6]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()			
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()	

            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()	
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()
			
            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()	

            ab5img = ab6.find(class_='skill-image').find('img').get('src')
            ab5sk = ab6.find(class_='skill-key').get_text()
            ab5name = ab6.find(class_='skill-heading').find('span').get_text()
            ab5cst = ab6.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab5cd = ab6.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab5desc = ab6.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"
            mpF = "```" + ab5cst + "|" + ab5cd + "\n" + ab5desc + "```"			  
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)
			
            embed6 = discord.Embed()
            embed6.title = "{ab5sk}".format(ab5sk=ab5sk)
            embed6.set_image(url='{ab5img}'.format(ab5img=ab5img))
            embed6.add_field(name="{ab5name}".format(ab5name=ab5name), value=mpF)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)
            await self.bot.say(embed=embed5)
            await self.bot.say(embed=embed6)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="trait", pass_context=False)
    async def _trait_valeera(self):   
        """Trait for Valeera"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tcd + "\n" + tdesc + "```"				
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="heroics", pass_context=False)
    async def _heroics_valeera(self):   
        """Heroic Abilities for Valeera"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[7]
            ab5 = skill.find_all(class_='skill')[8]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv1", pass_context=False)
    async def _talents1_valeera(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
            tl4 = t1.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e7/Vigor_Icon.png?version=cc5124b92fbbfc93dbee8563557defda')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bb/Subtlety_Icon.png?version=fbb1387e554da38cdbc503ff5d979531')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e3/Combat_Readiness_Icon.png?version=bf0a36ad9134c4786d072e25b617013e')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7c/Crippling_Poison_Icon.png?version=a02c389c09c54e9e8dfbde8825fdb190')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv4", pass_context=False)
    async def _talents4_valeera(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ec/Relentless_Strikes_Icon.png?version=3354a03381000a9b5b4b93d17a1a5a4e')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a8/Hemorrhage_Icon.png?version=a1197560aa4ee2f85f1c1a93c5f60ca4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7b/Initiative_Icon.png?version=e1857cce203d8649a899af76a64dc249')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/56/Wound_Poison_Icon.png?version=aaf524d033c7588e23d5001cd75b5243')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv7", pass_context=False)
    async def _talents7_valeera(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ef/Mutilate_Icon.png?version=490c81746bd6d662b0bf0a979e6e28ad')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b6/Fatal_Finesse_Icon.png?version=76ac19f4cc5f8c3545d05dab12a1a811')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Slice_and_Dice_Icon.png?version=96fa5297480e789bdbf80306cb0c77a2')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/05/Assassinate_Icon.png?version=2e23e7dcba513afb7815f9dbb829fd81')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv13", pass_context=False)
    async def _talents13_valeera(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Elusiveness_Icon.png?version=28f1d1327a69a872eea11725bdc9b0ab')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5d/Death_From_Above_Icon.png?version=7c19057a81d829e04f8b151e32c2d2c6')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9e/Blind_Icon.png?version=45488a7b7699effc8a67b4f57b2b4696')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bb/Strangle_Icon.png?version=1e9ed7327be4e9abdb17ca9f44c646d5')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv16", pass_context=False)
    async def _talents16_valeera(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
            tl4 = t6.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6e/Seal_Fate_Icon.png?version=189eb4c6c4e868f9b444b9e8d101d973')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/43/Rupture_Icon.png?version=6c503994b2ae41c2b2a67d038a909fbe')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0c/Expose_Armor_Icon.png?version=bc43c9689fc5f616883b89105489bbe8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cb/Thistle_Tea_Icon.png?version=49594163940dbd97736510ac6bc8be08')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valeera.command(name="tlv20", pass_context=False)
    async def _talents20_valeera(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valeera"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/31/Adrenaline_Rush_Valeera_Icon.png?version=a3c336c56b91017eb0ce481694747be7')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bc/Enveloping_Shadows_Icon.png?version=21e1e2904dd3a3cc46185902be1e3bc1')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ec/Nightslayer_Icon.png?version=65a88946aa2f766a59a09e25bb5147c4')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def valla(self, ctx):
        """The Demon Hunter"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @valla.command(name="info", pass_context=False)
    async def _info_valla(self):   
        """Basic Info about Valla"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="abilities", pass_context=False)
    async def _abilities_valla(self):   
        """Abilities for Valla"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="trait", pass_context=False)
    async def _trait_valla(self):   
        """Trait for Valla"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	
            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="heroics", pass_context=False)
    async def _heroics_valla(self):   
        """Heroic Abilities for Valla"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv1", pass_context=False)
    async def _talents1_valla(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Monster_Hunter_Icon.png?version=0a8484d0af2dbda71bb6db50a0107ec6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/69/Caltrops_Icon.png?version=c0c9ae65cdf3d147702d3dd48742cfbc')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/22/Hot_Pursuit_Icon.png?version=8984b7e4f94e886c7b1c2955e19c09a7')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv4", pass_context=False)
    async def _talents4_valla(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/51/Puncturing_Arrow_Icon.png?version=9d447d0de682fa228a1d6f33188a10e3')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/84/Punishment_Icon.png?version=d6633e8a6cc757c8a6b8e53333574515')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6c/Creed_of_the_Hunter_Icon.png?version=1c56ac153fd66a506b34fdf27578ec42')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv7", pass_context=False)
    async def _talents7_valla(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/11/Arsenal_Icon.png?version=586be06174f80628412e1d7ae82fec9d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f0/Siphoning_Arrow_Icon.png?version=0bebe1eb372f975913fd0f356517a6ce')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8d/Repeating_Arrow_Icon.png?version=ac49062e43f0f78d99a1c4222c95101b')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv13", pass_context=False)
    async def _talents13_valla(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f0/Siphoning_Arrow_Icon.png?version=0bebe1eb372f975913fd0f356517a6ce')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cf/Tempered_by_Discipline_Icon.png?version=16e331cc2d0fa86fe452feeee4bc805a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/27/Gloom_Icon.png?version=625cc711496de4b4b6b78c1089cb618f')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv16", pass_context=False)
    async def _talents16_valla(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/18/Frost_Shot_Icon.png?version=565c221dd1d4c445a5417c3b11107f9f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/75/Seething_Hatred_Icon.png?version=90d248d225b4792ae87f35f73dcc5cd4')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/d2/Manticore_Icon.png?version=32264ce4a3073f30eb14e3e4fe06d1d8')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @valla.command(name="tlv20", pass_context=False)
    async def _talents20_valla(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Valla"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b0/Vengeance_Icon.png?version=4da0d3200f9b5707f25f28ad939b9fc5')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fe/Storm_of_Vengeance_Icon.png?version=2557dd5491404c2823fad15ccffb2f78')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7a/Rancor_Icon.png?version=f7c53c18ddb51044a2e235fa474cbef8')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/de/Farflight_Quiver_Icon.png?version=19f337f4713a31aaa3d8b8b95ba9e791')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def varian(self, ctx):
        """The High King of the Alliance"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @varian.command(name="info", pass_context=False)
    async def _info_varian(self):   
        """Basic Info about Varian"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="abilities", pass_context=False)
    async def _abilities_varian(self):   
        """Abilities for Varian"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="trait", pass_context=False)
    async def _trait_varian(self):   
        """Trait for Varian"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tcd + "\n" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="heroics", pass_context=False)
    async def _heroics_varian(self):   
        """Heroic Abilities for Varian"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
            ab6 = skill.find_all(class_='skill')[6]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()

            ab5img = ab6.find(class_='skill-image').find('img').get('src')
            ab5name = ab6.find(class_='skill-heading').find('span').get_text()	
            ab5desc = ab6.find(class_='skill-description').get_text()				

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"
            mpF = "```" + ab5desc + "```"			
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)
			
            embed6 = discord.Embed()
            embed6.title = "Passive Heroic"
            embed6.set_image(url='{ab5img}'.format(ab5img=ab5img))
            embed6.add_field(name="{ab5name}".format(ab5name=ab5name), value=mpF)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)
            await self.bot.say(embed=embed6)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv1", pass_context=False)
    async def _talents1_varian(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8f/Lion%27s_Maw_Icon.png?version=d095f44df7d77f7514201870bfb3720d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/30/Overpower_%28Varian%29_Icon.png?version=ee5ee28dfebc318397de53e650ce3c65')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7d/High_King%27s_Quest_Icon.png?version=1d47b13e2960cda727ed35cd570352fe')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv4", pass_context=False)
    async def _talents4_varian(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/23/Shield_Wall_Icon.png?version=7eba053372293cd34eed810d37a0659e')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ec/Warbringer_Icon.png?version=eaa485c183287271f93af8c6f7604a2f')
            embed1.add_field(name="Description", value=mpB)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv7", pass_context=False)
    async def _talents7_varian(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/aa/Live_by_the_Sword_Icon.png?version=c43b79a6a07cb0fc07207e6d28abb5af')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f6/Second_Wind_%28Varian%29_Icon.png?version=4b65776a74cccf5a4b99a94750deaf14')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cc/Victory_Rush_Icon.png?version=3b5fdb732849a56bf667cd4221411835')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv13", pass_context=False)
    async def _talents13_varian(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/70/Juggernaut_Icon.png?version=18abe7889821afbfc8dd5f0e727042a0')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/96/Mortal_Strike_Icon.png?version=4fd571fa445e817b79c19286d4456cec')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a6/Shattering_Throw_Icon.png?version=e6abcc1770aa2eda1d6cd01823e4e8dd')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv16", pass_context=False)
    async def _talents16_varian(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f3/Banner_of_Stormwind_Icon.png?version=52304b6d2aa6e59c83f71d385122dcdc')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4a/Banner_of_Ironforge_Icon.png?version=21abd4b7ad9cfcef2085a33f8a74a95a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8f/Banner_of_Dalaran_Icon.png?version=8e0d99b19e41810f253254229e225dd0')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @varian.command(name="tlv20", pass_context=False)
    async def _talents20_varian(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Varian"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
            tl5 = t7.find_all(class_='matched-height talent')[4]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()
            mpD = "```" + tl4desc + "```"
			
            tl5name = tl5.find(class_='talent-name').get_text()
            tl5desc = tl5.find(class_='talent-description').get_text()
            mpE = "```" + tl5desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8d/Vigilance_Icon.png?version=15f8028d5120f32afd7b99b1eb300814')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/16/Master_at_Arms_Icon.png?version=ce35138e79416227b50fa7c483627fdb')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bb/Frenzy_Icon.png?version=cd338126e058d6c5cc30db023c5ed6a0')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c5/Glory_to_the_Alliance_Icon.png?version=77d54ceae3c373ca653933682371602c')
            embed3.add_field(name="Description", value=mpD)
			
            embed4 = discord.Embed()
            embed4.title = "{tl5name}".format(tl5name=tl5name)
            embed4.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c4/Demoralizing_Shout_Icon.png?version=3f270e176667cb4be6697d0baa21c8fd')
            embed4.add_field(name="Description", value=mpE)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)
            await self.bot.say(embed=embed4)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def zeratul(self, ctx):
        """The Dark Prelate"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @zeratul.command(name="info", pass_context=False)
    async def _info_zeratul(self):   
        """Basic Info about Zeratul"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="abilities", pass_context=False)
    async def _abilities_zeratul(self):   
        """Abilities for Zeratul"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()			
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"			  
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="trait", pass_context=False)
    async def _trait_zeratul(self):   
        """Trait for Zeratul"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tcd + "\n" + tdesc + "```"				
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="heroics", pass_context=False)
    async def _heroics_zeratul(self):   
        """Heroic Abilities for Zeratul"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv1", pass_context=False)
    async def _talents1_zeratul(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c4/Greater_Cleave_Icon.png?version=fd71cfe19a6afe50a416c2a8947d1ed7')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/75/Vorpal_Blade_Icon.png?version=a3f43bd33f8d201e3e9e85b00d3cbdf0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2a/Shadow_Hunter_Icon.png?version=5d36ce2c09385bc8a434fa5236fed7f6')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv4", pass_context=False)
    async def _talents4_zeratul(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/34/Grim_Task_Icon.png?version=121a2572f57b4ad6a7ca3118dd6175bc')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a1/Rending_Cleave_Icon.png?version=afa6bca6dc5f562264e6a4d9115575ff')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/91/Combo_Slash_Icon.png?version=00b6368d05818584cda2ffd4bca4cfdd')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv7", pass_context=False)
    async def _talents7_zeratul(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/26/Wormhole_Icon.png?version=31ce97e5d432a658038130acd490a246')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/29/Slip_into_Shadow_Icon.png?version=ad390ffead35aed8a2aee3dc4a7a256a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4b/Seeker_in_the_Dark_Icon.png?version=cb80e6f2515babd762bac4589eab60be')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv13", pass_context=False)
    async def _talents13_zeratul(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f5/Shroud_of_Adun_Icon.png?version=211bf86cabe05e87e4a7c33ecfbaba5f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/86/Spell_Shield_Icon.png?version=bd2cdeec3581c0c81b60c58d8488bda1')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e1/Mending_Strikes_Icon.png?version=992ba96f03a108cb183fb94830b67640')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv16", pass_context=False)
    async def _talents16_zeratul(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/be/Master_Warp-Blade_Icon.png?version=3e451d7782906b2ebcfc28d5b36c4b1c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Void_Slash_Icon.png?version=e9345a59ce2c19e90742075447e8c727')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9a/Sentenced_to_Death_Icon.png?version=35dce87645c706c6e4417815fa399489')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zeratul.command(name="tlv20", pass_context=False)
    async def _talents20_zeratul(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zeratul"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e2/Nerazim_Fury_Icon.png?version=319e076f847611cc7802b38ab727f8d6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/53/Protective_Prison_Icon.png?version=c750f74bc6272569bd0b07f62288d23c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Rewind_Icon.png?version=ccb98d8dd3e038c3031daf217ed40bb7')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def zuljin(self, ctx):
        """The Warlord of the Amani"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @zuljin.command(name="info", pass_context=False)
    async def _info_zuljin(self):   
        """Basic Info about Zul'jin"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="abilities", pass_context=False)
    async def _abilities_zuljin(self):   
        """Abilities for Zul'jin"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()			
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"			  
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="trait", pass_context=False)
    async def _trait_zuljin(self):   
        """Trait for Zul'jin"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tsk = trait.find(class_='skill-image').find(class_='skill-key').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tdesc + "```"				
			
            embed = discord.Embed()
            embed.title = "Trait({tsk})".format(tsk=tsk)
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="heroics", pass_context=False)
    async def _heroics_zuljin(self):   
        """Heroic Abilities for Zul'jin"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```"  + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```"  + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"	
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv1", pass_context=False)
    async def _talents1_zuljin(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4f/Boneslicer_Icon.png?version=670bd52999ed212c95e35dd124b1811e')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/15/Arcanite_Axes_Icon.png?version=359595e21f980c93bdc1c34eac8e13e0')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cc/You_Want_Axe_Icon.png?version=71290d599ced3919bed8f7f890283d35')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv4", pass_context=False)
    async def _talents4_zuljin(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4f/Troll%27s_Blood_Icon.png?version=b90dd578d1f176c6dc85897fa5a56223')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c1/Let_the_Killing_Begin_Icon.png?version=c7415c115f8dac73417fa09ed444b69c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c5/Headhunter_Icon.png?version=3cf7dd3697088c03f77a10c9d091ecd4')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv7", pass_context=False)
    async def _talents7_zuljin(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/19/Vicious_Assault_Icon.png?version=0480fe6e6cdbd653c30bd9b1328eff38')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/07/Wrong_Place_Wrong_Time_Icon.png?version=40b305289f222c14abdf618b25f9b723')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/10/Recklessness_Icon.png?version=88b225c805a68cde27f3bb548f2f51c8')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv13", pass_context=False)
    async def _talents13_zuljin(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4e/Eye_of_Zul%27jin_Icon.png?version=2d49bebf6f045054d228a4d74412c3a9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7a/Forest_Medicine_Icon.png?version=4f8c3d3a514b7b07d0083e2861da5542')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3b/Voodoo_Shuffle_Icon.png?version=e78321b4dbf19beaca80d5c06acedcd2')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv16", pass_context=False)
    async def _talents16_zuljin(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2e/Swirling_Death_Icon.png?version=21de9448eb92850725c21d4814320e3d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/4b/Lacerate_Icon.png?version=2029a42075d0252acffa9ed47bf06bb2')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/ae/Ferocity_Icon.png?version=bf8b3a889c81b11e83fd9f6dcbb4f771')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @zuljin.command(name="tlv20", pass_context=False)
    async def _talents20_zuljin(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Zul%27jin"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/70/Amani_Resilience_Icon.png?version=0d1d07070421c6d56cf4b7e8b0a8d81b')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/21/Buzzsaw_Icon.png?version=02c301d869b67ae33a85e9368752908e')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/ad/Ensnare_Icon.png?version=964093632e007bdb1ce6fa88f1a4c90a')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def kelthuzad(self, ctx):
        """Archlich of Naxxramas"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @kelthuzad.command(name="info", pass_context=False)
    async def _info_kelthuzad(self):   
        """Basic Info about Kel'Thuzad"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="abilities", pass_context=False)
    async def _abilities_kelthuzad(self):   
        """Abilities for Kel'Thuzad"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="trait", pass_context=False)
    async def _trait_kelthuzad(self):   
        """Trait for Kel'Thuzad"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="heroics", pass_context=False)
    async def _heroics_kelthuzad(self):   
        """Heroic Abilities for Kel'Thuzad"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()			

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"		
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv1", pass_context=False)
    async def _talents1_kelthuzad(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/45/The_Plaguelands_Icon.png?version=76747aee04928c47782b4b8b23d02b1c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/97/Blighted_Frost_Icon.png?version=eab295d409ae119f83696e46a702e0fa')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/87/Barbed_Chains_Icon.png?version=aca8b66adda2b5f479db51bbb9498666')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv4", pass_context=False)
    async def _talents4_kelthuzad(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()		
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/48/Strip_Shields_Icon.png?version=2fa3fa81a860a549f0fc2bb4dbcbbe39')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/57/Phylactery_of_Kel%27Thuzad_Icon.png?version=cc129997aebcd912d68dbba33b334886')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/99/Armor_of_the_Archlich_Icon.png?version=6ceb2b4a6a01dcc22e0ac79957d9c9af')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv7", pass_context=False)
    async def _talents7_kelthuzad(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/05/Accelerated_Decay_Icon.png?version=2ed931dcde3e3f23e5a0007a6c1aec59')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/02/Glacial_Spike_Icon.png?version=48e28e69161d5ba1b3c3b93339f1186a')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f2/Chilling_Touch_Icon.png?version=cb01feff3a265022b05c64726b2fc9df')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv13", pass_context=False)
    async def _talents13_kelthuzad(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8b/Icy_Grasp_Icon.png?version=646af513dc6b6098823312e45841bf3d')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b3/Chains_of_Ice_Icon.png?version=bb5d13da9e6646c7a232a6eda5f216eb')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/86/Chain-Link_Icon.png?version=b08e5b585bcaa94a9382738bf55a1524')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv16", pass_context=False)
    async def _talents16_kelthuzad(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/66/Arcane_Echoes_Icon.png?version=28f295f526d1d7adb4a6b8d87a3a6321')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f5/Hungering_Cold_Icon.png?version=a77c619fa6d2b43149854d018fa954cc')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/9d/Power_of_Icecrown_Icon.png?version=d0fa891b67fc8995ec9c5e242f62fe31')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @kelthuzad.command(name="tlv20", pass_context=False)
    async def _talents20_kelthuzad(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Kel%27Thuzad"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5b/Deathchill_Icon.png?version=6290980fa2de7f8a637c45e714aaf22c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e0/Might_of_the_Scourge_Icon.png?version=4ac68e6bb8388a2bf8ec3f7f7192cb16')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/02/Shifting_Malice_Icon.png?version=31c883017149244b8ef3316626740868')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/cb/The_Damned_Return_Icon.png?version=7786ab83c1fbd4007463e1ca116e8a29')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def anubarak(self, ctx):
        """The Traitor King"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @anubarak.command(name="info", pass_context=False)
    async def _info_anubarak(self):   
        """Basic Info about Anub'arak"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="abilities", pass_context=False)
    async def _abilities_anubarak(self):   
        """Abilities for Anub'arak"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"				
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="trait", pass_context=False)
    async def _trait_anubarak(self):   
        """Trait for Anub'arak"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tdesc + "```"		
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="heroics", pass_context=False)
    async def _heroics_anubarak(self):   
        """Heroic Abilities for Anub'arak"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()			

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"		
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv1", pass_context=False)
    async def _talents1_anubarak(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1e/Assault_Scarab_Icon.png?version=f43cd69fce7e4aec6c35bea312536a0f')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/23/Dampen_Magic_Icon.png?version=05b09c12e942dc4cebf3706cad66214f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/d/dd/Regeneration_Master_Icon.png?version=af2420c518ef9bce008d65c732b58b98')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv4", pass_context=False)
    async def _talents4_anubarak(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
            tl4 = t2.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()		
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()		
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/a/a6/Bed_of_Barbs_Icon.png?version=821ec41f780af6db5379123a52d0c757')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5c/Shed_Exoskeleton_Icon.png?version=6e9f111550c152359c26484fc95756ae')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/55/Underking_Icon.png?version=9523fd17e265476030e189f5d159aa29')
            embed2.add_field(name="Description", value=mpC)

            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/04/Legion_of_Beetles_Icon.png?version=924c371bfc1a520a2112aed1e5fd00ba')
            embed3.add_field(name="Description", value=mpD)
			
            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv7", pass_context=False)
    async def _talents7_anubarak(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e8/Urticating_Spines_Icon.png?version=488afcf3ae245580acdd9ad92b3f0429')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/55/Underking_Icon.png?version=9523fd17e265476030e189f5d159aa29')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/3/3a/Leeching_Scarabs_Icon.png?version=7daff3d9dc543395854c8911b628c370')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv13", pass_context=False)
    async def _talents13_anubarak(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/99/Burning_Rage_Icon.png?version=0236afd6e0085204220e805ccd87bb79')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5c/Shed_Exoskeleton_Icon.png?version=6e9f111550c152359c26484fc95756ae')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Follow_Through_Icon.png?version=83af95095a828d88cf00a7013785e931')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv16", pass_context=False)
    async def _talents16_anubarak(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/09/Epicenter_Icon.png?version=41783d1d2c1c360a5a058e9039d4b273')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/5/5a/Debilitation_Icon.png?version=f992453f643affd5e02423be244991f7')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/1e/Beetle%2C_Juiced_Icon.png?version=a4cdc8e0232d8e785d33423e9d136051')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @anubarak.command(name="tlv20", pass_context=False)
    async def _talents20_anubarak(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Anub%27arak"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/20/Hive_Master_Icon.png?version=09279d4bbb3ca8c30d4feeaa2ae9b216')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fb/Cryptweave_Icon.png?version=c6d5091934b66ec9b141296ac2bb74ed')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/82/Hardened_Shield_Icon.png?version=3963ebea2ed34cce354e6acac5052bc5')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Rewind_Icon.png?version=ccb98d8dd3e038c3031daf217ed40bb7')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
################################################################################################################################################################################################################################################
    @commands.group(pass_context=True)
    async def artanis(self, ctx):
        """The Hierarch of the Daelaam"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)  
			
    @artanis.command(name="info", pass_context=False)
    async def _info_artanis(self):   
        """Basic Info about Artanis"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            table = soupObject.find('table', attrs={'class': "infobox2"})
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            pric = table.find_all('tr')[6]
            reld = table.find_all('tr')[7]
            stat = table.find_all('tr')[8]
            hlt = table.find_all('tr')[9]
            hreg = table.find_all('tr')[10]
            eng = table.find_all('tr')[11]
            arm = table.find_all('tr')[12]
            spd = table.find_all('tr')[13]
            ats = table.find_all('tr')[14]
            atr = table.find_all('tr')[15]
            atd = table.find_all('tr')[16]

            tname = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            price = pric.find('th').get_text()
            price1 = pric.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            htit = hlt.find('th').get_text()
            hdat = hlt.find('td').get_text()
            hregt = hreg.find('th').get_text()
            hregdat = hreg.find('td').get_text()
            ent = eng.find('th').get_text()
            endat = eng.find('td').get_text()
            armt = arm.find('th').get_text()
            armdat = arm.find('td').get_text()
            spt = spd.find('th').get_text()
            spdat = spd.find('td').get_text()
            atst = ats.find('th').get_text()
            atsdat = ats.find('td').get_text()
            atrt = atr.find('th').get_text()
            atrdat = atr.find('td').get_text()
            atdt = atd.find('th').get_text()
            atddat = atd.find('td').get_text()
            stats = stat.find('th').get_text()
            nail = role.find('img').get('src')
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [price, price1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
			
            embed = discord.Embed()
            embed.title = "{tname}".format(tname=tname)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="abilities", pass_context=False)
    async def _abilities_artanis(self):   
        """Abilities for Artanis"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab1 = skill.find_all(class_='skill')[1]
            ab2 = skill.find_all(class_='skill')[2]
            ab3 = skill.find_all(class_='skill')[3]
			
            abimg = ab1.find(class_='skill-image').find('img').get('src')
            absk = ab1.find(class_='skill-key').get_text()
            abname = ab1.find(class_='skill-heading').find('span').get_text()	
            abcst = ab1.find(class_='skill-details').find(class_='skill-cost').get_text()	
            abcd = ab1.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            abdesc = ab1.find(class_='skill-description').get_text()
			
            ab1img = ab2.find(class_='skill-image').find('img').get('src')
            ab1sk = ab2.find(class_='skill-key').get_text()
            ab1name = ab2.find(class_='skill-heading').find('span').get_text()	
            ab1cst = ab2.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab1cd = ab2.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab1desc = ab2.find(class_='skill-description').get_text()	

            ab2img = ab3.find(class_='skill-image').find('img').get('src')
            ab2sk = ab3.find(class_='skill-key').get_text()
            ab2name = ab3.find(class_='skill-heading').find('span').get_text()	
            ab2cst = ab3.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab2cd = ab3.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab2desc = ab3.find(class_='skill-description').get_text()			

            mpA = "```" + abcst + "|" + abcd + "\n" + abdesc + "```"	
            mpB = "```" + ab1cst + "|" + ab1cd + "\n" + ab1desc + "```"	
            mpC = "```" + ab2cst + "|" + ab2cd + "\n" + ab2desc + "```"						
			
            embed1 = discord.Embed()
            embed1.title = "{absk}".format(absk=absk)
            embed1.set_image(url='{abimg}'.format(abimg=abimg))
            embed1.add_field(name="{abname}".format(abname=abname), value=mpA)
			
            embed2 = discord.Embed()
            embed2.title = "{ab1sk}".format(ab1sk=ab1sk)
            embed2.set_image(url='{ab1img}'.format(ab1img=ab1img))
            embed2.add_field(name="{ab1name}".format(ab1name=ab1name), value=mpB)
			
            embed3 = discord.Embed()
            embed3.title = "{ab2sk}".format(ab2sk=ab2sk)
            embed3.set_image(url='{ab2img}'.format(ab2img=ab2img))
            embed3.add_field(name="{ab2name}".format(ab2name=ab2name), value=mpC)

            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)		
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="trait", pass_context=False)
    async def _trait_artanis(self):   
        """Trait for Artanis"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            trait = skill.find_all(class_='skill')[0]
			
            timg = trait.find(class_='skill-image').find('img').get('src')
            tname = trait.find(class_='skill-heading').find('span').get_text()
            tcd = trait.find(class_='skill-details').find(class_='skill-cooldown').get_text()
            tdesc = trait.find(class_='skill-description').get_text()	

            mpA = "```" + tcd + "\n" + tdesc + "```"			
			
            embed = discord.Embed()
            embed.title = "Trait"
            embed.set_image(url='{timg}'.format(timg=timg))
            embed.add_field(name="{tname}".format(tname=tname), value=mpA)

            await self.bot.say(embed=embed)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="heroics", pass_context=False)
    async def _heroics_artanis(self):   
        """Heroic Abilities for Artanis"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "skills"})
            ab4 = skill.find_all(class_='skill')[4]
            ab5 = skill.find_all(class_='skill')[5]
			
            ab3img = ab4.find(class_='skill-image').find('img').get('src')
            ab3sk = ab4.find(class_='skill-key').get_text()
            ab3name = ab4.find(class_='skill-heading').find('span').get_text()
            ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()			

            mpD = "```" + ab3cst + "|" + ab3cd + "\n" + ab3desc + "```"
            mpE = "```" + ab4cst + "|" + ab4cd + "\n" + ab4desc + "```"		
			
            embed4 = discord.Embed()
            embed4.title = "{ab3sk}".format(ab3sk=ab3sk)
            embed4.set_image(url='{ab3img}'.format(ab3img=ab3img))
            embed4.add_field(name="{ab3name}".format(ab3name=ab3name), value=mpD)
			
            embed5 = discord.Embed()
            embed5.title = "{ab4sk}".format(ab4sk=ab4sk)
            embed5.set_image(url='{ab4img}'.format(ab4img=ab4img))
            embed5.add_field(name="{ab4name}".format(ab4name=ab4name), value=mpE)

            await self.bot.say(embed=embed4)	
            await self.bot.say(embed=embed5)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv1", pass_context=False)
    async def _talents1_artanis(self):   
        """Level 1 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t1 = skill.find_all(class_='talent-tier')[0]
			
            tl1 = t1.find_all(class_='matched-height talent')[0]
            tl2 = t1.find_all(class_='matched-height talent')[1]
            tl3 = t1.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/0/0a/Reactive_Parry_Icon.png?version=d4d44c034956fd36a3de750652d32e4a')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/bd/Amateur_Opponent_Icon.png?version=39546ad01bbbc527a2eb811951fd9e78')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/2/2f/Seasoned_Marksman_Icon.png?version=924f3f27956d02caa0ec86e0f1500680')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv4", pass_context=False)
    async def _talents4_artanis(self):   
        """Level 4 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t2 = skill.find_all(class_='talent-tier')[1]
			
            tl1 = t2.find_all(class_='matched-height talent')[0]
            tl2 = t2.find_all(class_='matched-height talent')[1]
            tl3 = t2.find_all(class_='matched-height talent')[2]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b9/Psionic_Synergy_Icon.png?version=2e7f4141a57d5d0b1436daff1fddd9e9')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/92/Shield_Battery_Icon.png?version=0f7ef59eba8775faeab0bb0db0c1f25f')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/ee/Shield_Surge_Icon.png?version=e8ad28b99e85d6bbbf18530330e374d9')
            embed2.add_field(name="Description", value=mpC)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)				
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv7", pass_context=False)
    async def _talents7_artanis(self):   
        """Level 7 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t3 = skill.find_all(class_='talent-tier')[2]
			
            tl1 = t3.find_all(class_='matched-height talent')[0]
            tl2 = t3.find_all(class_='matched-height talent')[1]
            tl3 = t3.find_all(class_='matched-height talent')[2]
            tl4 = t3.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/4/49/Solarite_Reaper_Icon.png?version=1f5f67ffb7a003ee5017bfcae0a8ee81')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/e/e0/Warp_Sickness_Icon.png?version=162b337b0625d132120a8f930b20a664')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b6/Chrono_Surge_Icon.png?version=ab3b88a746046f9e3328282b65e0db97')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fc/Follow_Through_Icon.png?version=83af95095a828d88cf00a7013785e931')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv13", pass_context=False)
    async def _talents13_artanis(self):   
        """Level 13 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t5 = skill.find_all(class_='talent-tier')[4]
			
            tl1 = t5.find_all(class_='matched-height talent')[0]
            tl2 = t5.find_all(class_='matched-height talent')[1]
            tl3 = t5.find_all(class_='matched-height talent')[2]
            tl4 = t5.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/7/7a/Templar%27s_Zeal_Icon.png?version=2c8c6a8f19554b9ada401b3474a747ea')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/fa/Triple_Strike_Icon.png?version=955e1f777da24c33ee07d82f2f933985')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/6/6f/Graviton_Vortex_Icon.png?version=8f16867ffb37ce463ea4c6e360e0dc54')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8a/Phase_Bulwark_Icon.png?version=9ac7b219815c7579b92f0ea77a1f6d9d')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv16", pass_context=False)
    async def _talents16_artanis(self):   
        """Level 16 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t6 = skill.find_all(class_='talent-tier')[5]
			
            tl1 = t6.find_all(class_='matched-height talent')[0]
            tl2 = t6.find_all(class_='matched-height talent')[1]
            tl3 = t6.find_all(class_='matched-height talent')[2]
            tl4 = t6.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/8c/Zealot_Charge_Icon.png?version=9ff1bf391f9fc945b7a0a08d76874ca6')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/f/f9/Titan_Killer_Icon.png?version=ee47578d4272d29471c556345a2ba216')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/b/b4/Psionic_Wound_Icon.png?version=c2098ee8546bd0e3f0dd987d972850b9')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/9/99/Burning_Rage_Icon.png?version=0236afd6e0085204220e805ccd87bb79')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
			
    @artanis.command(name="tlv20", pass_context=False)
    async def _talents20_artanis(self):   
        """Level 20 Talents"""
        url = "https://heroesofthestorm.gamepedia.com/Artanis"  
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            skill = soupObject.find('div', attrs={'class': "talent-table"})
            t7 = skill.find_all(class_='talent-tier')[6]
			
            tl1 = t7.find_all(class_='matched-height talent')[0]
            tl2 = t7.find_all(class_='matched-height talent')[1]
            tl3 = t7.find_all(class_='matched-height talent')[2]
            tl4 = t7.find_all(class_='matched-height talent')[3]
			
            tl1name = tl1.find(class_='talent-name').get_text()
            tl1desc = tl1.find(class_='talent-description').get_text()	
            mpA = "```" + tl1desc + "```"
			
            tl2name = tl2.find(class_='talent-name').get_text()
            tl2desc = tl2.find(class_='talent-description').get_text()		
            mpB = "```" + tl2desc + "```"
			
            tl3name = tl3.find(class_='talent-name').get_text()
            tl3desc = tl3.find(class_='talent-description').get_text()				
            mpC = "```" + tl3desc + "```"
			
            tl4name = tl4.find(class_='talent-name').get_text()
            tl4desc = tl4.find(class_='talent-description').get_text()				
            mpD = "```" + tl4desc + "```"
			
            embed = discord.Embed()
            embed.title = "{tl1name}".format(tl1name=tl1name)
            embed.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/15/Orbital_Bombardment_Icon.png?version=0bc6ec828da846fe1ff4de36e2c6aa1c')
            embed.add_field(name="Description", value=mpA)
			
            embed1 = discord.Embed()
            embed1.title = "{tl2name}".format(tl2name=tl2name)
            embed1.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/1/16/Target_Purified_Icon.png?version=66fc1623f9b6680be17bf51358b8f62c')
            embed1.add_field(name="Description", value=mpB)
			
            embed2 = discord.Embed()
            embed2.title = "{tl3name}".format(tl3name=tl3name)
            embed2.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/ce/Force_of_Will_Icon.png?version=8f8a0a5bf67f6f64c0b4cfb5fb8cbebe')
            embed2.add_field(name="Description", value=mpC)
			
            embed3 = discord.Embed()
            embed3.title = "{tl4name}".format(tl4name=tl4name)
            embed3.set_thumbnail(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/8/83/Nexus_Blades_Icon.png?version=0d354b01c55bc7f5232301a6d7a0ee01')
            embed3.add_field(name="Description", value=mpD)

            await self.bot.say(embed=embed)	
            await self.bot.say(embed=embed1)
            await self.bot.say(embed=embed2)	
            await self.bot.say(embed=embed3)			
        except discord.errors.HTTPException:
            await self.bot.say("Character Limit reached, unable to post frame data....")
        except IndexError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")
        except KeyError:
            await self.bot.say("Unexpected Error occurred retrieving frame data, please report issue here: https://github.com/Mojotroll/Mojo-Cogs/issues")	
################################################################################################################################################################################################################################################
def setup(bot):
    if soupAvailable is False:
        raise RuntimeError("You don't have BeautifulSoup installed, run\n```pip3 install bs4```And try again")
        return
    if tabulateAvailable is False:
        raise RuntimeError("You don't have tabulate installed, run\n```pip3 install tabulate```And try again")
        return
    bot.add_cog(hots(bot))