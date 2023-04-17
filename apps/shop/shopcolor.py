import discord
from sql.mysqlconnection import MySQLConnection
from tools.tamolog import TamoLogger

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
        embed = discord.Embed(title=f'Change your name color!', color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        return embed

    def purchase_color(self, interaction: discord.Interaction, choice: int):
        """
        Purchases a specified color and generates embed of purchase
        """
        embed = discord.Embed(title=f'You have purchased <>!', color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        return embed