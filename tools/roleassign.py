import discord
import datetime

from tools.tamolog import TamoLogger
from sql.mysqlconnection import MySQLConnection

ROLE_IDS = {
    821757961830793236, (
        1093186890393469008,
        1093186982257115177,
        1093187032718770279,
        1093187089371246663,
        1093187142848618576,
        1093187217544982540
    )
}
    
class RoleAssign():
    def __init__(self, db: MySQLConnection):
        self.db = db

    async def check_role_updates_on_user(self, member: discord.Member, guild: discord.Guild = None):
        if guild.id not in ROLE_IDS:
            TamoLogger.log("WARN", f"Called guild {guild.id} does not exist in ROLE_IDS. Skipping update roles.")
            return

        # Get Level Roles for Server
        level_one_role = discord.utils.get(guild.roles, id=1093186890393469008)
        level_two_role = discord.utils.get(guild.roles, id=1093186982257115177)
        level_three_role = discord.utils.get(guild.roles, id=1093187032718770279)
        level_four_role = discord.utils.get(guild.roles, id=1093187089371246663)
        level_five_role = discord.utils.get(guild.roles, id=1093187142848618576)
        level_six_role = discord.utils.get(guild.roles, id=1093187217544982540)

        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year
        month_time = (self.db.fetch_month_time_of_user(member.id, current_month, current_year)) // 3600

        if month_time < 3:
            # Remove all Level Roles
            await member.remove_roles(level_one_role, level_two_role, level_three_role, level_four_role, level_five_role, level_six_role)
            TamoLogger.log("INFO", f"Ensuring {member.name} does not have a level role.")
        elif month_time >= 3 and month_time < 10:
            # Assign Level 1 Role, unless user already has it, deassign other roles
            if level_one_role not in member.roles:
                await member.add_roles(level_one_role)
                await member.remove_roles(level_two_role, level_three_role, level_four_role, level_five_role, level_six_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level one role.")
        elif month_time >= 10 and month_time < 25:
            # Assign Level 2 Role, unless user already has it, deassign other roles
            if level_two_role not in member.roles:
                await member.add_roles(level_two_role)
                await member.remove_roles(level_one_role, level_three_role, level_four_role, level_five_role, level_six_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level two role.")
        elif month_time >= 25 and month_time < 60:
            # Assign Level 3 Role, unless user already has it, deassign other roles
            if level_three_role not in member.roles:
                await member.add_roles(level_three_role)
                await member.remove_roles(level_one_role, level_two_role, level_four_role, level_five_role, level_six_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level three role.")
        elif month_time >= 60 and month_time < 100:
            # Assign Level 4 Role, unless user already has it, deassign other roles
            if level_four_role not in member.roles:
                await member.add_roles(level_four_role)
                await member.remove_roles(level_one_role, level_two_role, level_three_role, level_five_role, level_six_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level four role.")
        elif month_time >= 100 and month_time < 250:
            # Assign Level 5 Role, unless user already has it, deassign other roles
            if level_five_role not in member.roles:
                await member.add_roles(level_five_role)
                await member.remove_roles(level_one_role, level_two_role, level_three_role, level_four_role, level_six_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level five role.")
        elif month_time >= 250:
            # Assign Level 6 Role, unless user already has it, deassign other roles
            if level_six_role not in member.roles:
                await member.add_roles(level_six_role)
                await member.remove_roles(level_one_role, level_two_role, level_three_role, level_four_role, level_five_role)
                TamoLogger.log("INFO", f"Assigning {member.name} level six role.")

