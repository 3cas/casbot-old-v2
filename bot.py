from nextcord import *
from nextcord.ext import commands
import logging

from ext.util import *
from ext.admin import *
from ext.test import *
from ext.misc import *

client = Client()

logging.basicConfig(level=logging.INFO)

mains = [929931487279718490] # real
bot_admins = [743340045628342324, 901978388829450291, 945222635573366845] # >>, aRealOne, CASbot

client.add_cog(Admin(client))
client.add_cog(Test(client))
client.add_cog(Misc(client))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

with open("C:\\Users\\casga\\Desktop\\bot-token.txt", "r") as f:
    TOKEN = f.read()

client.run(TOKEN)