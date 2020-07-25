import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle


with open('./config.json') as f:
  data = json.load(f)

bot = commands.Bot(command_prefix= f'{data["prefix"]}')
status = cycle(['Boting in Runescape!', 'Doing that thing, that rabbits do the best ;)'])

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    change_status.start()
    #await bot.change_presence(status=discord.Status.online, activity=discord.Game('Boting in Runescape!'))
    print('Bot is ready')

@tasks.loop(seconds=120)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used! Type <>help to check all avalible commands :carrot: :heart:')

bot.run(f'{data["token"]}') #Private bot token