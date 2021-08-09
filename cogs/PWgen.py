import discord
from discord.ext import commands

class PWgen(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["caesar","Caesar"])
    async def cc(self, ctx, key=None, text=None):
        password = ""
        try:
            key = int(key)
            for i in text:
                pos = ord(i)
                pos += key
                while True:
                    if pos >= 123:
                        pos -= 26
                    elif pos <= 96:
                        pos += 26
                    else:
                        break
                password += chr(pos)
            await ctx.send(f"Your new password is `{password}`")
        except TypeError:
            if text == None:
                await ctx.send("Nothing to encrypt!")
            else:
                await ctx.send("Unknown error occured.")
        except ValueError:
            await ctx.send("Invalid number!")

# Flaws:
# 1. Unable to encrypt non-alphabetical characters
# 2. Output is always lowercase, despite input is uppercase

def setup(client):
    client.add_cog(PWgen(client))