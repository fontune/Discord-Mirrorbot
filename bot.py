import discord
import asyncio

# This is the token of the user account which has access to the channel where the messages
# are being mirrored from
userToken = ""

# This is the token of the bot account, which can be created
# at https://discordapp.com/developers/applications/
botToken = ""

# ID of the channel where the messages are being mirrored from
# the user account needs permission to read messages in this channel
sourceChannelID = ""

# ID of the channel where the messages are being mirrorered to
# the bot account needs permission to send messages in this channel
targetChannelID = ""

botClient = discord.Client()
userClient = discord.Client()

@userClient.event
async def on_ready():
    print("User account connected")
    print(userClient.user.name)
    print(userClient.user.id)
    print("-------")

@botClient.event
async def on_ready():
    print("Bot account connected")
    print(botClient.user.name)
    print(botClient.user.id)
    print("-------")

def build_embed(authorName, authorPicture, embedDesc, embedColor):
    emb = discord.Embed()
    emb.set_author(name=authorName, url="", icon_url=authorPicture)
    emb.description = embedDesc
    emb.color = embedColor
    return emb

@botClient.event
async def send_message(messageEmbed):
    channel = botClient.get_channel(int(targetChannelID))
    await channel.send(embed=messageEmbed)

@userClient.event
async def on_message(message):
    if message.channel.id == int(sourceChannelID):
        authorName = message.author.name + "#" + message.author.discriminator
        await send_message(build_embed(authorName, message.author.avatar_url, message.clean_content, message.author.color))

loop = asyncio.get_event_loop()
task1 = loop.create_task(userClient.start(userToken, bot=False))
task2 = loop.create_task(botClient.start(botToken))
gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)
