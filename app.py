import logging
from telegram.ext import Updater, CommandHandler
from games import GameManager
from config import Config

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    # Initialize game manager and config
    game_manager = GameManager()
    config = Config()

    # Create updater
    updater = Updater(config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    commands = {
        'start': game_manager.start,
        'join': game_manager.join,
        'neverhaveiever': game_manager.never_have_i_ever,
        'truthordrink': game_manager.truth_or_drink,
        'mostlikely': game_manager.most_likely,
        'kingscup': game_manager.kings_cup,
        'randomtask': game_manager.random_task,
        'stats': game_manager.player_stats,
        'endgame': game_manager.end_game,
        'help': game_manager.help
    }

    for command, handler in commands.items():
        dp.add_handler(CommandHandler(command, handler))

    # Start the bot
    if config.ENV == "PRODUCTION":
        updater.start_webhook(
            listen="0.0.0.0",
            port=config.PORT,
            url_path=config.TELEGRAM_TOKEN,
            webhook_url=f"https://{config.APP_NAME}.herokuapp.com/{config.TELEGRAM_TOKEN}"
        )
        logger.info("Webhook set up in production mode")
    else:
        updater.start_polling()
        logger.info("Bot started in polling mode")

    updater.idle()

if __name__ == '__main__':
    main()
