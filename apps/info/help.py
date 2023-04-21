import discord
from discord.ext import commands
from tools.constants import Constants

class Help:
    @staticmethod
    def get_help_embed():
        """
        Returns the help discord embed
        """
        embed = discord.Embed(title="TamoBot Help", color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=':gear: General', value='**━━━━━━━━━━━━━━━**\n`/help`\n<:myemote:1097295903506829342> Get help! Oh wait, you\'re on this page right now.\n`/rules`\n<:myemote:1097295903506829342> View the server rules.\n`/roll [optional: max]`\n<:myemote:1097295903506829342>Randomly roll a number.\n`/8ball [question]`\n<:myemote:1097295903506829342> Ask the magic 8 ball a question.\n`/motivation [optional: user]`\n<:myemote:1097295903506829342> Get some motivation!\n**━━━━━━━━━━━━━━━**', inline=False)
        embed.add_field(name=':busts_in_silhouette: Profile & Time Tracking', value='**━━━━━━━━━━━━━━━**\n`/stats`\n<:myemote:1097295903506829342>View your TamoBot statistics.\n`/top`\n<:myemote:1097295903506829342>View the server focus leaderboard.\n**━━━━━━━━━━━━━━━**', inline=False)
        embed.add_field(name=':shopping_bags: Shop', value='**━━━━━━━━━━━━━━━**\n`/shopembed [hex]` (1000 <:customEmote:1096777370318413954> Tamo tokens)\n<:myemote:1097295903506829342> Customize profile embed color.\n`/shopcolor [#]` (500 <:customEmote:1096777370318413954> Tamo tokens)\n<:myemote:1097295903506829342> Customize your server name color, resets monthly.\n**━━━━━━━━━━━━━━━**', inline=False)
        embed.add_field(name=':joystick: Arcade', value='**━━━━━━━━━━━━━━━**\n`/trivia` (25 <:customEmote:1096777370318413954> Tamo tokens)\n<:myemote:1097295903506829342> Answer fun and simple trivia questions.\n**━━━━━━━━━━━━━━━**', inline=False)
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)
        return embed