import discord
from discord.ext import commands

class Latity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def latity(self, ctx, eps=None):
        try:
            mehdititle = mehdiurl = mehditn = mehdidesc = None
            if eps is None:
                eps = 1

            if eps == 1:
                mehdititle = "ORIGINAL CONCEPT: Reviewing Your Reddit Submissions"
                mehdiurl = "https://www.youtube.com/watch?v=Ok05GFoESGE&list=PLr_CZLgMkHeUxA1-DMSACtLF_1LP-a5DY&index=1&t=123s"
                mehditn = "https://cdn.discordapp.com/attachments/746991157766127678/869900994346090526/Latity_01.jpg"
                mehdidesc = "Let me review some of your submissions. Maybe we learn something?"
        except ValueError:
            await ctx.send("Please input a valid number!") 

        ebd=discord.Embed(
            title = mehdititle,
            url = mehdiurl,
            description = f"ElectroBOOM Latity - Eps {eps}",
            color = 0x9c5513
        )
        ebd.add_field(
            name = "Description",
            value = mehdidesc,
            inline = False
        )
        ebd.add_field(
            name = "Support Mehdi Here!",
            value = "http://patreon.com/electroboom",
            inline = True
        )
        ebd.add_field(
            name = "Mehdi Merchandises",
            value = "https://electroboom.creator-spring.com/?",
            inline = True
        )
        ebd.add_field(
            name = "Mehdi Amazon Picks",
            value = "https://www.amazon.com/shop/Electroboom",
            inline = True
        )
        ebd.set_thumbnail(url=mehditn)
        ebd.set_footer(text="This embed is not affiliated with ElectroBOOM whatsoever hhh")
        await ctx.send(embed=ebd)
        
def setup(client):
    client.add_cog(Latity(client))