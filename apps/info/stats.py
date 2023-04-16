import discord
import math

from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger

class Stats():
    def __init__(self, db: MySQLConnection):
        self.db = db
        TamoLogger.log("INFO", f"db successfully initialized in stats: {db}")

    def show_statistics(self, interaction: discord.Interaction, user: discord.User = None):
        """
        Create embed for discord user statistics
        """

        if user is None:
            # Interaction member is caller
            calling_user = interaction.user
            self.db.create_user_if_dne(calling_user.id)
            stats_user = self.db.fetch_simple_stats_profile_by_id(calling_user.id)
        else:
            # Provided user is caller
            calling_user = user
            self.db.create_user_if_dne(calling_user.id)
            stats_user = self.db.fetch_simple_stats_profile_by_id(calling_user.id)

        TamoLogger.log("INFO", f"Received stats_user = {stats_user}")
        daily_stime = math.floor(stats_user[0] / 3600)
        month_stime = math.floor(stats_user[1] / 3600)
        user_stime = math.floor(stats_user[2] / 3600)
        user_tokens = stats_user[3]
        user_trivia = stats_user[4]

        # Fetch the caller's hex code
        hex_string = self.db.fetch_hex_code_by_id(calling_user.id)
        hex_integer = int(hex_string, 16)

        red = (hex_integer >> 16) & 0xff
        green = (hex_integer >> 8) & 0xff
        blue = hex_integer & 0xff

        color = discord.Colour.from_rgb(red, green, blue)

        embed = discord.Embed(title=f'TamoBot Statistics for {calling_user.name}', color=color)
        embed.set_thumbnail(url=f'{calling_user.avatar.url}')
        embed.add_field(name='General', value=f':hourglass: **Today\'s Focus:** {daily_stime} hrs\n:calendar: **Month Focus:** {month_stime} hrs\n:star: **Total Focus:** {user_stime} hrs\n<:customEmote:1096777370318413954> **Tamo Tokens:** {user_tokens}', inline = False)
        embed.add_field(name='Arcade', value=f':question: **Trivia Questions Answered:** {user_trivia}')
        """
        TODO
        Under the condition that the user has a special title in 'feat',
        add this as a new field to the stats.
        """
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed