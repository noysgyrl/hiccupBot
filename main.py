# Welcome to hiccupBot.
# Discord bot to count hiccups. Created March 2023.

import discord
import os
import random
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Custom help command menu
class CustomHelp(commands.MinimalHelpCommand):
    async def send_bot_help(self, mapping):
        entries = ""
        for command in bot.commands:
            entries += f"{command}     \U0001F920     {command.help}\n"
        title = "You have reached the HELP MENU! (It's a list of all my commands. !command for more info!)"
        embed = discord.Embed(title=title, description=entries,color=discord.Color.blue())
        channel = self.get_destination()
        await channel.send(embed=embed)
    async def send_command_help(self, command):
        embed = discord.Embed(title=command, description=command.brief, color=discord.Color.blue())
        channel = self.get_destination()
        await channel.send(embed=embed)
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        channel = self.get_destination()

        await channel.send(embed=embed)

bot.help_command = CustomHelp()

# on_message functionality
@bot.event
async def on_message(message):
    if message.content == "Hello hiccupBot!":
        await message.channel.send("Hello, " + str(message.author))
    if message.content == "Goodnight, hiccupBot":
        await message.channel.send("Goodnight, " + str(message.author))

    # allow command processing
    await bot.process_commands(message)

@bot.command(
    name="eeps",
    help="+1 hiccup!",
    brief="Adds +1 hiccup to the counter. !hiccup also works for this.")
async def hiccup1(ctx):
    newCount = "broken!!"
    async for message in ctx.channel.history(limit=200, oldest_first=True):
        if "Oh no. Hiccup count: " in message.content:
            temp = message.content.replace("Oh no. Hiccup count: ", "")
            newCount = int(temp) + 1
    await ctx.channel.send(f"Oh no. Hiccup count: {newCount}")

@bot.command(
    name="hiccup",
    help="+1 hiccup!",
    brief="Adds +1 hiccup to the counter. !eeps also works for this.")
async def hiccup2(ctx):
    newCount = "broken!!"
    async for message in ctx.channel.history(limit=200, oldest_first=True):
        if "Oh no. Hiccup count: " in message.content:
            temp = message.content.replace("Oh no. Hiccup count: ", "")
            newCount = int(temp) + 1
    await ctx.channel.send(f"Oh no. Hiccup count: {newCount}")

bot.run("TOKEN") # BOT TOKEN HERE
