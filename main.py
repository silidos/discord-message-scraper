import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        if type(message.channel) is discord.channel.DMChannel:
            await message.channel.send('Received message: ' + message.content)

client.run('<Bot token here>')