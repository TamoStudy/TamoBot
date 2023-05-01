import discord
import datetime
from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger
from tools.constants import Constants

MONTHS = [
    "MissingNo",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

COLOR_ROLE_LIST = [
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

class ShopColor():
    def __init__(self, db: MySQLConnection):
        self.db = db
        TamoLogger.loga("INFO", "shop_color.__init__(db)", f"db successfully initialized in shop_color: {db}")

    def show_color_shop(self, interaction: discord.Interaction):
        """
        Generates the embed for the shop.
        """
        current_month = datetime.datetime.utcnow().month
        month = MONTHS[current_month]

        embed = discord.Embed(title=f'Change your name color!', color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=f':calendar_spiral: {month} Name Colors', value='**━━━━━━━━━━━━━━━**\n` 1` → <@&1097320653218123817>\n` 2` → <@&1097320665536802957>\n` 3` → <@&1097320668959342713>\n` 4` → <@&1097320671555637353>\n' +
                        '` 5` → <@&1097320674202230794>\n` 6` → <@&1097320679323480064>\n` 7` → <@&1097320683597484034>\n` 8` → <@&1097320689301733377>\n' +
                        '` 9` → <@&1097320692661358612>\n`10` → <@&1097320700655718491>\n`11` → <@&1097320754351181825>\n`12` → <@&1097320757798916167>\n' +
                        '`13` → <@&1097320760260968578>\n`14` → <@&1097320762743996527>\n`15` → <@&1097320765239603321>\n`16` → <@&1097320771392639086>\n**━━━━━━━━━━━━━━━**', inline=False)
        embed.add_field(name='\u200b', value='To purchase a color, use the `/shopcolor [#]` command.\n<:myemote:1097295903506829342> Purchasing a color role costs 500 <:customEmote:1096777370318413954> Tamo tokens.\n<:myemote:1097295903506829342> Color roles reset every month.', inline=False)
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)
        return embed

    async def purchase_color(self, member: discord.Member, guild: discord.Guild, choice: int):
        """
        Purchases a specified color and generates embed of purchase
        """
        user_id = member.id

        # Fetch user's tamo tokens.
        self.db.create_user_requirements_if_dne(user_id)
        tokens = int(self.db.fetch_tokens_by_id(user_id))

        # Check if they can purchase a color role.
        if not tokens >= 500:
            embed = discord.Embed(title=f'You do not have enough Tamo tokens!', color=0xff3a40)
            embed.set_thumbnail(url='https://github.com/narlock/Kaizen/blob/main/KaizenClient/assets/INFO_ERROR_ORANGE.png?raw=true')
            embed.add_field(name='\u200b', value=f'It costs `500` <:customEmote:1096777370318413954> Tamo tokens to perform this operation.\n<:myemote:1097295903506829342> You currently own `{tokens}` Tamo tokens.', inline=False)
            embed.add_field(name='\u200b', value=f'You can earn <:customEmote:1096777370318413954> Tamo tokens by spending focus time\nin a dedicated focus room!\n<:myemote:1097295903506829342> To check your amount of Tamo tokens, use `/stats`.', inline=False)
            embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)
            
            return embed
        
        # Update user's tamo tokens to subtract 500
        self.db.update_subtract_user_tokens(user_id, 500)
        tokens -= 500

        # Update the user's color role. Ensure that they do not have other color roles.
        color_roles = [
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[0]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[1]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[2]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[3]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[4]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[5]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[6]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[7]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[8]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[9]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[10]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[11]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[12]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[13]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[14]),
            discord.utils.get(guild.roles, id=COLOR_ROLE_LIST[15])
        ]

        # Get the color role based on choice and ensure the user only has that role
        color_role = color_roles[choice - 1]
        for role in member.roles:
            if role in color_roles and role != color_role:
                await member.remove_roles(role)
        await member.add_roles(color_role)

        # Return successful embed
        embed = discord.Embed(title=f'Successful Role Purchase', color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name='\u200b', value=f'You have successfully updated your role color to\n<@&{COLOR_ROLE_LIST[choice - 1]}>!.\n<:myemote:1097295903506829342> Your now have `{tokens}` <:customEmote:1096777370318413954> Tamo tokens.')
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)

        return embed