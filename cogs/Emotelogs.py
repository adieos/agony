import discord
from discord.ext import commands
from datetime import datetime

class EmoteLog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        channel = self.client.get_channel(877703041145507871)
        removed = set(before) - set(after)
        added = set(after) - set(before)
        timern = datetime.now().strftime("%d/%m/%Y")
        if len(added) != 0:
            ladded = tuple(added)
            emote = ladded[0]
            # Embed config
            etitle = "Emoji Added"
            edesc = f"{emote}  {emote.name}"
            efoot = f"ID: {emote.id} • {timern}"
            ecolor = 0x19e312
        elif len(removed) != 0:
            lremoved = tuple(removed)
            emote = lremoved[0]
            etitle = "Emoji Removed"
            edesc = f"{emote.name}"
            efoot = f"ID: {emote.id} • {timern}"
            ecolor = 0xdb1009
        else:
            # Approach: making a union, then substract the union from one of the remove/after set
            # update: DOES NOT WORK. PAIN 
            etitle = "Emoji Renamed"
            edesc = "I dont know how to access the emote names :pensive:"
            efoot = f"ID: IDK HOW TO ACCESS IT • {timern}"
            ecolor = 0xdfed18

        ebd = discord.Embed(
            title = etitle,
            description = edesc,
            color = ecolor
        )
        ebd.set_footer(text=efoot)
        await channel.send(embed=ebd)
        # use before - after or vice versa !

    @commands.command()
    async def amogus(self, ctx):
        await ctx.send("h")
        ebd = discord.Embed(
            title = "Datetime",
            description = "Datetime"
        )
        ebd.add_field(
            name = "Datetime",
            value = "Datetime"
        )
        ebd.set_footer(
            text = datetime.now().strftime("%H:%M:%S"),
            icon_url = "https://cdn.discordapp.com/attachments/873407182564098048/877729968078090280/ohhiorun.gif"
        )
        await ctx.send(embed=ebd)


def setup(client):
    client.add_cog(EmoteLog(client))