"""
TamoBot - main.py
by: narlock

The main runner of the TamoBot.
Contains standard pattern for Discord Bot creation utilizing discord.py
"""
# Required imports
import discord
from sql.mysqlconnection import MySQLConnection
from discord.ext import commands

# For tabs
import asyncio
from typing import Union

# Load TamoBot secrets
from tamo_secrets import TamoSecrets

# TamoBot Applications
from apps.time.time_track import TimeTrack
from apps.time.top import Top

from apps.misc.eight_ball import EightBall
from apps.misc.roll import Roll
from apps.misc.motivation import Motivation

from apps.info.rules import Rules
from apps.info.stats import Stats

# Initialize TamoBot and related connections
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
allowed_server = int(TamoSecrets.get_server())
db = MySQLConnection()

"""
The on_ready event will trigger when the bot starts up

1. Connects to the Tamo database.
2. Ensures that the TamoBot is only connected to allowed servers.
3. Sets the status of the TamoBot.
4. Syncs the slash commands.
"""
@bot.event
async def on_ready():
    # Connect to mySQL database
    db.connect()

    # bot is only allowed on allowed servers
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        if guild.id != allowed_server:
            await guild.leave()
        else:
            print(f'- {guild.name} (id: {guild.id})')

    # Set status message
    await bot.change_presence(activity=discord.Game(name="/help | tamostudy.com"))

    # Sync commands
    synced = await bot.tree.sync()
    print('TamoBot Slash CMDS Synced: ' + str(len(synced)))

    # Indicate on_ready is complete
    print('On ready is complete!')

"""
The on_guild_join functionality is used to ensure that the TamoBot
only joins servers that is has been assigned to join.

The TamoBot will leave servers that it has not been assigned to join.
"""
@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    print(f"Joined guild with ID: {guild_id}")
    print(type(guild.id))
    print(type(allowed_server))

    if guild.id != allowed_server:
        await guild.leave()
        print(f"Bot removed from unauthorized server: {guild.name}")
    else:
        print(f"Bot joined authorized server: {guild.name}")

# Timer Event

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    TimeTrack.update_time_on_event(member, before, after)

@bot.tree.command(name='stats', description='Displays the statistics of a user')
async def stats(interaction: discord.Interaction, user: discord.User = None):
    # TimeTrack.update_time_on_call(interaction, user)
    embed = Stats.show_statistics(interaction, user)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='top', description='View the current all time focus leaders')
async def top(interaction: discord.Interaction):
    # Get top users from database, user1=, user2= ...
    user1 = bot.fetch_user(481296666377453588)
    embed = Top.display_top(interaction, user1)
    await interaction.response.send_message(embed=embed)
    
# Misc Commands

"""
/roll [max_roll]

Rolls a random number between 1 and a maximum number (default 100)
- Utilizes /apps/misc/roll.py for logic and embed.
"""
@bot.tree.command(name='roll', description='Rolls a random number between 1 and a max number (default 100)')
async def roll(interaction: discord.Interaction, max_roll: str = '100'):
    embed = Roll.perform_action(interaction, max_roll)
    await interaction.response.send_message(embed=embed)

"""
/8ball [Question]

User can ask a question and receive a random response, similar to a magic 8-ball.
- Utilizes /apps/misc/8ball.py to create embed and perform action.
"""
@bot.tree.command(name='8ball', description='Magic 8 ball')
async def eightball(interaction: discord.Interaction, question: str):
    response = EightBall.get_response()
    await interaction.response.send_message(f'**Question**: {question}\n**Answer**: {response}')

"""
/motivation

User requests motivation from TamoBot, TamoBot responds with giving
the user a motivational message.
- Utilizes /apps/misc/motivation.py to create a message for the user.
"""
@bot.tree.command(name='motivation', description='Get some motivation!')
async def motivation(interaction: discord.Interaction, user: discord.User = None):
    response = Motivation.get_motivation_embed(interaction, user)
    await interaction.response.send_message(response)

# Info Commands

"""
/help

Displays the commands of the server.
- Utilizes /apps/info/help.py for embed integration
"""
@bot.tree.command(name='help', description='Information on how to use TamoBot')
async def help(interaction: discord.Interaction):
    pass

"""
/rules

Displays the rules for the server.
- Utilizes /apps/info/rules.py to create embed for rules.
"""
@bot.tree.command(name='rules', description='Displays the rules for the server.')
async def rules(interaction: discord.Interaction):
    rules_channel = bot.get_channel(821757961830793239)
    embed = Rules.get_rules_embed(rules_channel)
    await interaction.response.send_message(embed=embed)

# Starts the TamoBot
bot.run(TamoSecrets.get_token())
