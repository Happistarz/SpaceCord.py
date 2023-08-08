
[Logo](https://github.com/Happistarz/SpaceCord.py/blob/main/Sans%20titre.png)


# SpaceCord.py

SpaceCord.py is a addon of discord.py designed to simplify the development of Discord bots. It offers a powerful and comprehensive catalog of features to improve your efficiency and enable sofistical systems with ease.
It is really beneficial for beginner and senior developers.


### Documentation

[Documentation](https://linktodocumentation)


## Roadmap

- BETA v1.0
    - View manager
    - Embed building
    - Reaction handler
    - Permission handler


## Run Locally

Install dependencies

```bash
  pip install -U spacecord.py
```

Import the module

```python
import spacecord
```

## Usage/Examples

Quick example of a basic command and basic event
```python
import spacecord

bot = spacecord.Bot("TOKEN",intents="YOUR INTENTS")

@bot.add_event()
async def on_ready():
    await bot.debug("Bot is ready!")


@bot.bot.add_command('ping',"send ping")
async def ping_comand(ctx: spacecord.Context):
    await ctx.response.send_message("Pong",embed=spacecord.BuildedEmbed.InfoEmbed("Pong!"))

@bot.bot.add_command('name_of_the_command',"description_of_the_command")
async def name_of_the_function(ctx: spacecord.Context):
    """
    The documentation to help you keep in mind what this function does.
    Also this doc is not essential. If wouldn't, simply remove this."""
    
    # do stuff here...
    # Have fun!

```


## Main package

Also check out the main package if SpaceCord.py has not a features
- [Reference to discord.py](https://pypi.org/project/discord.py/)
