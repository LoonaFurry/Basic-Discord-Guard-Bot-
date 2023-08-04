import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
bot.remove_command('help')  # Remove the default help command

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} has been kicked.')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been banned.')

@bot.command()
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f'{member.name} has been muted.')

@bot.command()
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member.name} has been unmuted.')

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages have been cleared.')

@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    # Implement your warning logic here
    await ctx.send(f'{member.name} has been warned.')

@bot.command()
async def tempban(ctx, member: discord.Member, duration: int, *, reason=None):
    # Implement your temporary ban logic here
    await ctx.send(f'{member.name} has been temporarily banned for {duration} hours.')

@bot.command()
async def tempmute(ctx, member: discord.Member, duration: int):
    # Implement your temporary mute logic here
    await ctx.send(f'{member.name} has been temporarily muted for {duration} minutes.')

@bot.command()
async def nickname(ctx, member: discord.Member, *, new_nickname):
    await member.edit(nick=new_nickname)
    await ctx.send(f'{member.name}\'s nickname has been changed to {new_nickname}.')

@bot.command()
async def role(ctx, member: discord.Member, role: discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(f'{member.name} has been removed from the {role.name} role.')
    else:
        await member.add_roles(role)
        await ctx.send(f'{member.name} has been added to the {role.name} role.')

@bot.command()
async def servermute(ctx, member: discord.Member):
    # Implement your server mute logic here
    await ctx.send(f'{member.name} has been server muted.')

@bot.command()
async def serverunmute(ctx, member: discord.Member):
    # Implement your server unmute logic here
    await ctx.send(f'{member.name} has been server unmuted.')

@bot.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f'Slowmode has been set to {seconds} seconds in this channel.')

@bot.command()
async def removeslowmode(ctx):
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send('Slowmode has been removed in this channel.')

@bot.command()
async def lockdown(ctx):
    # Implement your lockdown logic here
    await ctx.send('This channel has been locked down.')

@bot.command()
async def unlock(ctx):
    # Implement your unlock logic here
    await ctx.send('This channel has been unlocked.')

@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{member.name}\'s User Info', color=member.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Username', value=member.name, inline=False)
    embed.add_field(name='Nickname', value=member.nick, inline=False)
    embed.add_field(name='ID', value=member.id, inline=False)
    embed.add_field(name='Joined Server', value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.add_field(name='Joined Discord', value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.add_field(name='Roles', value=', '.join([role.name for role in member.roles[1:]]), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    total_members = len(server.members)
    online_members = len([m for m in server.members if m.status != discord.Status.offline])
    text_channels = len(server.text_channels)
    voice_channels = len(server.voice_channels)
    server_owner = server.owner.name

    embed = discord.Embed(title=server.name, description=server.description)
    embed.add_field(name='Total Members', value=total_members)
    embed.add_field(name='Online Members', value=online_members)
    embed.add_field(name='Text Channels', value=text_channels)
    embed.add_field(name='Voice Channels', value=voice_channels)
    embed.add_field(name='Server Owner', value=server_owner)

    await ctx.send(embed=embed)


bot.run('MTEzMDg5NjA5NTczNjc3MDcwMg.GBcdaT.vyY6zyZMaeCaTVn8cKefMfUQBVk7b3h29WqPY8')
