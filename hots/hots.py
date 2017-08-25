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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            alarak = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "You address the highlord?"
			
            embed = discord.Embed()
            embed.title = "{alarak}".format(alarak=alarak)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            cassia = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "I am the Queen's spear!"
			
            embed = discord.Embed()
            embed.title = "{cassia}".format(cassia=cassia)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            chromie = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "We have all the time in the world!"
			
            embed = discord.Embed()
            embed.title = "{chromie}".format(chromie=chromie)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            #ab3cst = ab4.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab3cd = ab4.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab3desc = ab4.find(class_='skill-description').get_text()	

            ab4img = ab5.find(class_='skill-image').find('img').get('src')
            ab4sk = ab5.find(class_='skill-key').get_text()
            ab4name = ab5.find(class_='skill-heading').find('span').get_text()
            ab4cst = ab5.find(class_='skill-details').find(class_='skill-cost').get_text()	
            ab4cd = ab5.find(class_='skill-details').find(class_='skill-cooldown').get_text()	
            ab4desc = ab5.find(class_='skill-description').get_text()					

            mpD = "```" + ab3cd + "\n" + ab3desc + "```"
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
            print(ab4img)			
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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            falstad  = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "For Khaz Modan!"
			
            embed = discord.Embed()
            embed.title = "{falstad}".format(falstad=falstad)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            gall  = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "Embrace the shadow!"
			
            embed = discord.Embed()
            embed.title = "{gall}".format(gall=gall)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            genji = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "You... are a fish."
			
            embed = discord.Embed()
            embed.title = "{genji}".format(genji=genji)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            table = soupObject.find_all('table', attrs={'class': "infobox2"})[0]
            name = table.find_all('tr')[0]
            pic = table.find_all('tr')[1]
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            reld = table.find_all('tr')[6]
			
            table1 = soupObject.find_all('table', attrs={'class': "infobox2"})[1]
            gmh = table1.find_all('tr')[0]
            bstats = table1.find_all('tr')[1]
            at = table1.find_all('tr')[2]
            hlt1 = table1.find_all('tr')[3]
            hltreg1 = table1.find_all('tr')[4]
            res1 = table1.find_all('tr')[5]
            arm1 = table1.find_all('tr')[6]
            ats1 = table1.find_all('tr')[7]
            atr1 = table1.find_all('tr')[8]
            atd1 = table1.find_all('tr')[9]
			
            table2 = soupObject.find_all('table', attrs={'class': "infobox2"})[2]
            gmw = table2.find_all('tr')[0]
            bstats2 = table2.find_all('tr')[1]
            at1 = table2.find_all('tr')[2]
            hlt2 = table2.find_all('tr')[3]
            hltreg2 = table2.find_all('tr')[4]
            res2 = table2.find_all('tr')[5]
            arm2 = table2.find_all('tr')[6]
            ats2 = table2.find_all('tr')[7]
            atr2 = table2.find_all('tr')[8]
            atd2 = table2.find_all('tr')[9]

            greymane = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            date = reld.find('th').get_text()
            date1 = reld.find('td').get_text()
            nail = role.find('img').get('src')
			
            gmht = gmh.find('th').get_text()
            bstats1 = bstats.find('th').get_text()
            atA = at.find('th').get_text()
            atB = at.find('td').get_text()
            hltA = hlt1.find('th').get_text()
            hltB = hlt1.find('td').get_text()
            hltrA = hltreg1.find('th').get_text()
            hltrB = hltreg1.find('td').get_text()
            resA = res1.find('th').get_text()
            resB = res1.find('td').get_text()
            armA = arm1.find('th').get_text()
            armB = arm1.find('td').get_text()
            atsA = ats1.find('th').get_text()
            atsB = ats1.find('td').get_text()
            atrA = atr1.find('th').get_text()
            atrB = atr1.find('td').get_text()
            atdA = atd1.find('th').get_text()
            atdB = atd1.find('td').get_text()
			
            gmwt = gmw.find('th').get_text()
            bstats3 = bstats2.find('th').get_text()
            atC = at1.find('th').get_text()
            atD = at1.find('td').get_text()
            hltC = hlt2.find('th').get_text()
            hltD = hlt2.find('td').get_text()
            hltrC = hltreg2.find('th').get_text()
            hltrD = hltreg2.find('td').get_text()
            resC = res2.find('th').get_text()
            resD = res2.find('td').get_text()
            armC = arm2.find('th').get_text()
            armD = arm2.find('td').get_text()
            atsC = ats2.find('th').get_text()
            atsD = ats2.find('td').get_text()
            atrC = atr2.find('th').get_text()
            atrD = atr2.find('td').get_text()
            atdC = atd2.find('th').get_text()
            atdD = atd2.find('td').get_text()
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[atA, atB], [hltA, hltB], [hltrA, hltrB], [resA, resB], [armA, armB], [atsA, atsB], [atrA, atrB], [atdA, atdB]], tablefmt='grid', stralign='left')
            tab2 = tabulate([[atC, atD], [hltC, hltD], [hltrC, hltrD], [resC, resD], [armC, armD], [atsC, atsD], [atrC, atrD], [atdC, atdD]], tablefmt='grid', stralign='left')
            mpA = "Gilneas never back down!"
			
            embed = discord.Embed()
            embed.title = "{greymane}".format(greymane=greymane)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{gmht}".format(gmht=gmht), value=tab1, inline='true')
            embed.add_field(name="{gmwt}".format(gmwt=gmwt), value=tab2, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            guldan = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "I will not be denied!"
			
            embed = discord.Embed()
            embed.title = "{guldan}".format(guldan=guldan)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            illidan = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "I will not be denied!"
			
            embed = discord.Embed()
            embed.title = "{illidan}".format(illidan=illidan)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            binfo = table.find_all('tr')[2]
            title = table.find_all('tr')[3]
            role = table.find_all('tr')[4]
            fran = table.find_all('tr')[5]
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            jaina = name.find('th').get_text()		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "I'm here to help!"
			
            embed = discord.Embed()
            embed.title = "{jaina}".format(jaina=jaina)
            embed.set_image(url='https://heroesofthestorm.gamepedia.com/media/heroesofthestorm.gamepedia.com/c/c1/JainaArt.jpg?version=33bae818a937c31d0a3023ee310151d3')
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            kaelthas = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "I don't suffer setbacks. I revel in them."
			
            embed = discord.Embed()
            embed.title = "{kaelthas}".format(kaelthas=kaelthas)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
            reld = table.find_all('tr')[6]
            stat = table.find_all('tr')[7]
            hlt = table.find_all('tr')[8]
            hreg = table.find_all('tr')[9]
            eng = table.find_all('tr')[10]
            arm = table.find_all('tr')[11]
            spd = table.find_all('tr')[12]
            ats = table.find_all('tr')[13]
            atr = table.find_all('tr')[14]
            atd = table.find_all('tr')[15]

            kerrigan = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            mpA = "Your time's up."
			
            embed = discord.Embed()
            embed.title = "{kerrigan}".format(kerrigan=kerrigan)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.set_footer(text=mpA)

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
def setup(bot):
    if soupAvailable is False:
        raise RuntimeError("You don't have BeautifulSoup installed, run\n```pip3 install bs4```And try again")
        return
    if tabulateAvailable is False:
        raise RuntimeError("You don't have tabulate installed, run\n```pip3 install tabulate```And try again")
        return
    bot.add_cog(hots(bot))