import discord

class ErrorEmbed():
    @staticmethod
    def message(msg: str) -> discord.Embed:
        """
        Generates an error embed with a specified message.

        Args:
            msg (str)
        
        Returns:
            embed (discord.Embed)
        """
        embed = discord.Embed(title='TamoBot Error Occurred', color=0xff0000)
        embed.set_thumbnail(url='https://github.com/narlock/Kaizen/blob/main/KaizenClient/assets/INFO_ERROR_ORANGE.png?raw=true')
        embed.add_field(name="Error was raised", value=f"{msg}", inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed