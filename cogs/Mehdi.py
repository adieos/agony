import discord
from discord.ext import commands

class Mehdi(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def latity(self, ctx, eps=None):
        try:
            mehdititle = mehdiurl = mehditn = mehdidesc = None
            if eps is None:
                helpebd = discord.Embed(
                    title = "Latity",
                    description = "Used if you want to watch one of ElectroBOOM's Latity\n(Last Time I Told You) series.",
                    color = 0x9c5513
                )
                helpebd.add_field(
                    name = "Syntax",
                    value = "`sus latity <eps>`",
                    inline = False
                )
                helpebd.set_thumbnail(url="https://cdn.discordapp.com/attachments/746991157766127678/869185583430389810/mehdi.jpg")
                helpebd.set_footer(text="This embed is not affiliated with ElectroBOOM whatsoever hhh")
                await ctx.send(embed=helpebd)
                return

            eps = int(eps)
            if eps == 0:
                await ctx.send("Episodes start at 1!")
                return
            elif eps == 1:
                mehdititle = "ORIGINAL CONCEPT: Reviewing Your Reddit Submissions"
                mehdiurl = "https://www.youtube.com/watch?v=Ok05GFoESGE"
                mehditn = "https://cdn.discordapp.com/attachments/746991157766127678/869900994346090526/Latity_01.jpg"
                mehdidesc = "Let me review some of your submissions. Maybe we learn something?"
            elif eps == 2:
                mehdititle = "Making Water Spin Like Magic, LATITY-002"
                mehdiurl = "https://www.youtube.com/watch?v=E3VousBUEd4"
                mehditn ="https://cdn.discordapp.com/attachments/746991157766127678/873400792822993037/Latity_02.jpg"
                mehdidesc = "Let's review your deepest questions in another \"LAst Time I Told You\""
            elif eps == 3:
                mehdititle = "MAGNET IMPLANT Gives You Powers!!! (LATITY-003)"
                mehdiurl = "https://www.youtube.com/watch?v=KIWlVW9Hybc"
                mehditn = "https://cdn.discordapp.com/attachments/746991157766127678/873402361199095878/Latity_03.jpg"
                mehdidesc = "Can I implant a MAGNET in my finger and FEEL ELECTRICITY?! Let me check your submissions..."
            elif eps == 4:
                mehdititle = "Charging Phone DANGEROUS?! ElectroBOOM Crew EXPOSED!!! (LATITY-004)"
                mehdiurl = "https://www.youtube.com/watch?v=iX1Myc51Pvc"
                mehditn = "https://cdn.discordapp.com/attachments/746991157766127678/873405757629038652/Latity_04.jpg"
                mehdidesc = "Didn’t you want to meet ElectroBOOM team? Well, watch the video!"
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

    @commands.command()
    async def embed(self, ctx):
        ebd = discord.Embed(
            title="Circuit, Series, and Parallel",
            url="https://www.youtube.com/watch?v=AMXWm_bnsTE",
            description="ElectroBOOM101 - Eps. 005",
            color = 0x9c5513
        )
        ebd.set_author(
            name=ctx.author.display_name,
            url="https://www.youtube.com/watch?v=5DlROhT8NgU",
            icon_url=ctx.author.avatar_url
        )
        ebd.set_thumbnail(url="https://cdn.discordapp.com/attachments/746991157766127678/869185583430389810/mehdi.jpg")
        ebd.add_field(
            name="Circuit",
            value="Mehdi Sadaghdar explains what a circuit is",
            inline=False
        )
        ebd.add_field(
            name="Series",
            value="Mehdi explains how a series circuit behaves",
            inline=True
        )
        ebd.add_field(
            name="Parallel",
            value="Mehdi explains how a parallel circuit behaves",
            inline=True
        )
        ebd.set_footer(text="This embed is not affiliated with ElectroBOOM whatsoever hhh")
        await ctx.send(embed=ebd)
        
def setup(client):
    client.add_cog(Mehdi(client))