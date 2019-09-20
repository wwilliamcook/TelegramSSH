# telegram_bot.py
# Author: Weston Cook
# Wrapper for the python-telegram-bot wrapper.


# References:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot/c8dd272e26b939168eaa5812de5bf2b066ff10d6


import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os


class TelegramBot(object):
    """Telegram bot."""
    def __init__(self, token, admin_id=None, verbose=False):
        self._verbose = verbose
        self.updater = Updater(token=token, use_context=True)
        self._admin_id = admin_id
        self._admin_chat_id = None
        # Set up handlers
        start_handler = CommandHandler('start', self._start_callback)
        exec_handler = CommandHandler('exec', self._exec_callback)
        message_handler = MessageHandler(Filters.text, self._message_callback)
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(exec_handler)
        dispatcher.add_handler(message_handler)
        #
        if verbose:
            print('Connected to bot API as {}'.format(self.bot.get_me().username))
    
    @property
    def bot(self):
        return self.updater.bot
    
    def _is_admin(self, message):
        """Check whether the message was sent by the admin."""
        if self._admin_id is not None:
            if message.from_user.id == self._admin_id:
                return True
        return False
    
    def _start_callback(self, update, context):
        if self._admin_id is not None and self._admin_chat_id is None:
            if update.message.from_user.id == self._admin_id:
                self._admin_chat_id = update.message.chat_id
                if self._verbose:
                    print('New chat started with admin ({}/@{})'.format(
                        update.message.from_user.first_name,
                        update.message.from_user.username
                    ))
        if self._is_admin(update.message):
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Welcome, admin.')
            if self._verbose:
                print('Admin issued \"start\" command.')
        else:
            msg = 'New chat started with {}/@{} ({})'.format(
                update.message.from_user.first_name,
                update.message.from_user.username,
                update.message.from_user.id
            )
            self.send_admin_message(msg, log=True)
            if self._verbose:
                print(msg)

    def _exec_callback(self, update, context):
        if self._is_admin(update.message):
            cmd = ' '.join(context.args)
            if self._verbose:
                print('Executing: {}'.format(cmd))
            p = os.popen(cmd)
            out = p.read()
            p.close()
            context.bot.send_message(chat_id=update.message.chat_id, text=out)
        else:
            msg = 'Warning! Unauthorized user attempted to issue \"exec\" command:\n{}/@{} ({})'.format(
                update.message.from_user.first_name,
                update.message.from_user.username,
                update.message.from_user.id
            )
            self.send_admin_message(msg, log=True)
            if self._verbose:
                print(msg)

    def _message_callback(self, update, context):
        if self._is_admin(update.message):
            context.bot.send_message(
                chat_id=update.message.chat_id,
                text='Bot is online.\nEcho: \"{}\"'.format(update.message.text)
            )
        else:
            msg = '{}/@{} ({}) says:\n{}'.format(
                update.message.from_user.first_name,
                update.message.from_user.username,
                update.message.from_user.id,
                update.message.text
            )
            self.send_admin_message(msg, log=True)
            if self._verbose:
                print(msg)
    
    def send_admin_message(self, text, log=FAlse):
        """Send a message to the admin."""
        if log:
            text = '[TELEGRAM LOG]\n' + text
        if self._admin_chat_id is not None:
            self.bot.send_message(chat_id=self._admin_chat_id, text=text)
            return True
        else:
            return False

    def start(self):
        """Begin polling for new commands/messages."""
        self.updater.start_polling()
    
    def idle(self):
        self.updater.idle()
