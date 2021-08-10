import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
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
    channel = bot.get_channel(873407182564098048) 
    await channel.send("🙏 :pray:")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")

@bot.command()
async def invite(ctx):
    ebd = discord.Embed(
        title = "Invite Bot",
        description = "You think this bot is actually useful\nand not a completely "\
            "futile artificial intelligence, huh?\nGo ahead, add this junk to your server."
    )
    ebd.set_thumbnail(
        url = "https://cdn.discordapp.com/attachments/873407182564098048/874500884351037500/amogus.jpg"
    )
    ebd.add_field(
        name = "Click This!",
        value = "[Add AmoguBot to your server](https://discord.com/api/oauth2/authorize?client_id=868475589017870376&permissions=287808&scope=bot)"
    )
    await ctx.send(embed=ebd)
# Misc
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

# Load and unload extensions hhhh
@bot.command()
async def load(ctx, *ext):
    if ctx.author.id != 515777528657608705:
        await ctx.send("You are not allowed to do that!")
        return
    if len(ext) == 0:
        await ctx.send("No extension loaded!")
    else:
        for i in ext:
            try:
                bot.load_extension(f"cogs.{i}")
                await ctx.send(f"Extension `{i}` has been loaded.")
            except ExtensionNotFound:
                await ctx.send(f"Extension `{i}` not found!")
            except ExtensionAlreadyLoaded:
                await ctx.send(f"Extension `{i}` is already loaded!")

@bot.command()
async def unload(ctx, *ext):
    if ctx.author.id != 515777528657608705:
        await ctx.send("You are not allowed to do that!")
        return
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
    if ctx.author.id != 515777528657608705:
        await ctx.send("You are not allowed to do that!")
        return
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