import discord
import os

from discord.ext import commands

token = "TheTokenHere"
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=".", case_insensitive=True,intents=intents)

for filename in os.listdir(R"./cogs"):
    if filename.endswith(".py"):
       bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)
