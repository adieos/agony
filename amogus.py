from discord.ext import commands
from suspisus import token

bot = commands.Bot(command_prefix="sus ")

@bot.event
async def on_ready():
    print(bot.user.name+" is online.")

@bot.command()
async def picious(ctx):
    await ctx.send("amogus")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")

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
        key = key(int)
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
        if text == None:
            await ctx.send("Nothing to encrypt!")
        else:
            await ctx.send(f"Your new password is `{password}")
    except TypeError:
        await ctx.send("Hey! Input a valid number!")


bot.run(token)