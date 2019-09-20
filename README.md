# TelegramSSH
Python Telegram bot that enables an 'admin' Telegram user to remotely execute commands on the bot machine. Includes secure password-based token storage.

## Getting Started
First install dependencies:

`pip install cryptography python-telegram-bot`

Then start the bot with

`python3 main.py --verbose`

You will be prompted to enter your bot's [API token](https://core.telegram.org/bots) and a password to encrypt and save it. After that, all that is required to run the bot is the password you entered the first time. Alternatively, you can hard code an encryption password into `main.py` to avoid having to enter it every time.

Start a chat with this bot using your Telegram account and make note of the nine-digit user ID that the program prints at the console. Put this ID in `main.py` as the admin ID. You can now remotely execute commands by using the `/exec` command in Telegram. For example, try `/exec ls` to see what files are in the program's working directory.

### Dependencies:
- [python-telegram-bot](https://python-telegram-bot.org/)==12.1.1
- [cryptography](https://cryptography.io)

## License
See the [license](LICENSE) for information on how you can use this program.
See the dependencies' licenses for additional information:
- [Telegram Terms of Service](https://telegram.org/tos)
- [python-telegram-bot License](https://github.com/python-telegram-bot/python-telegram-bot#license)
- [cryptography License](https://github.com/pyca/cryptography/blob/master/LICENSE)
