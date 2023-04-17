import discord

class Arcade():
    @staticmethod
    def show_arcade_options():
        embed = discord.Embed(title="TamoBot Arcade", color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name=':joystick: Single Player', value='**Trivia:** answer fun and simple trivia questions\n→ `/trivia` (100 Tamo tokens)', inline=False)
        embed.add_field(name=':signal_strength: Multi Player', value='**Coming Soon**', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)
        return embed
