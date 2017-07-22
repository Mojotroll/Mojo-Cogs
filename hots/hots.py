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
            type = table.find_all('tr')[6]
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

            alarak = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            type1 = type.find('th').get_text()
            type2 = type.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [type1, type2], [date, date1]], tablefmt='grid', stralign='left')
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
            type = table.find_all('tr')[6]
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

            cassia = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            type1 = type.find('th').get_text()
            type2 = type.find('td').get_text()
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
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [type1, type2], [date, date1]], tablefmt='grid', stralign='left')
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
            type = table.find_all('tr')[6]
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
            spl = table.find_all('tr')[17]
            mhpl = table.find_all('tr')[18]
            hgpl = table.find_all('tr')[19]
            rgpl = table.find_all('tr')[20]

            chromie = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            type1 = type.find('th').get_text()
            type2 = type.find('td').get_text()
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
            splt = spl.find('th').get_text()
            spl1 = mhpl.find('th').get_text()
            spl2 = mhpl.find('td').get_text()
            spl3 = hgpl.find('th').get_text()
            spl4 = hgpl.find('td').get_text()
            spl5 = rgpl.find('th').get_text()
            spl6 = rgpl.find('td').get_text()
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [type1, type2], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            tab2 = tabulate([[spl1, spl2], [spl3, spl4], [spl5, spl6]], tablefmt='fancygrid', stralign='left')
            mpA = "We have all the time in the world!"
			
            embed = discord.Embed()
            embed.title = "{chromie}".format(chromie=chromie)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.add_field(name="{splt}".format(splt=splt), value=tab2, inline='true')
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
            type = table.find_all('tr')[6]
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
            spl = table.find_all('tr')[17]
            mhpl = table.find_all('tr')[18]
            hgpl = table.find_all('tr')[19]
            rgpl = table.find_all('tr')[20]

            falstad  = name.find('th').get_text()	
            picture = pic.find('img').get('src')		
            info = binfo.find('th').get_text()			
            ttl = title.find('th').get_text()
            ttl1 = title.find('td').get_text()
            role1 = role.find('th').get_text()
            role2 = role.find('td').get_text()
            franc = fran.find('th').get_text()
            franc1 = fran.find('td').get_text()
            type1 = type.find('th').get_text()
            type2 = type.find('td').get_text()
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
            splt = spl.find('th').get_text()
            spl1 = mhpl.find('th').get_text()
            spl2 = mhpl.find('td').get_text()
            spl3 = hgpl.find('th').get_text()
            spl4 = hgpl.find('td').get_text()
            spl5 = rgpl.find('th').get_text()
            spl6 = rgpl.find('td').get_text()
			
            tab = tabulate([[ttl, ttl1], [role1, role2], [franc, franc1], [type1, type2], [date, date1]], tablefmt='grid', stralign='left')
            tab1 = tabulate([[htit, hdat], [hregt, hregdat], [ent, endat], [armt, armdat], [spt, spdat], [atst, atsdat], [atrt, atrdat], [atdt, atddat]], tablefmt='grid', stralign='left')
            tab2 = tabulate([[spl1, spl2], [spl3, spl4], [spl5, spl6]], tablefmt='fancygrid', stralign='left')
            mpA = "For Khaz Modan!"
			
            embed = discord.Embed()
            embed.title = "{falstad}".format(falstad=falstad)
            embed.set_image(url='{picture}'.format(picture=picture))
            embed.set_thumbnail(url="{nail}".format(nail=nail))
            embed.add_field(name="{info}".format(info=info), value=tab, inline='true')
            embed.add_field(name="{stats}".format(stats=stats), value=tab1, inline='true')
            embed.add_field(name="{splt}".format(splt=splt), value=tab2, inline='true')
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
def setup(bot):
    if soupAvailable is False:
        raise RuntimeError("You don't have BeautifulSoup installed, run\n```pip3 install bs4```And try again")
        return
    if tabulateAvailable is False:
        raise RuntimeError("You don't have tabulate installed, run\n```pip3 install tabulate```And try again")
        return
    bot.add_cog(hots(bot))