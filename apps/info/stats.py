import discord

class Stats():
    @staticmethod
    def show_statistics(interaction: discord.Interaction, user: discord.User = None):
        """
        Create embed for discord user statistics
        """
        print("Called stats method!")
        embed = discord.Embed(title='TamoBot Statistics for narlock', color=0xff3a40)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
        embed.add_field(name='General', value=':calendar: **Month Rank:** #2 (10 hrs)\n:star: **Focus Rank:** #5 (34 hrs)\n<:customEmote:1096777370318413954> **Tamo Tokens:** 1234', inline = False)
        embed.add_field(name='Arcade', value=':question: **Trivia Rank:** #10 (2)')
        """
        TODO
        Under the condition that the user has a special title in 'feat',
        add this as a new field to the stats.
        """
        embed.add_field(name='\u200b', value='Powered by [**narlock.dev**](https://narlock.github.io/narlock)', inline=False)

        return embed