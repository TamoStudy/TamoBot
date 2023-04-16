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
            embed = discord.Embed(title=f'You do not have enough Tamo tokens!', color=0xffa500)
            embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
            embed.add_field(name='\u200b', value=f'It costs 1000 Tamo tokens to perform this operation.\nYou currently own {tokens} Tamo tokens.')
            embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
            
            return embed

        # Update user's tamo tokens to subtract 1000.
        self.db.update_subtract_user_tokens(user_id, tokens)

        # Return successful embed.

        # Fetch the caller's hex code
        hex_string = self.db.fetch_hex_code_by_id(user_id)
        hex_integer = int(hex_string, 16)

        red = (hex_integer >> 16) & 0xff
        green = (hex_integer >> 8) & 0xff
        blue = hex_integer & 0xff

        color = discord.Colour.from_rgb(red, green, blue)

        embed = discord.Embed(title=f'Purchase successful!', color=color)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name='\u200b', value=f'Congrats. You have successfully updated your embed color to {hex}.\nPreview is on this embed!')
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed
            