import discord
from discord.ext import commands
import re

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
    server = 30
    server = int(input("Which channel do you want to type in? "))
    channel = client.get_channel(channel_ids[server])
    return channel

client = discord.Client()
@client.event
async def on_ready():
    GetChannelList()
    channel = PickServer()
    line = ""
    while line == "":
        line = input("What do you want me to say? ")
        if str.lower(line) == "servers":
            channel = PickServer()
        elif str.lower(line) == "quit":
            quit()
        else:
            await channel.send(line)
        line = ""

TOKEN = open("TOKEN.txt", "r").read()
client.run(TOKEN)
