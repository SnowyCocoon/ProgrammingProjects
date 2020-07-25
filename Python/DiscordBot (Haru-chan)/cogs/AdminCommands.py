import discord
from discord.ext import commands

class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin Cog is Working')

    @commands.command()
    @commands.has_permissions(manage_messages=True) #Sprawdzanie permisji
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for {reason}')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server :)')
        #member.channel.send('Hello ' + {member} + ':heart:') #Testing welcome messge

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server :(')

def setup(bot):
    bot.add_cog(AdminCommands(bot))