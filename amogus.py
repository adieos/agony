import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionNotFound, ExtensionNotLoaded, UserNotFound
from personal.suspisus import atoken
from discord.utils import find
import os

bot = commands.Bot(command_prefix="sus ",description="Amogus")

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
async def grabid(ctx, user: discord.User):
    await ctx.send(user.id)

@bot.command()
async def sp(ctx, user: discord.User = None, amt=None):
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
            for i in range(amt):
                await ctx.send(f"<@{user.id}>")
        except ValueError:
            await ctx.send("Input a valid number!")
        except:
            await ctx.send("User not found!")


@bot.command()
async def embed(ctx):
    ebd = discord.Embed(
        title="Circuit, Series, and Parallel",
        url="https://www.youtube.com/watch?v=AMXWm_bnsTE",
        description="ElectroBOOM101 - Eps. 005",
        color = 0x9c5513
    )
    ebd.set_author(
        name=ctx.author.display_name,
        url="https://www.youtube.com/watch?v=5DlROhT8NgU",
        icon_url=ctx.author.avatar_url
    )
    ebd.set_thumbnail(url="https://cdn.discordapp.com/attachments/746991157766127678/869185583430389810/mehdi.jpg")
    ebd.add_field(
        name="Circuit",
        value="Mehdi Sadaghdar explains what a circuit is",
        inline=False
    )
    ebd.add_field(
        name="Series",
        value="Mehdi explains how a series circuit behaves",
        inline=True
    )
    ebd.add_field(
        name="Parallel",
        value="Mehdi explains how a parallel circuit behaves",
        inline=True
    )
    ebd.set_footer(text="This embed is not affiliated with ElectroBOOM whatsoever hhh")
    await ctx.send(embed=ebd)

# Load and unload extensions hhhh
@bot.command()
async def load(ctx, *ext):
    if len(ext) == 0:
        await ctx.send("No extension loaded!")
    else:
        for i in ext:
            try:
                bot.load_extension(f"cogs.{i}")
                await ctx.send(f"Extension `{i}` has been loaded.")
            except ExtensionNotFound:
                await ctx.send(f"Extension `{i}` not found!")

@bot.command()
async def unload(ctx, *ext):
    if len(ext) == 0:
        await ctx.send("No extension unloaded!")
    else:
        for i in ext:
            try:
                bot.unload_extension(f"cogs.{i}")
                await ctx.send(f"Extension `{i}` has been unloaded.")
            except ExtensionNotLoaded:
                await ctx.send(f"Extension `{i}` not found!")

@bot.command()
async def reload(ctx, *ext):
    if len(ext) == 0:
        await ctx.send("No extension reloaded!")
    else:
        for i in ext:
            try:
                bot.unload_extension(f"cogs.{i}")
                bot.load_extension(f"cogs.{i}")
                await ctx.send(f"Extension {i} has been reloaded.")
            except ExtensionNotLoaded:
                await ctx.send(f"Extension `{i}` not found!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
         bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(atoken)