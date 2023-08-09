import spacecord
import random

bot = spacecord.Bot('YOUR TOKEN', 'message; guild; content')

@bot.event
async def on_ready():
  bot.debug("Bot is ready!")


@bot.add_command("hello","say hello")
async def hello_command(ctx: spacecord.Context):
  await ctx.response.send_message(f"hello {ctx.user.mention}!",ephemeral=True)

@bot.add_command("rand","choose a number between your range choices")
async def rand_command(ctx: spacecord.Context, min: int, max: int):
  if min < max:
    choice = random.randint(min,max)
    await ctx.response.send_message(f"Choosed {choice}!")
  else:
    await ctx.response.send_message(embed=spacecord.BuildedEmbed.ErrorEmbed('Please provide valid range'),ephemeral=True)

@bot.add_command("8ball",'i answer your question but not as good as i am')
async def ball_command(ctx: spacecord.Context, question: str):
  responses = [
    "Yes.",
    "No.",
    "Better not to know it.",
    "He's not wrong...",
    "Never.",
    "Always as i can.",
    "Chances high.",
    "Not sure.",
    "Repeat plz.",
    "?????!!!"
  ]
  response = random.choice(responses)
  embed = spacecord.EmbedBuilder("","", spacecord.Color.RED)
  embed.add_field("{ctx.user.mention} says: ",f"```{question}```")
  embed.add_field("My response: ",response)
  embed.set_author(ctx.user.name,url=ctx.user.avatar.url)
  
