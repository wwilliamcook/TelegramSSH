# main.py
# Author: Weston Cook
# Runs a Telegram bot.


from telegram_bot import TelegramBot
from arg_parser import parseArgs
from get_token import getToken
import logging


admin_id = 31415927  # Insert your unique user ID here for bot to respond differently to admin


# Parse arguments
a = parseArgs()


def start_callback(bot, update):
    """Callback for handling a new conversation."""
    if update.message.from_user.id == admin_id:
        if a.verbose:
            print('New conversation started with admin.')
        update.message.reply_text('Welcome, admin.')
    else:
        if a.verbose:
            print('New conversation started with %s. User ID: %s' % (
                  update.message.from_user.first_name,
                  update.message.from_user.id))
        update.message.reply_text('Hello, %s. This bot does nothing!' % \
                                  update.message.from_user.first_name)


def update_callback(bot, update):
    """Callback for handling a new message."""
    if update.message.from_user.id == admin_id:
        if a.verbose:
            print('Received from admin: %s' % update.message.text)
        update.message.reply_text('Received: %s' % update.message.text)
    else:
        if a.verbose:
            print('New message received from %s:\n%s' % (
                update.message.from_user.first_name,
                update.message.text))
        update.message.reply_text(update.message.text)


def main(salt_path, token_path):
    if a.verbose:
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # Get telegram token and get the corresponding bot
    token = getToken(salt_path, token_path)
    print('Token successfully acquired, logging in...')
    bot = TelegramBot(token, start_callback, update_callback)
    print('Logged in. Bot started.')
    # Start bot
    bot.start()
    if a.verbose:
        print('Bot stopped.')


if __name__ == '__main__':
    main('salt.pickle', 'token.pickle')
