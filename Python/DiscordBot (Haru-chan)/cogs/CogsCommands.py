import discord
from discord.ext import commands

class CogsCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs-Cog is Working')

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')

    @load.error
    async def load_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing argument! After "load" please type one of the avalible cogs :carrot:')

    @commands.command()
    async def unload(self, ctx, extension):
        print(extension)
        if(extension != 'CogsCommands'):
            self.bot.unload_extension(f'cogs.{extension}')
        else:
            await ctx.send('You can\'t unload this cog!')
            print('Erro cog')

    @unload.error
    async def unload_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing argument! After "unload" please type one of the avalible cogs :carrot:')

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')

    @reload.error
    async def reload_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing argument! After "reload" please type one of the avalible cogs :carrot:')

def setup(bot):
    bot.add_cog(CogsCommands(bot))