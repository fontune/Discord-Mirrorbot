import discord
import asyncio
import re

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

# Return a string with the url contained in a given string.
def find_url(string):
    url = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)
    return url

# Returns a discord.Embed ready to be sent.
def build_embed(authorName, authorPicture, embedDesc, embedColor, embedImage):
    emb = discord.Embed()
    emb.set_author(name=authorName, url="", icon_url=authorPicture)
    emb.description = embedDesc
    emb.color = embedColor
    messageUrls = find_url(embedDesc)
    if embedImage != "":
        emb.set_image(url=embedImage) 
        print(authorName + " uploaded an image")
    elif len(messageUrls) > 0:
        emb.set_image(url=messageUrls[0])
        print(authorName + " linked an image")
    else:
        print(authorName + ": " + embedDesc)
    return emb

@botClient.event
async def send_message(messageEmbed):
    channel = botClient.get_channel(int(targetChannelID))
    await channel.send(embed=messageEmbed)

@userClient.event
async def on_message(message):
    if message.channel.id == int(sourceChannelID):
        authorName = message.author.name + "#" + message.author.discriminator
        if len(message.attachments) > 0:
            imageURL = message.attachments[0].url
        else:
            imageURL = ""
        await send_message(build_embed(authorName, message.author.avatar_url, message.clean_content, message.author.color, imageURL))

# Async loop allows both clients to run simultaneously.
loop = asyncio.get_event_loop()
task1 = loop.create_task(userClient.start(userToken, bot=False))
task2 = loop.create_task(botClient.start(botToken))
gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)
