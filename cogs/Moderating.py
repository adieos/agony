import discord
import contextlib
import io
import json
from datetime import datetime
from discord.errors import HTTPException
from discord.ext import commands
import asyncio

from discord.ext.commands.errors import MissingRequiredArgument, NotOwner

class Moderating(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.client.get_channel(889486525874720768)
        msg = message.content[:1024] # shortens the message
        amt = "Massive Message Deleted" if len(message.content) > 1024 else "Message Deleted" # just fancy fancy shit o man
        color = 0xfca103 if len(message.content) < 1025 else 0xdb1009
        ebd = discord.Embed(title=amt, color=color)
        ebd.add_field(name="Author", value=message.author)
        ebd.add_field(name="Location", value=message.channel)
        ebd.add_field(name="Message", value=msg, inline=False)
        ebd.timestamp=datetime.utcnow()
        try:
            await channel.send(embed=ebd)
        except HTTPException:
             await channel.send(f"An embed just got deleted at {datetime.utcnow()}")
        except Exception as e:
            await channel.send(f"`{type(e).__name__}: {e}`")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author==self.client.user:
            return

        with open('socialcredit.json', 'r') as scj:
            data = json.load(scj)
            words = msg.content.split()
            longfunnywarn = '''
            500 social credits have been deducted from your account. 500 社會信用已從您的帳戶中扣除。Reason: saying the T#iwan word. 原因：說出T#iwan這個詞。DO NOT DO THIS AGAIN! 不要再這樣做了！Should you keep doing this again, you will be sent to re-education camp. 如果你繼續這樣做，你將被送到再教育營。
            '''
            for i in words:            
                if i.lower() == "taiwan":
                    for j in data['members']:
                        if j['id'] == msg.author.id:
                            j['credit'] -= 500
                            await msg.channel.send(longfunnywarn)
                            break
                    break

        with open('socialcredit.json', 'w') as scj:
            json.dump(data, scj, indent = 2)

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
    @commands.is_owner()
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
        if isinstance(error, commands.NotOwner):
            await ctx.send("You cant do that!")

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

    @commands.command()
    async def presence(self, ctx, type, *, arg):
        if type == "game":
            act = discord.Game(name=arg)
        elif type == "stream":
            act = discord.Streaming(name=arg) # NEED URL
        elif type == "listen":
            act = discord.Activity(type=discord.ActivityType.listening, name=arg)
        elif type == "watch":
            act = discord.Activity(type=discord.ActivityType.watching, name=arg)
        await self.client.change_presence(activity=act)

# MUTE COMMAND
    @commands.command()
    @commands.is_owner()
    async def shutup(self, ctx, user:discord.Member, dura="1m"):
        # checking if the muted role exist or not (named "please shut up thanks")
        if discord.utils.get(ctx.guild.roles, name="please shut up thanks"):
            pass
        else:
            await ctx.guild.create_role(name="please shut up thanks", permissions=discord.Permissions(permissions=0), color=0x808080)
            role = discord.utils.get(ctx.guild.roles, name="please shut up thanks")
            for channel in ctx.guild.text_channels:
                perms = channel.overwrites_for(role)
                perms.send_messages=False
                await channel.set_permissions(role, overwrite=perms, reason="em my beloved <3")
        
        # convert the duration to seconds
        dura = dura.lower()
        conversion = {"s":1, "m":60, "h":3600,"d":86400}
        try:
            duration = int(dura)
        except ValueError:
            duration = int(dura[:-1]) * conversion[dura[-1]]

        # creating simple embed
        ebd = discord.Embed(
            title = f":white_check_mark: | {user} will no longer speak for the next {duration} seconds :grin:",
            color = 0xdaa717
        )

        # muting the user
        mutedrole = discord.utils.get(ctx.guild.roles, name="please shut up thanks")    
        await user.add_roles(mutedrole)
        await ctx.send(embed=ebd)
        await asyncio.sleep(duration)
        await user.remove_roles(mutedrole)
    @shutup.error
    async def shutuperror(self, ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("haha, no dont do that")
        else:
            await ctx.send(error)

def setup(client):
    client.add_cog(Moderating(client))