import discord
from discord.ext import commands

class EmoteLog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        channel = self.client.get_channel(873407182564098048)
        await channel.send("Hey, an emote just got added ! (or removed.., idk)")


def setup(client):
    client.add_cog(EmoteLog(client))