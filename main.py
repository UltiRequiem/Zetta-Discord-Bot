# -*- coding: utf-8 -*-

import os
import datetime
import discord
import asyncio
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands

from urllib import parse, request
import re

bot = commands.Bot(command_prefix="z!", case_insensitive=True)

bot.author_id = 413720448627638274  # Change to your discord id!!!

#-----------Text Commands----------------


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!\n{round(bot.latency * 1000)}ms")


@bot.command()
async def repeatm(ctx, times: int, content: str):
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def message(ctx, member: discord.Member, *, content):
    await member.send(content)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # print(search_results) // No Thanks
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Server data:",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.red())
    embed.add_field(name="Server created at:", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner:", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region:",
                    value=f"{ctx.guild.region}".capitalize())
    embed.add_field(name="Server ID:", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)


#------------Math Utilities---------------------


@bot.command()
async def calcula(ctx, num_one: int, simbol: str, num_two: int):
    if simbol == '+':
        await ctx.send(num_one + num_two)
    elif simbol == '-':
        await ctx.send(num_one - num_two)
    elif simbol == '/':
        await ctx.send(num_one / num_two)
    elif simbol == '*':
        await ctx.send(num_one * num_two)
    else:
        await ctx.send('Uhhh.')


#------------Mod Utilities---------------------


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")


@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await member.send(
        f"You have been warned in {ctx.guild.name} for : {reason}")
    await ctx.send(f"Warned {member.mention} for : {reason}")


#------------Events---------------------
@bot.event
async def on_ready():
    print("I'm in.")
    print(bot.user)
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="Zero Requiem"))


# TODO Fix this:
'''
@bot.listen()
async def on_message(message):
    if "zero" in message.content.lower():
        await message.channel.send('Zero Requiem')
        await bot.process_commands(message)
'''


extensions = ['cogs.cog_example','music']

# ---------- Load Extensions ------------------------------
if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

# --------------- Bot Password------------------
keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)  # Starts the bot
