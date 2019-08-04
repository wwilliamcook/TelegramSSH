# telegram_bot.py
# Author: Weston Cook
# Wrapper for the python-telegram-bot wrapper.


# References:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot/c8dd272e26b939168eaa5812de5bf2b066ff10d6


from telegram.ext import Updater, CommandHandler, MessageHandler, \
     Filters


class TelegramBot(object):
    def __init__(self, token, command_handlers, message_handler):
        """command_handlers should be dict of {command name: func} pairs"""
        # Assertions
        assert type(command_handlers) == dict
        assert 'start' in command_handlers
        
        self.__updater = Updater(token=token)
        dispatcher = self.__updater.dispatcher

        # Attach command handlers to dispatcher
        for cmd in command_handlers:
            dispatcher.add_handler(CommandHandler(cmd, command_handlers[cmd]))
        # Attach message handler to dispatcher
        dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    def start(self):
        """Start bot."""
        self.__updater.start_polling()
        self.__updater.idle()
