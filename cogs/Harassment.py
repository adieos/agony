import discord 
from discord.ext import commands

class Harassment(commands.Cog):

    def __init__(self, client):
        self.client = client

    trollid = None

    @commands.Cog.listener()
    async def on_message(self, ctx):
        return
        if trollid is None:
            return
        elif ctx.author.id == trollid:
            await ctx.delete()
            await ctx.channel.send("https://cdn.discordapp.com/emojis/851662635379327006.gif?v=1")

    @commands.command()
    async def tyohio(self, ctx):
        channel = self.client.get_channel(877703041145507871)
        await channel.send("thank you Ohhio")
    @commands.command()
    async def troll(self, ctx, user: discord.Member = None):
        global trollid
        if user is None:
            await ctx.send("ok enough troling today :)")
            trollid = None
            return
        trollid = user.id
        await ctx.send(f"`trollid` has been set to {trollid}")

    @commands.command()
    async def whostroll(self, ctx):
        try:
            if trollid is None:
                await ctx.send("Noone to troll!")
                return
            await ctx.send(trollid+" is being trolled !")
        except NameError:
            await ctx.send("Run `sus troll` command first!")

    @commands.command()
    async def dm(self, ctx, user: discord.User = None, *, msg):
        if user is None:
            await ctx.send("Noone to DM!")
            return
        
        user = await self.client.fetch_user(user.id)
        await user.send(msg)
        
    @commands.command(aliases=["id"])
    async def grabid(self, ctx, user: discord.User = None):
        if user is None:
            ebd = discord.Embed(
                title = "Grabid",
                description = "Displays the ID of the specified person."
            )
            ebd.add_field(
                name = "Usage",
                value = "`sus grabid <user>`",
                inline = False
            )
            ebd.add_field(
                name = " Aliases",
                value = "`id`"
            )
            await ctx.send(embed=ebd)
            return
        await ctx.send(f"{user}'s user ID is {user.id}")

    # This thing is stil flawed hhh (but still works!)
    @commands.command(aliases=["spamping"])
    async def sp(self, ctx, user: discord.User = None, amt=None):
        if user is None:
            await ctx.send("No user detected!")
        elif amt is None:
            await ctx.send("Ping amount required!")
        else:
            try:
                amt = int(amt)
                if amt >= 10:
                    await ctx.send("Too many pings, evildoer!")
                    return
                elif amt < 0:
                    await ctx.send("Hey dumbo, you cant ping someone negative number times")
                    return
                elif amt == 0:
                    await ctx.send("Yea ok not pinging anyone got it")
                    return
                for i in range(amt):
                    await ctx.send(user.mention)
            except ValueError:
                await ctx.send("Input a valid number!")
            except:
                await ctx.send("Invalid user!")
        
    @commands.command(aliases=["gmc"])
    async def givemecolor(self, ctx, *color):
        if len(color) == 0:
            await ctx.send("Yea ok not giving you any role")
            return
        for i in color:
            i = i.upper()
            i = i.capitalize()
            if i not in["Blue", "Yellow", "Red", "Green"]:
                await ctx.send(f"Color {i} does not exist!")
            else:
                crole = discord.utils.get(ctx.guild.roles, name=i)
                await ctx.author.add_roles(crole)
                await ctx.send(f"Assigned color {i}.")
                    # Troll message soontm
        
    @commands.command(aliases=["tmc"])
    async def takemycolor(self, ctx, *color):
        if len(color) == 0:
            ebd = discord.Embed(
                title = "Takemycolor",
                description = "Takes away color role(s) from command author."
            )
            ebd.add_field(
                name = "Usage",
                value = "`sus takemycolor <colors>`",
                inline = False
            )
            ebd.add_field(
                name = "Aliases",
                value = "`tmc`",
                inline = False
            )
            ebd.set_footer(
                text = "Made by adios#1444",
                icon_url = "https://cdn.discordapp.com/attachments/733197081681985653/872832326239911986/hhh.gif"
            )
            await ctx.send(embed=ebd)
            return
        for i in color:
            i = i.upper()
            i = i.capitalize()
            if i not in["Blue", "Yellow", "Red", "Green"]:
                await ctx.send(f"Color {i} does not exist!")
            else:
                crole = discord.utils.get(ctx.guild.roles, name=i)
                if crole not in ctx.author.roles:
                    await ctx.send(f"You don't have color {i}")
                else:
                    await ctx.author.remove_roles(crole)
                    await ctx.send(f"Removed color {i}.")

def setup(client):
    client.add_cog(Harassment(client))