import os
import discord
from dotenv import load_dotenv

load_dotenv("secrets.env")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

token = os.getenv("discordToken")


# List of Cogs
cogs = [
        'summariser'
    ]

# Bot Login Handler
@bot.event
async def on_ready():
    print(f"[+] Logged-in as {bot.user} ({bot.user.id})")
    
    await bot.change_presence(activity=discord.CustomActivity(name="Summarising Stuff"))


for cog in cogs:
    bot.load_extension(f"cogs.{cog}")


bot.run(token)
