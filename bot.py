import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CANAL_ID = int(os.getenv("CANAL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

    canal = bot.get_channel(CANAL_ID)
    if canal:
        await canal.send("Bot online 🚀")
    else:
        print("Canal não encontrado.")

bot.run(TOKEN)