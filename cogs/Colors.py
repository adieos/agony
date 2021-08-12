import discord
from discord.ext import commands

class Colors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        if user.bot:
            return
        
        if reaction.emoji == "❤️":
            crole = discord.utils.get(user.guild.roles, name="Red")
            await user.add_roles(crole)
        elif reaction.emoji == "💙":
            crole = discord.utils.get(user.guild.roles, name="Blue")
            await user.add_roles(crole)
        elif reaction.emoji == "💛":
            crole = discord.utils.get(user.guild.roles, name="Yellow")
            await user.add_roles(crole)
        elif reaction.emoji == "💚":
            crole = discord.utils.get(user.guild.roles, name="Green")
            await user.add_roles(crole)
        
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel
        if user.bot:
            return
        
        if reaction.emoji == "❤️":
            crole = discord.utils.get(user.guild.roles, name="Red")
            await user.remove_roles(crole)
        elif reaction.emoji == "💙":
            crole = discord.utils.get(user.guild.roles, name="Blue")
            await user.remove_roles(crole)
        elif reaction.emoji == "💛":
            crole = discord.utils.get(user.guild.roles, name="Yellow")
            await user.remove_roles(crole)
        elif reaction.emoji == "💚":
            crole = discord.utils.get(user.guild.roles, name="Green")
            await user.remove_roles(crole)

    @commands.command()
    async def callcolor(self, ctx):
        if ctx.author.id != 515777528657608705:
            await ctx.send("You cant do that hhhhh")
            return

        ebd = discord.Embed(
            title = "Colors",
            description = "uhh react to these stuffs for colors yep"
        )
        ebd.add_field(
            name = "Primary Colors",
            value = "<@&874283722625667102>\n<@&874283643248455680>\n<@&874283521034833970>\n<@&874224696655224844>",
            inline = False
        )
        msg = await ctx.send(embed=ebd)
        
        emojis = ["❤️", "💙", "💛", "💚"]
        channel = self.client.get_channel(874999244073865268)
        for i in emojis:
            await msg.add_reaction(i)

def setup(client):
    client.add_cog(Colors(client))