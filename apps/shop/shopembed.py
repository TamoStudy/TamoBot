import discord

from tools.tamolog import TamoLogger
from sql.mysqlconnection import MySQLConnection

class ShopEmbed():
    def __init__(self, db: MySQLConnection):
        self.db = db
        TamoLogger.loga("INFO", "ShopEmbed.__init__(db)", f"db successfully initialized in time_track: {db}")

    def purchase_embed(self, user_id, hex):
        # Fetch user's tamo tokens.
        self.db.create_user_requirements_if_dne(user_id)
        tokens = int(self.db.fetch_tokens_by_id(user_id))

        # Update user's hex if they have enough Tamo tokens.
        if not tokens >= 1000:
            embed = discord.Embed(title=f'You do not have enough Tamo tokens!', color=0xff3a40)
            embed.set_thumbnail(url='https://github.com/narlock/Kaizen/blob/main/KaizenClient/assets/INFO_ERROR_ORANGE.png?raw=true')
            embed.add_field(name='\u200b', value=f'It costs `1000` <:customEmote:1096777370318413954> Tamo tokens to perform this operation.\n<:myemote:1097295903506829342> You currently own `{tokens}` Tamo tokens.', inline=False)
            embed.add_field(name='\u200b', value=f'You can earn <:customEmote:1096777370318413954> Tamo tokens by spending focus time\nin a dedicated focus room!\n<:myemote:1097295903506829342> To check your amount of Tamo tokens, use `/stats`.', inline=False)
            embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
            
            return embed

        # Update user's tamo tokens to subtract 1000.
        self.db.update_subtract_user_tokens(user_id, 1000)
        tokens -= 1000

        # Return successful embed.
        self.db.update_user_hex(user_id, hex)

        # Fetch the caller's hex code
        hex_string = self.db.fetch_hex_code_by_id(user_id)
        hex_integer = int(hex_string, 16)

        red = (hex_integer >> 16) & 0xff
        green = (hex_integer >> 8) & 0xff
        blue = hex_integer & 0xff

        color = discord.Colour.from_rgb(red, green, blue)

        embed = discord.Embed(title=f'Purchase successful!', color=color)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name='\u200b', value=f'You have successfully updated your embed color to `{hex}`.\n<:myemote:1097295903506829342> A preview of your color is on this embed.\n<:myemote:1097295903506829342> Your now have `{tokens}` <:customEmote:1096777370318413954> Tamo tokens.')
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed
            