import discord
from sql.mysqlconnection import MySQLConnection
from tools.constants import Constants
from tools.tamolog import TamoLogger

class TriviaButtons(discord.ui.View):
    def __init__(self, db: MySQLConnection, embed: discord.Embed, user_id: int):
        super().__init__(timeout=None)
        self.db = db
        self.embed = embed
        self.user_id = user_id

        # TODO Get Question, Options from MySQL Database
        self.question = '**What is Discord\'s  signature color?**'
        self.options = ['Red', 'Blurple', 'Green', 'Gray']
        self.correct = 1

        self.options_message = f'**A**: {self.options[0]}\n**B**: {self.options[1]}\n**C**: {self.options[2]}\n**D**: {self.options[3]}'
        self.embed.set_field_at(0, name='\u200b', value=self.question, inline=False)
        self.embed.set_field_at(1, name='\u200b', value=self.options_message, inline=False)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Check if the user who clicked the button is the same as the user who initiated the game."""
        return interaction.user.id == self.user_id

    @discord.ui.button(label='A', style=discord.ButtonStyle.blurple)
    async def option_a(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.embed.set_field_at(0, name='\u200b', value=f'You selected **A**', inline=False)
        self.check_correct_answer(0)
        self.clear_items()
        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(label='B', style=discord.ButtonStyle.blurple)
    async def option_b(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.embed.set_field_at(0, name='\u200b', value=f'You selected **B**', inline=False)
        self.check_correct_answer(1)
        self.clear_items()
        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(label='C', style=discord.ButtonStyle.blurple)
    async def option_c(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.embed.set_field_at(0, name='\u200b', value=f'You selected **C**', inline=False)
        self.check_correct_answer(2)
        self.clear_items()
        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(label='D', style=discord.ButtonStyle.blurple)
    async def option_d(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.embed.set_field_at(0, name='\u200b', value=f'You selected **D**', inline=False)
        self.check_correct_answer(3)
        self.clear_items()
        await interaction.response.edit_message(embed=self.embed, view=self)

    def check_correct_answer(self, selection: int):
        if selection == self.correct:
            self.embed.color = discord.Color.green()
            self.embed.set_field_at(1, name='\u200b', value='You answered correctly!', inline=False)
        else:
            self.embed.color = discord.Color.red()
            self.embed.set_field_at(1, name='\u200b', value='You answered incorrectly!', inline=False)

class Trivia():
    def __init__(self):
        pass

    """
    Plays the trivia game.

    1. Check if the user is eligible to play Trivia. The user must have 
    """
    def play_trivia(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"Trivia Question for {interaction.user.name}", color=0xffa500)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/TamoStudy/TamoBot/main/README%20Assets/TamoBot.png')
        embed.add_field(name='\u200b', value='', inline=False)
        embed.add_field(name='\u200b', value='', inline=False)
        embed.add_field(name='\u200b', value=Constants.get_footer_string(), inline=False)
        return embed