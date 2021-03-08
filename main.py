from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
# we need members intent too
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print("The bot is online!")
	bot.load_extension("cogs.onMessage")

bot.run(os.environ.get("ODE3MjYxODQyMjQxNjgzNDg3.YEG8Zw.D7xLAMzuXZ0BezOtK7OdcLFtNx4"))
