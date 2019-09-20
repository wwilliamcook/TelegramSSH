# TelegramBot
Python Telegram bot that enables an 'admin' Telegram user to remotely execute commands on the bot machine. Includes secure password-based token storage.

## Getting Started
First install dependencies:

`pip install cryptography python-telegram-bot`

Then start the bot with

`python3 main.py --verbose`

You will be prompted to enter your bot's [API token](https://core.telegram.org/bots) and a password to encrypt and save it. After that, all that is required to run the bot is the password you entered the first time.

To reset your copy of the program, just delete the files ending in `.pickle`, which are used to store the encrypted API token.

### Dependencies:
- [python-telegram-bot](https://python-telegram-bot.org/)==12.1.1
- [cryptography](https://cryptography.io)

## License
See the [license](LICENSE) for information on how you can use this program.
See the dependencies' licenses for additional information:
- [Telegram Terms of Service](https://telegram.org/tos)
- [python-telegram-bot License](https://github.com/python-telegram-bot/python-telegram-bot#license)
- [cryptography License](https://github.com/pyca/cryptography/blob/master/LICENSE)
