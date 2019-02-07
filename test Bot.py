import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")

    print(client.user.name)

    print(client.user.id)

    print("------------------")

    await client.change_presence(game=discord.Game(name='test Bot 대기중', type=0))

@client.event
async def on_message(message):
    if message.content.startswith('hi'):
        await client.send_message(message.channel, "hello world!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
