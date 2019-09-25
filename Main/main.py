from _multiprocessing import send

import discord
from discord import Embed, Game, abc
from discord.ext.commands import bot

from PuReBot.Main import Static
from PuReBot.Permissions import Secret
from PuReBot.Commands import help

client = discord.Client()

commands = {

    "help": help,

}


@client.event
async def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    [(lambda s: print("  - %s (%s)" % (s.name, s.id)))(s) for s in client.guilds]
    await client.change_presence(activity=discord.Activity(type=0, name="Listen & Kill"))


@client.event
async def on_message(message):
    if message.content.startswith(Static.Prefix):
        invoke = message.content[len(Static.Prefix):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await abc.Messageable.send(message.channel, embed=Embed(color=discord.Color.red(), description=(
                        "Der Befehl '%s' ist nicht gültig!!!" % invoke)))

@client.event
async def on_member_join(member):
    await abc.Messageable.send(member, "##Willkommen %s!\n"
                                      "\n"
                                      "Auf dem %s Server von %s!\n"
                                      "Wenn du möchtest kannst du etwas über dich in den %s Channel eintragen.\n"
                                      "Hab Spaß und einen schönen Tag!\n"
                                      "`Zum Nutzen des Musikbots benutzt / vor dem Befehl, wenn ihr die Befehle nicht kennt, könnt ihr euch eine Befehlsliste mit /help zusenden lassen.\nViel Spaß noch auf dem Server!`"
                               % (member.name, member.guild.name, member.guild.owner.mention, discord.utils.get(member.guild.channels, id=530919958503227392).mention))


client.run(Secret.TOKEN)
