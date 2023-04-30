import discord

from discord.ext import commands
from tools.tamolog import TamoLogger

ROLE_IDS = {
    821757961830793236: [
        1093186890393469008,
        1093186982257115177,
        1093187032718770279,
        1093187089371246663,
        1093187142848618576,
        1093187217544982540,
        1097320653218123817,
        1097320665536802957,
        1097320668959342713,
        1097320671555637353,
        1097320674202230794,
        1097320679323480064,
        1097320683597484034,
        1097320689301733377,
        1097320692661358612,
        1097320700655718491,
        1097320754351181825,
        1097320757798916167,
        1097320760260968578,
        1097320762743996527,
        1097320765239603321,
        1097320771392639086
     ]
}


class ResetMonth():
    @staticmethod
    async def reset_month_and_color_roles(ctx: commands.Context):
        """
        reset_month_and_color_roles
        """
        guild = ctx.guild

        if guild.id not in ROLE_IDS:
            TamoLogger.loga("WARN", "ResetMonth.reset_month_and_color_roles", f"Called guild {guild.id} does not exist in ROLE_IDS. Skipping update roles.")
            return
        
        for role_id in ROLE_IDS[guild.id]:
            role = discord.utils.get(ctx.guild.roles, name=role_id) # get the role object
            if not role:
                TamoLogger.loga("WARN", "ResetMonth.reset_month_and_color_roles", f"Role {role_id} not found.")
                return

            for member in ctx.guild.members:
                if role in member.roles:
                    TamoLogger.loga("INFO", "ResetMonth.reset_month_and_color_roles", f"Removing {role.name} from {member.name}")
                    await member.remove_roles(role)

        TamoLogger.loga("INFO", "ResetMonth.reset_month_and_color_roles", f"Resetting Month Completed.")