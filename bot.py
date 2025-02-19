import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file (for local testing)
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Create a slash command tree
tree = app_commands.CommandTree(bot)

# Event: Bot is ready
@bot.event
async def on_ready():
    await tree.sync()  # Sync slash commands
    print(f"Logged in as {bot.user}")

# Slash command: Ping
@tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")

# Run the bot
bot.run(TOKEN)
