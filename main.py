"""
TamoBot - main.py
by: narlock

The main runner of the TamoBot.
Contains standard pattern for Discord Bot creation utilizing discord.py
"""
# Required imports
import discord
import re

from tools.tamolog import TamoLogger
from tools.errorembed import ErrorEmbed

from sql.mysqlconnection import MySQLConnection
from discord.ext import commands
from tamo_secrets import TamoSecrets

# TamoBot Applications
from apps.time.time_track import TimeTrack
from tools.roleassign import RoleAssign
from apps.time.top import Top

from apps.shop.shop import Shop
from apps.shop.shopembed import ShopEmbed
from apps.shop.shopcolor import ShopColor

from apps.misc.eight_ball import EightBall
from apps.misc.roll import Roll
from apps.misc.motivation import Motivation

from apps.info.help import Help
from apps.info.rules import Rules
from apps.info.stats import Stats

from apps.arcade.arcade import Arcade

# Initialize TamoBot and related connections
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
allowed_server = int(TamoSecrets.get_server())
db = MySQLConnection(TamoSecrets.get_db_database())
TamoLogger.loga("INFO", "main", f"db successfully initialized in main: {db}")

time_tracker = TimeTrack(db)
role_assign = RoleAssign(db)
stats_caller = Stats(db)
top_app = Top(db)
shopembed_app = ShopEmbed(db)
shopcolor_app = ShopColor(db)

@bot.event
async def on_ready():
    """
    The on_ready event will trigger when the bot starts up

    1. Connects to the Tamo database.
    2. Ensures that the TamoBot is only connected to allowed servers.
    3. Sets the status of the TamoBot.
    4. Syncs the slash commands.
    """

    # Connect to mySQL database
    db.connect()

    # bot is only allowed on allowed servers
    TamoLogger.loga("SUCCESS", "main.on_ready", f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        if guild.id != allowed_server:
            TamoLogger.loga("WARN", "main.on_ready", f'{bot.user} leaving unauthorized server {guild.name} (id: {guild.id})')
            await guild.leave()
        else:
            TamoLogger.loga("INFO", "main.on_ready", f'{bot.user} is connected to {guild.name} (id: {guild.id})')
            time_tracker.start_up(guild)

    # Set status message
    await bot.change_presence(activity=discord.Game(name="/help | tamostudy.com"))

    # Sync commands
    synced = await bot.tree.sync()
    TamoLogger.loga('INFO', "main.on_ready", 'TamoBot Slash Commands Synced: ' + str(len(synced)))

    # Indicate on_ready is complete
    TamoLogger.loga('SUCCESS', "main.on_ready", 'TamoBot is officially ready for use!')

@bot.event
async def on_guild_join(guild):
    """
    The on_guild_join functionality is used to ensure that the TamoBot
    only joins servers that is has been assigned to join.

    The TamoBot will leave servers that it has not been assigned to join.
    """
    guild_id = guild.id
    TamoLogger.loga("INFO", "main.on_guild_join", f"Joined guild with ID: {guild_id}")

    if guild.id != allowed_server:
        await guild.leave()
        TamoLogger.loga("WARN", "main.on_guild_join", f"Bot removed from unauthorized server: {guild.name}")
    else:
        TamoLogger.loga("INFO", "main.on_guild_join", f"Bot joined authorized server: {guild.name}")

@bot.command(name='shutdown')
async def shutdown(ctx: commands.Context):
    """
    $shutdown

    A traditional context command for administrator use only.
    This will shut the bot down at any given time.
    This command acts as a 'safe' shut down.
    """
    TamoLogger.loga("INFO", "main.shutdown", f"Received shutdown command from {ctx.author.name}")
    guild = ctx.guild
    user_has_role = discord.utils.get(ctx.author.roles, id=934885581614350348) is not None
    if user_has_role:
        time_tracker.handle_shutdown(guild)
        await ctx.send("Shutting down...")
        await bot.close()
        TamoLogger.loga("SUCCESS", "main.shutdown", f"TamoBot Close Successful")
    else:
        await ctx.send("LOL! :rofl:")
        TamoLogger.loga("WARN", "main.shutdown", f"Shutdown attempt failure. User has inproper permissions.")

##########################################
##########################################
##########################################
# Timer Events and Commands
##########################################
##########################################
##########################################

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    """
    on_voice_state_update

    TamoBot will first update time tracking for the member based off of received voice states. (via TimeTracker)
    Then, TamoBot will assign level roles according to the user's current month time. (via RoleAssign)
    """
    # try:
    TamoLogger.loga("INFO", "main.on_voice_state_update", f"Attempting to get member and guild from incoming interaction {member}")
    guild = member.guild

    TamoLogger.log("INFO", f"Voice State Update received by {member.name} in guild {guild.name}")
    time_tracker.update_time_on_event(member, before, after)
    await role_assign.check_role_updates_on_user(member, guild)
    # except Exception as e:
    #     TamoLogger.loga("ERROR", "main.on_voice_state_update", f"Error obtaining member and guild from incoming interaction. {e}")

@bot.tree.command(name='stats', description='Displays the statistics of a user')
async def stats(interaction: discord.Interaction, member: discord.Member = None):
    """
    /stats [user]

    Displays the TamoBot statistics of the specified user. If no user is
    provided, the calling user is set as the user.
    """
    try:

        TamoLogger.loga("INFO", "main.stats", f"Attempting to get member and guild from incoming interaction")
        if member is None:
            member = interaction.guild.get_member(interaction.user.id)

        time_tracker.update_time_on_call(interaction, member)
        guild = interaction.guild

        await role_assign.check_role_updates_on_user(member, guild)

        embed = stats_caller.show_statistics(interaction, member)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        TamoLogger.loga("ERROR", "main.stats", f"Error obtaining member and guild from incoming interaction. {e}")
        await interaction.response.send_message(embed=ErrorEmbed.message("Unexpected error occurred."))

@bot.tree.command(name='top', description='View the current all time focus leaders')
async def top(interaction: discord.Interaction):
    """
    /top

    Displays the top three focus leaders on the server.
    """
    embed = top_app.display_top(interaction)
    await interaction.response.send_message(embed=embed)

##########################################
##########################################
##########################################
# Shop Commands
##########################################
##########################################
##########################################

"""
/shop

Displays the current server shop options.
"""
@bot.tree.command(name='shop', description='View the shop listings.')
async def shop(interaction: discord.Interaction):
    embed = Shop.show_shop_options()
    await interaction.response.send_message(embed=embed)

"""
/shopembed [hex]

User calls the command to purchase the embed to add to their profile
"""
@bot.tree.command(name='shopembed', description='Use 1000 Tamo tokens to change the color of your profile embed.')
async def shop(interaction: discord.Interaction, hex: str = None):
    if hex and re.match(r'^[0-9a-fA-F]{6}$', hex):
        embed = shopembed_app.purchase_embed(interaction.user.id, hex)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"{interaction.user.mention}, please provide a correct hex code. Example: `FFFFFF` (white).")
    
