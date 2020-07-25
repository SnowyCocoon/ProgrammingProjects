import discord
from discord.ext import commands

class TestgroundCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test Cog is Working')

    @commands.command()
    async def image(self, ctx):
        file = discord.File("./HaruImages/HaruBot.png", filename="HaruBot.png")
        await ctx.channel.send("HaruBot.png", file=file)

    #@commands.command()
    #async def image2(self, ctx):
    #    file = discord.File("https://pbs.twimg.com/media/ENs5MH1XsAAPWRh.jpg", filename="HaruBotx")
    #    await ctx.channel.send("HaruBotu", file=file)

    #def is_it_me(self, ctx):
    #    return ctx.author.id == 221351971674783754

    @commands.command()
    #@commands.check(is_it_me)
    async def example(self, ctx):
        await ctx.send(f'Hi Im {ctx.author}')


def setup(bot):
    bot.add_cog(TestgroundCommands(bot))