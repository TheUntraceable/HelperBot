import discord
from discord.ext import commands
class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready!")
    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.bot.user} has disconnected from Discord!")
    @commands.Cog.listener()
    async def on_resumed(self):
        print(f"{self.bot.user} has reconnected to Discord!")
    @commands.command(description="Gets the bot's current ping.")
    @commands.cooldown(1,5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.reply(f"Currently Active! Client Latency -{round(self.bot.latency * 1000)}ms")
def setup(client):
    client.add_cog(Status(client))
