import discord
from discord.ext import commands
import random

class FunCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog is Working')

    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! Latency: {round(self.bot.latency * 1000)} ms')

    @commands.command(aliases=['Hello', 'hi', 'Hi'])
    async def hello(self, ctx):
        await ctx.send('Hello Luv :heart:')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question): #Multiple argument as one "*"
        responses = responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @_8ball.error
    async def _8ball_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in clear req arguments!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return #We dont want any loops

        if message.content.startswith('Beastars') or message.content.startswith('beastars'):
            await message.channel.send('Beastars is the best anime!')
        if message.content.startswith('Haru') or message.content.startswith('haru'):
            await message.channel.send('Hi Luv. My name is Haru. Your virtual rabbit :carrot: :heart:. Type "<>help" to see what can i do!')
            await self.bot.process_commands(message) #This line allows us to run the bot with this sort of events



def setup(bot):
    bot.add_cog(FunCommands(bot))