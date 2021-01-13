import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot is ready")



@client.command()
async def Info(ctx):
    await ctx.send("This is a magic 8ball bot that lets you aks the 8ball quastions")

@client.command()
async def q(ctx, *,question):

    responses = [
        "It is certain",
        "It is decidedly so",
        "Yes – definitely",
        "You may rely on it",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"

    ]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

client.run('Nzk4MDc2NjY4MDg1OTI3OTc2.X_vw0Q.2OWoUlqZZ7Z0snLEeNSBA4wD7fY')
