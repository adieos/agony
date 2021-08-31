import discord
import contextlib
import io
from discord import channel
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingRequiredArgument, NotOwner

class Moderating(commands.Cog):

    def __init__(self, client):
        self.client = client

    is_automod_on = False

    @commands.Cog.listener() # NOTE: automod
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id != 810700979154452482:
            return

        if not is_automod_on:
            return

        for i in message.content.split():
            if i == "test":
                await message.delete()
                await message.channel.send("no swer !!11!!1")
                return

    @commands.command() # NOTE: automod trigger
    async def automod(self, ctx, foo = "0"):
        global is_automod_on
        is_automod_on = False
        if foo == "0":
            await ctx.send("Automod disabled")
            return
        elif foo == "1":
            is_automod_on = True
            await ctx.send("Automod enabled")
        elif foo == "status":
            await ctx.send(is_automod_on)
        else:
            await ctx.send("Automod disabled")

    # @commands.command()
    # async def test(self, ctx):
    #     await ctx.send(type(has_permissions))
    #     await ctx.send(has_permissions)

    # @commands.command()
    # @commands.has_role("Tester")
    # async def tester(self, ctx):
    #     await ctx.send("Yay you have the appropriate role!")
    # @tester.error
    # async def testererror(self, ctx, error):
    #     if isinstance(error, commands.MissingRole):
    #         await ctx.send("You don't have the appropriate role, L.")

    # @commands.command()
    # async def checkperms(self, ctx):
    #     await ctx.send(ctx.author.guild_permissions)

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
    async def send(self, ctx, ch=0, *, msg=None): # look I cba to make the exceptions ok
        if ctx.author.id != 515777528657608705:
            await ctx.send("You can't do that!")
            return
        
        channel = self.client.get_channel(ch)
        await channel.send(msg)
        await ctx.message.delete()
    @send.error
    async def senderror(self, ctx, error):
        await ctx.send(error)
    
    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        cmd = self.client.get_command(command)

        if cmd is None:
            await ctx.send("I can't find such command!")
            return
        elif cmd == ctx.command:
            await ctx.send("You can't disable this command!")
            return

        cmd.enabled = not cmd.enabled # toggling the command
        ternary = "enabled" if cmd.enabled else "disabled"
        await ctx.send(f"{ternary} {cmd.qualified_name}")
    @toggle.error
    async def toggleerror(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("I need the command name to enable/disable!")
            return
        elif isinstance(error, NotOwner):
            await ctx.send("You can't run this command!")
            return
        await ctx.send(f"`{type(error).__name__}: {error}`")

    @commands.command(aliases=["e", "eval"])
    @commands.is_owner()
    async def evaluate(self, ctx, *, code):
        str_obj = io.StringIO() #Retrieves a stream of data
        if code[0] == "`":
            code = code[9:-4]
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            await ctx.send("oh no")
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        if str_obj.getvalue() == "":
            await ctx.send("No output")
            return
        await ctx.send(f'```{str_obj.getvalue()}```')
    @evaluate.error
    async def asssss(self, ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Hey, you can't run this command!")
            return
        await ctx.send(error)

def setup(client):
    client.add_cog(Moderating(client))