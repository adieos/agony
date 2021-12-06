import discord
from discord.errors import Forbidden, HTTPException
from discord.ext import commands
from time import sleep
import random
import json

from discord.ext.commands.errors import DisabledCommand, MissingRequiredArgument

class Harassment(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dm(self, ctx, user: discord.User = None, *, msg=None):
        try:
            if user is None:
                await ctx.send("Noone to DM!")
                return
            elif msg is None:
                await ctx.send("Can't send empty message!")
                return
        except discord.HTTPException:
            await ctx.send("Unable to DM this user.")
        
        await user.send(msg)
        await ctx.send("DM Success.")
    @dm.error
    async def dmerror(self, ctx, error):
        if isinstance(error, commands.UserNotFound):
            await ctx.send("Please input a valid user!")
            return
        elif isinstance(error, Forbidden) or isinstance(error, HTTPException):
            await ctx.send("Unable to send a direct message to this user.")
            return
        
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
    @commands.command(aliases=["sp"])
    @commands.cooldown(2, 30)
    async def spamping(self, ctx, user: discord.User = None, amt=None, *, msg=None):
        if user is None:
            await ctx.send("No user detected!")
        elif amt is None:
            await ctx.send("Ping amount required!")
        else:
            try:
                amt = int(amt)
                if amt >= 21:
                    await ctx.send("Too many pings, evildoer!")
                    return
                elif amt < 0:
                    await ctx.send("Hey dumbo, you cant ping someone negative number times")
                    return
                elif amt == 0:
                    await ctx.send("Yea ok not pinging anyone got it")
                    return
                for i in range(amt):
                    if msg is None:
                        await ctx.send(user.mention)
                        sleep(0.25)
                    else:
                        await ctx.send(f"{user.mention} {msg}")
                        sleep(0.25)
            except ValueError:
                await ctx.send("Input a valid number!")
            except:
                await ctx.send("Invalid user!")
    @spamping.error
    async def sperror(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, you are on cooldown!")
            return

    @commands.command(aliases=["social", "sc"])
    async def socialcredit(self, ctx, user: discord.User, amt: int):
        with open('socialcredit.json', 'r') as sc:
            data = json.load(sc)
            # IF statement below is only used to generate final message
            if amt < 0 : #negative social credit boo
                amtabs = -1 * amt # amtabs = amt Absolute
                amts = str(amtabs) # amts = amount String
                msglist = ["Keep this up and you will be sent to re-education camp!", "Supreme Leader is disappointed with you.",
                "Do better next time.", "Should you lose more social credits, you will be sent to re-education camp."]
                msg = random.choice(msglist)
                finalmsg = amts + " social credits have been deducted from your account. " + msg

            elif amt > 0: #positive social credit yay
                amts = str(amt)
                msglist = ["Enjoy!", "Glory to CCP!", "Have fun!", "Xi Jinping is satisfied with you."]
                msg = random.choice(msglist)
                finalmsg = amts + " social credits have been added to your account. " + msg

            else:
                return

            # JSON data manipulating
            for i in data['members']:
                if i['id']==user.id:
                    i['credit']+=amt

        with open('socialcredit.json', 'w') as newsc:
            json.dump(data, newsc, indent = 2)

        await user.send(finalmsg)
        await ctx.send(f"Social credit manipulation on {user} success.")
    @socialcredit.error
    async def socialcrediterror(self, ctx, error):
        await ctx.send(error)

    @commands.command()
    async def displaycredit(self, ctx, user:discord.User=None):
        if user is None:
            user = ctx.author

        with open('socialcredit.json', 'r') as scj:
            data = json.load(scj)
            for i in data['members']:
                if i['id']==user.id:
                    await ctx.send(f"User {user} has {i['credit']} Social Credits in their account.")
    @displaycredit.error
    async def displaycrediterror(self, ctx, error):
        await ctx.send(error)

    @commands.command()
    async def nukecredit(self, ctx, user:discord.User):
        with open('socialcredit.json','r') as scj:
            data = json.load(scj)

            for i in data['members']:
                if i['id'] == user.id:
                    i['credit'] = 0
                    
        with open('socialcredit.json', 'w') as scj:
            json.dump(data, scj, indent = 2)
        
        await ctx.send(f":exploding_head: | Success! Reduced {user}'s Social Credits to ashes. They now have 0 Social Credits remaining.")

    @nukecredit.error
    async def nukecrediterror(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("kock")

        

def setup(client):
    client.add_cog(Harassment(client))