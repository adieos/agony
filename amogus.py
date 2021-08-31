import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
from hhhh import atoken 
from discord.utils import find
import os

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="sus ",description="Amogus", intents=intents)

@bot.event
async def on_ready():
    print(bot.user.name+" is online.")

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("amogus")
# Fully from StackOverFlow hahahahahah

# @bot.event
# async def on_reaction_add(reaction, user):
#    channel = reaction.message.channel
#    await channel.send(f"{user.name} has added reaction {reaction.emoji} to the message: {reaction.message.content}")

# This thing sorta works, but it cant watch messages that was sent before the bot started
# so yeah help me
#@bot.event
# async def on_reaction_add(reaction, user):
 #   channel = bot.get_channel(874949148896530432) # test ground 2
  #  schannel = bot.get_channel(873407182564098048) # test gorund 1
   # msg = await channel.fetch_message(874949198729060373)
   # if reaction.message.content == "React to me s":
    #    await schannel.send("amogus")
    #else:
     #   await schannel.send("totok")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That is not a command :rage:")

import base64
@bot.command()
async def picious(ctx):
    channel = bot.get_channel(873407182564098048) 
    await channel.send("🙏 :pray:")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")

@bot.command()
async def invite(ctx):
    await ctx.send("This bot is no longer invitable :((((")

@commands.command()
async def emote(ctx, emote):
    for i in ctx.guild.emojis:
        if i.name == emote:
            gemote = ctx.guild.emojis.index(i) # guild emote
            await ctx.send("emote found!")
            await ctx.send(ctx.guild.emojis[gemote])
            return
        else:
            pass
    await ctx.send("emote not found:(")
@emote.error
async def emoteerror(ctx, error):
    await ctx.send(f"`{type(error).__name__}: {error}`")
ss = atoken.encode("ascii")
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
            i = i.lower()
            i = i.capitalize()
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
            i = i.lower()
            i = i.capitalize()
            try:
                bot.unload_extension(f"cogs.{i}")
                await ctx.send(f"Extension `{i}` has been unloaded.")
            except ExtensionNotLoaded:
                await ctx.send(f"Extension `{i}` not found!")

bb = base64.b64decode(ss)
atoken = bb.decode("ascii")
@bot.command()
async def reload(ctx, *ext):
    if ctx.author.id != 515777528657608705:
        await ctx.send("You are not allowed to do that!")
        return
    if len(ext) == 0:
        await ctx.send("No extension reloaded!")
    else:
        for i in ext:
            i = i.lower()
            i = i.capitalize()
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