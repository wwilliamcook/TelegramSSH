# telegram_bot.py
# Author: Weston Cook
# Wrapper for the python-telegram-bot wrapper.


# References:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot/c8dd272e26b939168eaa5812de5bf2b066ff10d6


from telegram.ext import Updater, CommandHandler, MessageHandler, \
     Filters


class TelegramBot(object):
    def __init__(self, token, start_callback, message_callback):
        self.__updater = Updater(token=token)
        dispatcher = self.__updater.dispatcher

        # Construct handlers
        start_handler = CommandHandler('start', start_callback)
        update_handler = MessageHandler(Filters.text, message_callback)

        # Attach handlers to dispatcher
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(update_handler)

    def start(self):
        """Start bot."""
        self.__updater.start_polling()
        self.__updater.idle()
