import discord, asyncio
from config import *

client = discord.Client()
counting_channel = 621720055692132372

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Coutning"))
    print(f'{client.user} logged in!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel.id
    messages = await message.channel.history(limit=5).flatten()
    if channel == counting_channel:
        two = int(messages[1].content)
        one = int(messages[0].content)
        if one == two +1:
            await message.add_reaction("✅")
        else:
            await messages[0].delete()
            reply = await message.channel.send(f'<@{message.author.id}>, wrong number, the current number is {two}')
            await asyncio.sleep(1)
            await reply.delete()

client.run(token)