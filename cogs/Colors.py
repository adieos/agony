import discord
from discord.ext import commands

class Colors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.client.fetch_user(payload.user_id)

        if (user.bot) or (message.id != 876410640976216094):
            return

        # Simplify this soon !!! (half-simplified)
        if payload.emoji.name == "❤️":
            crole = discord.utils.get(payload.member.guild.roles, name="Red")
        elif payload.emoji.name == "💙":
            crole = discord.utils.get(payload.member.guild.roles, name="Blue")
        elif payload.emoji.name == "💛":
            crole = discord.utils.get(payload.member.guild.roles, name="Yellow")
        elif payload.emoji.name == "💚":
            crole = discord.utils.get(payload.member.guild.roles, name="Green")
        else:
            return
        
        await payload.member.add_roles(crole)
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = await self.client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = self.client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        
        if message.id != 876410640976216094:
            return
        
        if payload.emoji.name == "❤️":
            crole = discord.utils.get(guild.roles, name="Red")
        elif payload.emoji.name == "💙":
            crole = discord.utils.get(guild.roles, name="Blue")
        elif payload.emoji.name == "💛":
            crole = discord.utils.get(guild.roles, name="Yellow")
        elif payload.emoji.name == "💚":
            crole = discord.utils.get(guild.roles, name="Green")
        else:
            return

        await member.remove_roles(crole)

    @commands.command()
    async def callco(self, ctx):
        if ctx.author.id != 515777528657608705:
            await ctx.send("You cant do that hhhhh")
            return

        ebd = discord.Embed(
            title = "Colors",
            description = "available colors mmm"
        )
        ebd.add_field(
            name = "Primary Colors",
            value = "<@&874283722625667102>\n<@&874283521034833970>\n<@&874283643248455680>\n<@&874224696655224844>",
            inline = False
        )
        await ctx.send(embed=ebd)

    @commands.command()
    async def primreact(self, ctx, id = None):
        if ctx.author.id != 515777528657608705:
            await ctx.send("You can`t do that hhh")
            return
        if ctx.channel.id != 876410407684800532:
            await ctx.send("You can't run that command here!")
            return
        if id is None:
            await ctx.send("I need the message ID, duh")
            return
        try:
            id = int(id)
        except ValueError:
            await ctx.send("Input a valid number!")
            return
        channel = self.client.get_channel(876410407684800532)
        msg = await channel.fetch_message(id)
        emojis = ["❤️", "💛", "💚", "💙"]
        for i in emojis:
            await msg.add_reaction(i)

def setup(client):
    client.add_cog(Colors(client))