import discord
from discord.ext import commands
import CommandDesc
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
from hhhh import atoken 
from discord.utils import find
import os

# Help section
class CustomHelpCMD(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        try:
            ebd = discord.Embed(
                title = "Help Command",
                description = f'`List of command in this server.`',
                color = 0xdaa717
            )
            for cog in mapping:
                cmds = ""
                for cmd in mapping[cog]:
                    cmds += f"`{cmd.name}`, "
                ebd.add_field(
                    name = cog.qualified_name if cog is not None else "Base",
                    value = cmds,
                    inline = False
                )
                
            
            await self.get_destination().send(embed=ebd)
        except Exception as e:
            await self.get_destination().send(e)

    async def send_command_help(self, command):
        ebd = discord.Embed(
            title = f"{command.name.capitalize()} Command",
            description = command.brief,
            color = 0xdaa717
        )
        ebd.add_field(
            name = "\u200b \n Usage",
            value = command.description,
            inline = False
        )
        ebd.add_field(
            name = "\u200b \n Information",
            value = command.help,
            inline = False
        )
        await self.get_destination().send(embed=ebd)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="sus ",description="Amogus", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name = "Social Credit Simulator 1989"))
    print(bot.user.name+" is online.")

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("amogus")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That is not a command :rage:")
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("That command is currently disabled!")

import base64

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")

@bot.command()
async def invite(ctx):
    await ctx.send("This bot is no longer invitable :((((")

# @commands.command()
# async def emote(ctx, emote):
#     for i in ctx.guild.emojis:
#         if i.name == emote:
#             gemote = ctx.guild.emojis.index(i) # guild emote
#             await ctx.send("emote found!")
#             await ctx.send(ctx.guild.emojis[gemote])
#             return
#         else:
#             pass
#     await ctx.send("emote not found:(")
# @emote.error
# async def emoteerror(ctx, error):
#     await ctx.send(f"`{type(error).__name__}: {error}`")
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
@load.error
async def loaderror(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("Hey, you can't do that!")

@bot.command()
async def unload(ctx, *ext):
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
@unload.error
async def unloaderror(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("Hey, you can't do that!")

bb = base64.b64decode(ss)
atoken = bb.decode("ascii")
@bot.command()
async def reload(ctx, *ext):
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
@reload.error
async def reloaderror(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("Hey, you can't do that!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
         bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(atoken)