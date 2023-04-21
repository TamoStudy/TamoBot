import discord

from tools.constants import Constants

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
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)

        return embed
    
    @staticmethod
    def notokens(tokens: int, amount: int) -> discord.Embed:
        embed = discord.Embed(title=f'You do not have enough Tamo tokens!', color=0xff3a40)
        embed.set_thumbnail(url='https://github.com/narlock/Kaizen/blob/main/KaizenClient/assets/INFO_ERROR_ORANGE.png?raw=true')
        embed.add_field(name='\u200b', value=f'It costs `{amount}` <:customEmote:1096777370318413954> Tamo tokens to perform this operation.\n<:myemote:1097295903506829342> You currently own `{tokens}` Tamo tokens.', inline=False)
        embed.add_field(name='\u200b', value=f'You can earn <:customEmote:1096777370318413954> Tamo tokens by spending focus time\nin a dedicated focus room!\n<:myemote:1097295903506829342> To check your amount of Tamo tokens, use `/stats`.', inline=False)
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)

        return embed