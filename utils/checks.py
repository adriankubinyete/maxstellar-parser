import discord
import os
import logging
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger("sofonbot.checks")

def is_me():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == os.getenv("BOT_OWNER") or interaction.user.id in os.getenv("BOT_OWNER")
    return app_commands.check(predicate)
    
def is_test_guild():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.guild.id == os.getenv("TESTING_GUILD_ID" or interaction.guild.id in os.getenv("TESTING_GUILD_ID"))
    return app_commands.check(predicate)
