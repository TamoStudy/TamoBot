import discord
import random
from discord import Embed
from discord.ext import commands
from discord import app_commands
from tamo_secrets import TamoSecrets

# set up the bot client with intents
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
allowed_server = int(TamoSecrets.get_server())

@bot.event
async def on_ready():
    # bot is only allowed on allowed servers
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        if guild.id != allowed_server:
            await guild.leave()
        else:
            print(f'- {guild.name} (id: {guild.id})')

    # Set status message
    await bot.change_presence(activity=discord.Game(name="$help | narlock.dev"))

    # Sync commands
    synced = await bot.tree.sync()
    print('Slash CMDS Synced: ' + str(len(synced)))

@bot.event
async def on_guild_join(guild):
    # Get the guild's ID
    guild_id = guild.id
    print(f"Joined guild with ID: {guild_id}")
    print(type(guild.id))
    print(type(allowed_server))

    if guild.id != allowed_server:
        await guild.leave()
        print(f"Bot removed from unauthorized server: {guild.name}")
    else:
        print(f"Bot joined authorized server: {guild.name}")

# define the "hello" command
@bot.tree.command(name='hello', description='say hello')
async def hello(interaction: discord.Interaction):
    # send a message to the user who entered the command
    await interaction.response.send_message(content='Hello!')
    
@bot.command(name='roll')
async def roll(ctx, max_roll: str = '100'):
    """
    Rolls a random number between 1 and a maximum number (default 100)
    Usage: !roll [max_roll]
    """
    try:
        max_roll = int(max_roll)
    except ValueError:
        await ctx.send("The maximum roll value must be an integer.")
        return

    if max_roll < 1:
        await ctx.send("The maximum roll value must be greater than or equal to 1.")
    elif max_roll > 99999:
        await ctx.send("The maximum roll value cannot exceed 99999.")
    else:
        roll_number = random.randint(1, max_roll)
        await ctx.send(f"{ctx.author.mention} rolled a {roll_number} out of {max_roll}!")

@bot.command(name='rules')
async def rules(ctx):
    """
    Displays the rules for the server.
    """
    embed = Embed(title='Server Rules')
    embed.add_field(name='Rule #1', value='Always follow [Discord\'s official Terms of Service](https://discord.com/terms)', inline = False)
    embed.add_field(name='Rule #2', value='Be respectful to other users; any form of discrimination will not be tolerated. This includes any conversation dealing with politics or religion - it will not be tolerated.', inline = False)
    embed.add_field(name='Rule #3', value='Initiating in fights/controversial discussion will not be tolerated.', inline = False)
    embed.add_field(name='Rule #4', value='Do not send harmful material such as viruses, IP-grabbers, or harm-ware.', inline = False)
    embed.add_field(name='Rule #5', value='Advertising of other servers/websites will not be tolerated.', inline = False)
    embed.add_field(name='Rule #6', value='Use common sense. If you think it\'s going to get you in trouble, odds are it will.', inline = False)
    embed.add_field(name='Rule #7', value='English only in text channels. You may speak in other languages in <#1030510653003276318>.', inline = False)
    embed.add_field(name='Rule #8', value='Impersonating other users will not be tolerated.', inline = False)
    embed.set_footer(text='Thanks for following the rules!')

    await ctx.send(embed=embed)

# Start the bot
print(TamoSecrets.get_server())
bot.run(TamoSecrets.get_token())
