import discord
import os
import json
import fire
import requests
from typing import List
import subprocess
import subprocess as sp
import asyncio
from subprocess import call

output = sp.getoutput('pip install pydadjoke')

client = discord.Client()


@client.event
async def on_ready():
    print("we are logged in as {0.user}".format(client))
    await client.change_presence(
        activity=discord.Game('$joke  - for disappointment'))


path_help = '$help.txt'
path_dm = 'dmd.txt'
path_joke = '$joke.txt'


@client.event
async def on_message(message):
    id = client.get_guild(827251091153748009)
    channels = ['special']

    if message.author == client.user:
        return

    if message.content.startswith("$joke"):
        output = sp.getoutput('pydadjoke joke')
        await message.channel.send(output)
        print('told a joke')
        joke_object = message.author
        joke_object_str = str(joke_object)
        joke_file = open(path_joke, 'a')
        joke_file.write(joke_object_str + ';   ')
        joke_file.close()

    if message.content.startswith("$dm me"):
        output = sp.getoutput('pydadjoke joke')
        await message.author.send(output)
        print('dmd a joke')
        dm_object = message.author
        dm_object_str = str(dm_object)
        dm_file = open(path_dm, 'a')
        dm_file.write(dm_object_str + ';   ')
        dm_file.close()

    if str(message.channel) in channels:
        if message.content.startswith('$memcount'):
            await message.channel.send(f"""Member count: {id.member_count} """)

    if message.content.startswith('$help'):
        await message.author.send('proper help embeed in progress, for now just use the commands: $joke, $dm, $beemovie')
        print(f"""just instructed {message.author}""")
        help_dm_object = message.author
        help_dm_object_str = str(help_dm_object)
        help_file = open(path_help, 'a')
        help_file.write(help_dm_object_str + ';   ')
        help_file.close()
        await message.channel.purge(limit=1)
        
    if message.content.startswith("$beemovie"):
      await message.author.send("""According to all known laws of aviation, there is no way a bee should be able to fly.""")
   
    if message.content.startswith("$beemovie_full"):
      await message.author.send("""https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script""")

client.run(os.getenv("TOKEN"))
