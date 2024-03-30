import discord
from discord.ext import commands
import settings
from utils.custom_help import CustomHelpCommand

# Setting up logging based on the configuration in the settings module
logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents, help_command=CustomHelpCommand())

    @bot.event
    async def on_ready():
        # Log bot's user information once the bot is ready
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        # Log the ID of the first guild (server) the bot is in
        logger.info(f"Guild ID: {bot.guilds[0].id}")

        # Load extensions (cogs) containing additional functionality for the bot
        await bot.load_extension("cogs.engine_game")
        await bot.load_extension("cogs.chess_training")

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)


if __name__ == '__main__':
    run()
