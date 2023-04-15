import discord
from discord.ext import commands

class Help:
    @staticmethod
    def get_help_embed(interaction: discord.Interaction):
        """
        Returns the help discord embed
        """
        embed = discord.Embed(title="TamoBot Help")
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=':gear: General', value='`/help` - Get help! Oh wait, you\'re on this page right now.\n`/rules` - View the server rules.\n`/roll` - Randomly roll a number.\n`/8ball [q]` - Ask the magic 8 ball a question.\n`/motivation` - Get some motivation!', inline=False)
        embed.add_field(name=':busts_in_silhouette: Profile & Time Tracking', value='`/stats` - View your TamoBot statistics.\n`/top` - View the server focus leaderboard.', inline=False)
        embed.add_field(name=':shopping_bags: Shop', value='`/shop embed [hex]` (1000 Tamo tokens) - Customize profile embed color.\n`/shop color [No.] - Customize your server name color.`', inline=False)
        embed.add_field(name=':joystick: Arcade', value='`/trivia` (100 Tamo tokens)', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
        return embed