import discord
import random
from discord import Embed
from discord.ext import commands
from discord import app_commands
from tamo_secrets import TamoSecrets
from eight_ball import EightBall

# set up the bot client with intents
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
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
    await bot.change_presence(activity=discord.Game(name="/help | tamostudy.com"))

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
    
@bot.tree.command(name='roll', description='Rolls a random number between 1 and a max number (default 100)')
async def roll(interaction: discord.Interaction, max_roll: str = '100'):
    """
    Rolls a random number between 1 and a maximum number (default 100)
    Usage: !roll [max_roll]
    """
    footer_message = None
    roll_message = 'Unexpected error occurred during /roll command.'
    try:
        max_roll = int(max_roll)
    except ValueError:
        roll_message = 'The maximum roll value must be an integer.'
        footer_message = 'Use the /roll command to try again.'
        return

    if max_roll < 1:
        roll_message = 'The maximum roll value must be greater than or equal to 1.'
        footer_message = 'Use the /roll command to try again.'
    elif max_roll > 99999:
        roll_message = 'The maximum roll value cannot exceed 99999.'
        footer_message = 'Use the /roll command to try again.'
    else:
        roll_number = random.randint(1, max_roll)
        roll_message = f"{interaction.user.name} rolled a {roll_number} out of {max_roll}!"

    embed = discord.Embed(title=f'{roll_message}', color=0xffa500)
    embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
    if footer_message is not None:
        embed.add_field(name='\u200b', value=footer_message)
    embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='8ball', description='Magic 8 ball')
async def eightball(interaction: discord.Interaction, question: str):
    response = EightBall.get_response()
    await interaction.response.send_message(f'**Question**: {question}\n**Answer**: {response}')

@bot.tree.command(name='rules', description='Displays the rules for the server.')
async def rules(interaction: discord.Interaction):
    """
    Displays the rules for the server.
    """
    rules_channel = bot.get_channel(821757961830793239)

    embed = discord.Embed(title='Server Rules', color=0xff3a40)
    embed.set_thumbnail(url='https://github.com/narlock/Kaizen/blob/main/KaizenClient/assets/INFO_ERROR_ORANGE.png?raw=true')
    embed.add_field(name='\u200b', value='**1** → Always follow [Discord\'s official Terms of Service](https://discord.com/terms)', inline = False)
    embed.add_field(name='\u200b', value='**2** → Be respectful to other users; any form of discrimination will not be tolerated.', inline = False)
    embed.add_field(name='\u200b', value='**3** → Initiating in fights/controversial discussion will not be tolerated.', inline = False)
    embed.add_field(name='\u200b', value='**4** → Do not send harmful material such as viruses, IP-grabbers, or harm-ware.', inline = False)
    embed.add_field(name='\u200b', value='**5** → Advertising of other servers/websites will not be tolerated.', inline = False)
    embed.add_field(name='\u200b', value='**6** → Use common sense. If you think it\'s going to get you in trouble, odds are it will.', inline = False)
    embed.add_field(name='\u200b', value='**7** → English only in text channels. You may speak in other languages in <#1030510653003276318>.', inline = False)
    embed.add_field(name='\u200b', value='**8** → Impersonating other users will not be tolerated.', inline = False)
    embed.add_field(name='\u200b', value=f'**Refer to {rules_channel.mention} for more information**.', inline = False)

    await interaction.response.send_message(embed=embed)


# Start the bot
print(TamoSecrets.get_server())
bot.run(TamoSecrets.get_token())
