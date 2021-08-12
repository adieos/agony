import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderating(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send(type(has_permissions))
        await ctx.send(has_permissions)

    @commands.command()
    @commands.has_role("Tester")
    async def tester(self, ctx):
        await ctx.send("Yay you have the appropriate role!")
    @tester.error
    async def testererror(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have the appropriate role, L.")

    @commands.command()
    async def checkperms(self, ctx):
        await ctx.send(ctx.author.guild_permissions)

    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amt=None):
        try:
            if amt == None:
                await ctx.send("Oi evildoer, I need a number")
                return
            amt = int(amt) + 1
            await ctx.channel.purge(limit=amt)
        except:
            await ctx.send("Something hsa gone wrong hhh")
    @clear.error
    async def purgeerror(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")
        else:
            await ctx.send("ynwjdn")

    @commands.command()
    async def jinping(self, ctx):
        chanle = self.client.get_channel(873407182564098048)
        face = await chanle.fetch_message(875224307385643008)
        await ctx.send(face.content)

    @commands.command()
    async def ihateamogubot(self, ctx):
        await ctx.send("test")
        chanle = self.client.get_channel(874999244073865268)
        await ctx.send("bal")
        try:
            await ctx.send("piss")
            msg = await chanle.fetch_message(875012839214043166)
            await ctx.send("p")
            await ctx.send(msg.content)
        except Exception as ex:
            await ctx.send(f"Error occured hhh ({type(ex).__name__}")

def setup(client):
    client.add_cog(Moderating(client))