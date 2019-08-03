# TelegramBot
Premade Python Telegram bot with secure token storage. Written for Python 3.

## Getting Started
First install dependencies:

`python3 -m pip install cryptography python-telegram-bot==11.1.0`

Then start the bot with

`python3 main.py --verbose`

You will be prompted to enter your bot's [API token](https://core.telegram.org/bots) and a password to encrypt and save it. After that, all that is required to run the bot is the password you entered the first time.

To reset your copy of the program, just delete the files ending in `.pickle`, which are used to store the encrypted API token.

### Dependencies:
- [python-telegram-bot](https://python-telegram-bot.org/)==11.1.0
- [cryptography](https://cryptography.io)==2.1.4

## Usage
Modify the callback functions in `main.py` to give your bot functionality.

## License
See the [license](LICENSE) for information on how you can use this program.
See the dependencies' licenses for additional information:
- [Telegram Terms of Service](https://telegram.org/tos)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot#license)
- [cryptography License](https://github.com/pyca/cryptography/blob/master/LICENSE)
