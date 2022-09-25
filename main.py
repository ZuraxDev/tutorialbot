import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents= intents)

@bot.event
async def on_ready():
    print("Bot is online")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Test status :D"))

@bot.command()
async def test(ctx):
    await ctx.send("test :D")
    print("test command activated :D")

bot.run("TOKEN HERE")
