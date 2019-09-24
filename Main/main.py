import discord
from discord import Embed, Game

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
    await client.change_presence(activity=discord.Activity(type=0, name="Mission Listen & Kill"))


@client.event
async def on_message(message):
    if message.content.startswith(Static.Prefix):
        invoke = message.content[len(Static.Prefix):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.channel, embed=Embed(color=discord.Color.red(), descriotion=(
                        "Der Befehl '%s' ist nicht gültig!!!" % invoke)))

@client.event
async def on_member_join(member):
    await client.send_message(member, "css b,i Befehle des Bots:"
                                   "**Invoke:  **                                    !"
                                   "**Befehle: **                                   !help"
                                   "**Nachrichten löschen:**            !clear"
                                   "**Kick:**                                          !kick"
                                   "**Youtube:**                                  !yt"
                                   "** Regeln Musikplayer: **"
                                           "Musik kann nur ab Vize/Admin hinzugefügt werden."
                                           "Wenn man bestimmte Lieder hören möchte,"
                                           "kann einem Admin eine PN mit den Liedern geschrieben werden."
                                           "Die Maximale Anzahl an Liedern beträgt 15,"
                                           "dementsprechend auch bei einer Playlist nur mit Maximal 15 Liedern."
                                           "Die Lieder sollten eine Maximal Laufzeit von 15 Minuten nicht überschreiten.```")


client.run(Secret.TOKEN)
