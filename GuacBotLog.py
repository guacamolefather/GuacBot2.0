import discord
from discord.ext import commands
import re
import os

channel_names = []
channel_ids = []

def GetChannelList():
    for guild in client.guilds:
        for channel in guild.text_channels:
            channel_names.append(channel)
            channel_ids.append(channel.id)
    for i in channel_names:
        print(str(channel_names.index(i)) + " - " + str(i) + " - " + str(channel_ids[channel_names.index(i)]))
    
def PickServer():
    server = 31
    server = int(input("Which channel do you want the record of? "))
    channel = client.get_channel(channel_ids[server])
    return channel

client = discord.Client()
@client.event
async def on_ready():
    GetChannelList()
    channel = PickServer()
    line = ""
    while line == "":
        line = input("Servers, Quit, or Fetch Records? ")
        if str.lower(line) == "servers":
            os.system('cls')
            GetChannelList()
            channel = PickServer()
        elif str.lower(line) == "quit":
            quit()
        else:
            messages = await channel.history(limit=None).flatten()
            os.system('cls')
            for message in messages:
                print(str(message.author) + " - " + message.content + "\n")
        line = ""

TOKEN = open("TOKEN.txt", "r").read()
client.run(TOKEN)
