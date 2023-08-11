import spacecord

bot = spacecord.Bot('YOUR TOKEN', intents='message; guild; content;')

@bot.add_event
async def on_ready():
  bot.debug('Bot is Ready!')
  bot.tree.sync()

@bot.add_command('quiz','quiz')
async def course_command(ctx: spacecord.Context):
  await ctx.response.defer()
  embed = spacecord.BuildedEmbed.InfoEmbed('QUIZ TIME!')
  embed.add_author(ctx.user,ctx.user.avatar.url)

  options = [
    spacecord.SelectOption(label="Paris"),
    spacecord.SelectOption(label="London"),
    spacecord.SelectOption(label="Berlin")
  ]
  select = spacecord.Select(placeholder='Select your choice',options=options,minvalue=1,maxvalue=1)
  async def callback(ctx: spacecord.Context, button: spacecord.Button, correct: bool):
    if correct:
      await ctx.response.send_message(embed=spacecord.BuildedEmbed.SuccessEmbed('Correct answer! You answered correctly"),ephemeral=True)
    else:
      await ctx.response.send_message("Incorrect answer!",ephemeral=True)
  
  view = spacecord.BuildedView.quiz(ctx, embed, 'What is the capital of France?',select,callback, options,timeout=60)

