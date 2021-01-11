  
import os
from keep_alive import keep_alive
from discord.ext import commands
import discord

client = commands.Bot(command_prefix='uwu ') 
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!\n{round(client.latency * 1000)}ms") 


@client.event
async def on_ready():
    game = discord.Game('Killing Furrys')
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Me prendi uwu')


@client.command() 
async def ban(ctx, member : discord.Member, *, reason=None): 
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")



@client.command() 
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")

@client.event
async def on_message(message):
  
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('gay'):
        await message.channel.send(':point_up_2: :rainbow_flag:')

    if message.content.startswith('Loli'):
      await message.channel.send("What's up?")

@client.command() 
async def warn(ctx, member : discord.Member, *, reason=None):
    await member.send(f"You have been warned in {ctx.guild.name} for : {reason}")
    await ctx.send(f"Warned {member.mention} for : {reason}")

 
extensions = [
	'cogs.cog_example' 
]

if __name__ == '__main__':  
	for extension in extensions:
		client.load_extension(extension) 

keep_alive()  
token = os.environ.get("DISCORD_BOT_SECRET") 
client.run(token) 