"""
/shopcolor          : displays shop color options
/shopcolor [option] : purchase color option
"""
@bot.tree.command(name='shopcolor', description='Use 500 Tamo tokens to change the color of your discord name!')
async def shopcolor(interaction: discord.Interaction, color: str = None):
    if str is None:
        embed = shopcolor_app.show_color_shop(interaction)
        await interaction.response.send_message(embed=embed)
    else:
        try:
            purchase_number = int(color)
            if 1 <= purchase_number <= 16:
                raise Exception('Invalid entry')
            embed = shopcolor_app.purchase_color(interaction, purchase_number)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            embed = ErrorEmbed.message('Invalid color option was entered.\nEnter an integer between `1` and `16`.')
            await interaction.response.send_message(embed=embed)
    

##########################################
##########################################
##########################################
# Misc Commands
##########################################
##########################################
##########################################

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

##########################################
##########################################
##########################################
# Info Commands
##########################################
##########################################
##########################################

"""
/help

Displays the commands of the server.
- Utilizes /apps/info/help.py for embed integration
"""
@bot.tree.command(name='help', description='Information on how to use TamoBot')
async def help(interaction: discord.Interaction):
    embed = Help.get_help_embed()
    await interaction.response.send_message(embed=embed)

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

##########################################
##########################################
##########################################
# Arcade Commands
##########################################
##########################################
##########################################

"""
/arcade

Displays the game options in the arcade.
"""
@bot.tree.command(name='arcade', description='Displays the game options in the arcade.')
async def arcade(interaction: discord.Interaction):
    embed = Arcade.show_arcade_options()
    await interaction.response.send_message(embed=embed)

"""
/trivia

Answer fun trivia questions (100 Tamo tokens)
"""
@bot.tree.command(name='trivia', description='Answer fun trivia questions (100 Tamo tokens)')
async def trivia(interaction: discord.Interaction):
    await interaction.response.send_message("This feature is currently in development")

# Starts the TamoBot
bot.run(TamoSecrets.get_token())
