# Discord-Mirrorbot

Discord-Mirrorbot allows for a channel that can be accessed by a user account to be mirrored elsewhere, output by a bot account.

### Setup

Discord-Mirrorbot requires [Python 3.6 or above](https://www.python.org/downloads/) installed to run.

Change current working directory to the project folder.
```ps
cd Discord-Mirrorbot
```
Install the requirements.
```ps
# Windows
py -3 -m pip install -r requirements.txt
# Linux/MacOS
python3 -m pip install -r requirements.txt
```

Set the relevant tokens and channel IDs on lines 7, 11, 15 & 19.
```py
7   userToken = ""
11  botToken = ""
15  sourceChannelID = ""
19  targetChannelID = ""
```

Finally, run the bot...
```ps
# Windows
py -3 bot.py
# Linux/MacOS
python3 bot.py
```

### Todos
 - Add support for multiple images/attachments in a single message
 - Clear clutter by editing a single embed if a user sends more than one message at once
 - Add a way of showing user emoji reactions to messages
 - Add support for channel events such as pins, deleted messages, nickname changes etc.

License
----

MIT
