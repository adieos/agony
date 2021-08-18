import discord
from discord.ext import commands

class EmoteLog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        channel = self.client.get_channel(873407182564098048)
        await channel.send("Hey, an emote just got added ! (or removed.., idk)")
        await channel.send(before)
        removed = before - after
        added = after - before
        if removed is None:
            await channel.send("An emote just got added!")
        elif added is None:
            await channel.send("An emote just got removed!")
        else:
            await channel.send("wtf")
        # use before - after or vice versa !

    @commands.command()
    async def amogus(self, ctx):
        await ctx.send("sus")


def setup(client):
    client.add_cog(EmoteLog(client))