import discord

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


client.run('NTMyNDExMTY5MDgwNjA2NzUz.DyRPoQ.pNEE2GEAvTXYLl9jWJB9YNMOA08')