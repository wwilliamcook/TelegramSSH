# main.py
# Author: Weston Cook
# Runs a Telegram bot.


# References:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot/c8dd272e26b939168eaa5812de5bf2b066ff10d6


from telegram_bot import TelegramBot
from arg_parser import parseArgs
from get_token import getToken
import logging


admin_id = 314159265  # Insert your unique user ID here


# Parse arguments
a = parseArgs()


def main(salt_path, token_path):
    if a.verbose:
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # Get telegram token and get the corresponding bot
    token = getToken(salt_path, token_path)
    print('Token successfully acquired, logging in...')
    bot = TelegramBot(token, admin_id=admin_id, verbose=a.verbose)
    print('Logged in. Bot started.')
    # Start bot
    bot.start()
    bot.idle()
    if a.verbose:
        print('Bot stopped.')


if __name__ == '__main__':
    main('salt.pickle', 'token.pickle')
