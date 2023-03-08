# Welcome to hiccupBot.
# Discord bot to count hiccups. Created March 2023.

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client.dailyCount = 1

@client.event
async def on_ready():
    print("hiccupBot is active on Discord! :D")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!hiccup":
        response = ("Oh no. Daily Hiccup Count: " + str(client.dailyCount))
        await message.channel.send(response)
        client.dailyCount += 1

    if message.content == "Goodnight, hiccupBot":
        await message.channel.send("Goodnight, " + str(message.author))

client.run("TOKEN") # BOT TOKEN HERE
