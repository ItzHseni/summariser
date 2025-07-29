from discord.ext import commands
from core.summaryHandler import getSummary
import discord

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name='Get Summary')
    async def summary(self, ctx, message: discord.Message):
        
        summary = await getSummary(message.content)
        await ctx.respond(summary, ephemeral=True)

def setup(bot):
    bot.add_cog(Greetings(bot))