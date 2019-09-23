import asyncio
import discord

from PuReBot.Main import Static
from PuReBot.Permissions import Secret
from PuReBot.Commands import help

client = discord.Client()

commands = {

    "help": help,


}

@client.event
@asyncio

def on_ready():
    await client.send_message()

def on_message(message):
    if message.content.startswith(Static.Prefix):
        invoke = message.content[len(Static.Prefix):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("Invoke: %s\nARGS: %s" % (invoke, args.__str__)()[1:-1].replace("'"," "))

client.run(Secret.TOKEN)
