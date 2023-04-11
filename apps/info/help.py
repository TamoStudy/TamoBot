import discord
from discord.ext import commands
import asyncio
from typing import Union


class Help:
    @staticmethod
    def get_help_embed(interaction: discord.Interaction):
        embed = discord.Embed(title="test")
        embed.set_footer("Info Commands - Page 1/3")