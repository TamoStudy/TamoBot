import discord

class Stats():
    @staticmethod
    def show_statistics(interaction: discord.Interaction, user: discord.User = None):
        """
        Create embed for discord user statistics
        """
        print("Called stats method!")
        # TODO