import discord

from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger
from tools.errorembed import ErrorEmbed
from tools.constants import Constants

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
            user_list = self.db.fetch_top_10_stime_monthly_users()
        except Exception as e:
            TamoLogger.loga("ERROR", "top.display_top", f"user_list creation failure on db.fetch_top_3_stime_monthly_users. {e}")
            return ErrorEmbed.message("Unexpected error occurred.")

        member_one = interaction.guild.get_member(user_list[0][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 1 {member_one}")
        member_one_name = self.get_username(member_one)
        member_one_month_time = user_list[0][1] // 3600

        member_two = interaction.guild.get_member(user_list[1][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 2 {member_two}")
        member_two_name = self.get_username(member_two)
        member_two_month_time = user_list[1][1] // 3600

        member_thr = interaction.guild.get_member(user_list[2][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 3 {member_thr}")
        member_thr_name = self.get_username(member_thr)
        member_thr_month_time = user_list[2][1] // 3600

        member_fou = interaction.guild.get_member(user_list[3][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 4 {member_fou}")
        member_fou_name = self.get_username(member_fou)
        member_fou_month_time = user_list[3][1] // 3600

        member_fiv = interaction.guild.get_member(user_list[4][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 5 {member_fiv}")
        member_fiv_name = self.get_username(member_fiv)
        member_fiv_month_time = user_list[4][1] // 3600

        member_six = interaction.guild.get_member(user_list[5][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 6 {member_six}")
        member_six_name = self.get_username(member_six)
        member_six_month_time = user_list[5][1] // 3600

        member_sev = interaction.guild.get_member(user_list[6][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 7 {member_sev}")
        member_sev_name = self.get_username(member_sev)
        member_sev_month_time = user_list[6][1] // 3600

        member_eig = interaction.guild.get_member(user_list[7][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 8 {member_eig}")
        member_eig_name = self.get_username(member_eig)
        member_eig_month_time = user_list[7][1] // 3600

        member_nin = interaction.guild.get_member(user_list[8][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 9 {member_nin}")
        member_nin_name = self.get_username(member_nin)
        member_nin_month_time = user_list[8][1] // 3600

        member_ten = interaction.guild.get_member(user_list[9][0])
        TamoLogger.loga("INFO", "top.display_top" , f"Top Member 10 {member_ten}")
        member_ten_name = self.get_username(member_ten)
        member_ten_month_time = user_list[9][1] // 3600

        embed = discord.Embed(title='TamoBot Focus Leaderboard <:myemote:1094329395994439790>', color=0xffa500)
        embed.set_thumbnail(url=f'{member_one.avatar.url}')
        embed.add_field(name=':first_place: First', value=f'**{member_one_name}** ({member_one_month_time} hrs)', inline=False)
        embed.add_field(name=':second_place: Second', value=f'**{member_two_name}** ({member_two_month_time} hrs)', inline=False)
        embed.add_field(name=':third_place: Third', value=f'**{member_thr_name}** ({member_thr_month_time} hrs)\n\n**━━━━━━━━━━━━━━━**\n\u200b\n', inline=False)
        embed.add_field(name=':mega: Honorable Mentions', value=f'{member_fou_name} ({member_fou_month_time} hrs)\n{member_fiv_name} ({member_fiv_month_time} hrs)\n{member_six_name} ({member_six_month_time} hrs)\n{member_sev_name} ({member_sev_month_time} hrs)\n{member_eig_name} ({member_eig_month_time} hrs)\n{member_nin_name} ({member_nin_month_time} hrs)\n{member_ten_name} ({member_ten_month_time} hrs)\n')
        embed.add_field(name='\u200b', value=':small_blue_diamond: Leaderboard resets monthly relative to UTC.\n:small_blue_diamond: At the *end of the month*,\n<:myemote:1097295903506829342> :first_place: **First** gains 200 <:customEmote:1096777370318413954> & <@&849134842814005279> (1 mth)\n<:myemote:1097295903506829342> :second_place: **Second** gains 100 <:customEmote:1096777370318413954>\n<:myemote:1097295903506829342> :third_place: **Third** gains 50 <:customEmote:1096777370318413954>', inline=False)
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)

        return embed
    
    def display_top_trivia(self, interaction: discord.Interaction):
        TamoLogger.loga("INFO", "top.display_top_trivia", f"Generating top embed. Requested by {interaction.user.name}")
        
        try:
            user_list = self.db.fetch_top_3_trivia_users()
        except Exception as e:
            TamoLogger.loga("ERROR", "top.display_top_trivia", f"user_list creation failure on db.fetch_top_3_trivia_users. {e}")
            return ErrorEmbed.message("Unexpected error occurred.")
        
        member_one = interaction.guild.get_member(user_list[0][0])
        member_one_trivia = user_list[0][1]
        member_two = interaction.guild.get_member(user_list[1][0])
        member_two_trivia = user_list[1][1]
        member_thr = interaction.guild.get_member(user_list[2][0])
        member_thr_trivia = user_list[2][1]

        embed = discord.Embed(title='TamoBot Trivia Leaderboard <:myemote:1094329395994439790>', color=0xffa500)
        avatar_url = self.get_top_url(member_one)
        try:
            embed.set_thumbnail(url=f'{avatar_url}')
        except Exception as e:
            embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=':first_place: First', value=f'**{member_one.name}** ({member_one_trivia} correct answers)', inline=False)
        embed.add_field(name=':second_place: Second', value=f'**{member_two.name}** ({member_two_trivia} correct answers)', inline=False)
        embed.add_field(name=':third_place: Third', value=f'**{member_thr.name}** ({member_thr_trivia} correct answers)', inline=False)

        return embed
    
    def get_username(self, member: discord.Member):
        if member is None:
            # TODO Remove member from database
            return "TamoBot"
        else:
            return member.name
        
    def get_top_url(self, member: discord.Member):
        if member is None:
            # TODO Remove member from database
            return "https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png"
        else:
            return member.avatar.url