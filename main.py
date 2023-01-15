import discord
from discord.ext import commands

with open('token.dat', 'r') as file:
    token = file.read()

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user.name} online!")

client.run(token)