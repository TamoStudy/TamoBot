import discord

class Shop():
    @staticmethod
    def show_shop_options():
        embed = discord.Embed(title="TamoBot Shop")
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name='Profile Customization', value=':dna: `/shopembed [hex]` (1000 <:customEmote:1096777370318413954> Tamo tokens)\n<:myemote:1097295903506829342> Customize profile embed color.\n\u200b\n:fire: `/shopcolor [#]` (500 <:customEmote:1096777370318413954> Tamo tokens)\n<:myemote:1097295903506829342> Customize your server name color.', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
        return embed