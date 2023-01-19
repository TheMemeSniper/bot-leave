from nextcord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@commands.command()
async def eject(ctx, serverid):
    guild = bot.get_guild(int(serverid))
    await guild.leave()
    print(f"Left guild {serverid}")

bot.add_command(eject)


bot.run("no get your own token!!!! >:(")