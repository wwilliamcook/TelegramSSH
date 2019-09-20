"""Runs a Telegram bot that can be used to remotely execute commands.

References:
- https://python-telegram-bot.readthedocs.io/en/stable/index.html
- https://core.telegram.org/bots/api

@author Weston Cook
"""


from telegram_bot import TelegramBot
from get_token import getToken
import argparse
import logging


admin_id = 314159265  # Insert your unique user ID here


def main(args):
    if args.verbose:
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # Get telegram token and get the corresponding bot
    token = getToken(args.salt_path, args.token_path)
    print('Token successfully acquired, logging in...')
    bot = TelegramBot(token, admin_id=admin_id, verbose=args.verbose)
    print('Logged in. Bot started.')
    # Start bot
    bot.start()
    bot.idle()
    if args.verbose:
        print('Bot stopped.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--salt_path', type=str, default='salt.pickle')
    parser.add_argument('--token_path', type=str, default='token.pickle')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    args = parser.parse_args()
    
    main(args)
