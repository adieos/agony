import discord
from discord.errors import Forbidden, HTTPException
from discord.ext import commands
from time import sleep

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
        else: # Hopefully this doesnt run
            await ctx.send(f"An unknown error has occured. (`{error}`)")
            await ctx.send("<@515777528657608705> BOR an unknown error !") 
        
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
            await ctx.send("Command is on cooldown!")
        else:
            await ctx.send(f"Unknown error occured.")

        

def setup(client):
    client.add_cog(Harassment(client))