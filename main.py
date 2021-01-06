import os
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(
	command_prefix="z!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

client.author_id = 487258918465306634  # Change to your discord id!!!

#Ping command
@client.command()#You can added inside the () either "aliases=['Command Alias']" OR "help = 'Command Description'"
async def ping(ctx):
    await ctx.send(f"Pong!\n{round(client.latency * 1000)}ms") #The "\n" is used to start another line

@client.event 
async def on_ready():  # When the bot is ready
    print("Me prendi")
    print(client.user)  # Prints the bot's username and identifier

@client.event
async def on_message(message):
  
    if message.content.startswith('gay'):
        await message.channel.send(':point_up_2: :rainbow_flag:')

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		client.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
client.run(token)  # Starts the bot
