import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')


client.run('Nzk4MDc2NjY4MDg1OTI3OTc2.X_vw0Q.2OWoUlqZZ7Z0snLEeNSBA4wD7fY')
