import discord

class Top():
    @staticmethod
    def display_top(interaction: discord.Interaction):
        """
        Returns the embed for the top users on the server.
        """
        embed = discord.Embed(title='TamoBot Focus Leaderboard', color=0xffa500)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
        embed.add_field(name=':first_place:', value='narlock (120 hrs)', inline=False)
        embed.add_field(name=':second_place:', value='beside bella (102 hrs)', inline=False)
        embed.add_field(name=':third_place:', value='Melody (100 hrs)', inline=False)
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed