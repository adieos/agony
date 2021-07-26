from typing import Type
import discord
from discord.ext import commands
from suspisus import atoken
from discord.utils import find

bot = commands.Bot(command_prefix="sus ")

@bot.event
async def on_ready():
    print(bot.user.name+" is online.")

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("amogus")
# Fully from StackOverFlow hahahahahah

@bot.command()
async def picious(ctx):
    await ctx.send("amogus")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")

@bot.command()
async def ohhiorun(ctx, box=None):
    try:
        if box is None:
            box = 1
        else:
            box = int(box)
        if box <= 0:
            await ctx.send("No ohhiorun :(")
        elif box >= 6:
            await ctx.send("Too many ohhioruns!")
        else:
            await ctx.send(("<a:ohhiorun:868114328254050344>"*box+"\n")*box)
    except ValueError:
        await ctx.send("Invalid number!")

@bot.command()
async def add(ctx, *num):
    try:
        sum = 0
        ctx.send(type(sum))
        for i in num:
            i = int(i)
            sum += i
        await ctx.send(sum)
    except ValueError or TypeError:
        await ctx.send("Invalid number detected!")

@bot.command(aliases=["purge"])
async def clear(ctx, amt=None):
    a = 1
    while a == 1:
        try:
            if amt == None:
                await ctx.send("Oi evildoer, I need a number")
                break
            amt = int(amt) + 1
            await ctx.channel.purge(limit=amt)
            await ctx.send(f"{amt-1} messages got deleted by {ctx.author.mention}")
        except:
            await ctx.send("Something hsa gone wrong hhh")
        finally:
            break

@bot.command()
async def cc(ctx, key=None, text=None):
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

@bot.command()
async def embed(ctx):
    embedharharhar = discord.Embed(
        title="Embed demo",
        url="https://www.youtube.com/watch?v=1rjCuPQI298",
        description="Click this to go to Mehdi Sadhaghar's video"
    )
    embedharharhar.set_author(
        name="Amogus",
        url="https://www.youtube.com/watch?v=5DlROhT8NgU",
        icon_url="https://imgur.com/a/QixbJ4h"
    )
    await ctx.send(embed=embedharharhar)

bot.run(atoken)