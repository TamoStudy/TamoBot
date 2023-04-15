import discord

class Shop():
    @staticmethod
    def show_shop_options():
        embed = discord.Embed(title="TamoBot Shop")
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=':dna: Profile Customization', value='`/shop embed [hex]` (1000 Tamo tokens) - Customize profile embed color.\n`/shop color [no.]` (500 Tamo tokens) - Customize your server name color.', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
        return embed