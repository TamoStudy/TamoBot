import discord

from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger

class Top():
    def __init__(self, db: MySQLConnection):
        self.db = db
        TamoLogger.loga("INFO", "top.__init__(db)", f"db successfully initialized in top: {db}")

    def display_top(self, interaction: discord.Interaction) -> discord.Embed:
        """
        Generates the embed for the top users on the server, sends error embed if error occurs.

        Args:
            interaction (discord.Interaction)
        
        Returns:
            embed (discord.Embed)
        """
        TamoLogger.loga("INFO", "top.display_top", f"Generating top embed. Requested by {interaction.user.name}")
        
        try:
            user_list = self.db.fetch_top_3_stime_monthly_users()
        except Exception as e:
            TamoLogger.loga("ERROR", "top.display_top", f"user_list creation failure on db.fetch_top_3_stime_monthly_users. {e}")
            return

        embed = discord.Embed(title='TamoBot Focus Leaderboard', color=0xffa500)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
        embed.add_field(name=':first_place:', value='narlock (120 hrs)', inline=False)
        embed.add_field(name=':second_place:', value='beside bella (102 hrs)', inline=False)
        embed.add_field(name=':third_place:', value='Melody (100 hrs)', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed