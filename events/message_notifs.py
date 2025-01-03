import discord
from discord.ext import commands
import logging

# Log configuration
logger = logging.getLogger("maxparser.event.on_message")


# this is where you configure biomes
# "BIOME": f"<@&ROLE_ID_HERE>"
biomes = {
    # "GLITCH": f"<@&1324848574600712233>",
    "GRAVEYARD": f"<@&1324840525995573309>",
    "PUMPKIN MOON": f"<@&1324848083741184020>",
    "NULL": f"<@&1324848147536543824>",
    "SAND STORM": f"<@&1324848108689162291>",
    "STARFALL": f"<@&1324848413522657411>",
    "HELL": f"<@&1324848369289527408>",
    "CORRUPTION": f"<@&1324848134160908328>",
    "RAINY": f"<@&1324840478058745866>",
    "WINDY": f"<@&1324840506643054724>",
    "SNOWY": f"<@&1324848304705765376>",
}

class MaxstellarMessageNotificator(commands.Cog): 
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    # on every message
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            logger.info(f'Bot message detected!')
            
            if message.embeds:
                for embed in message.embeds:
                    logger.debug(f"Embed title: {embed.title}")
                    logger.debug(f"Embed description: {embed.description}")
                    logger.debug(f"Embed url: {embed.url}")
                    
                    # has an embed description
                    if embed.description:
                        
                        # iterate over all the biomes and check if message contains any of them
                        for biome, mention in biomes.items():
                            
                            # if biome is in embed desc
                            if f'Biome Started - {biome}' in embed.description:
                                
                                # mention role
                                logger.info(f"Mentioning {mention} for biome {biome}")
                                await message.channel.send(mention)
                                break

            return
        
        # if you uncomment this, it will start logging every message sent on your server
        # only do this for debugging purposes, but its not really needed
        # logger.debug(f"[{message.channel.mention}]({message.channel.name}): {message.content}")
        
# Função para carregar a cog no bot
async def setup(bot: commands.Bot):
    await bot.add_cog(MaxstellarMessageNotificator(bot))