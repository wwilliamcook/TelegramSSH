# crypto_tools.py
# Author: Weston Cook
# Used for password-based fernet encryption/decryption of arbitrary serializable objects.


import base64
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import pickle


def getSalt(salt_path=None):
    """Read salt from path if found, otherwise generate new and save."""
    if salt_path is None:
        return os.urandom(16)
    else:
        # Recover or generate salt
        try:
            # Read salt from file
            with open(salt_path, 'rb') as f:
                return f.readline()
        except FileNotFoundError:
            # Generate new salt and save to salt_path
            salt = getSalt()
            with open(salt_path, 'wb+') as f:
                f.write(salt)
            return salt


def getKeyFromPassword(salt, password):
    """Return a fernet key generated from the given salt and password."""
    # Get ready to convert password to a key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())

    # Get password from user and turn it into a fernet key
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    return key


def validateFernet(key, validation_token, validation_data):
    """Validate the given key with the given token and return a fernet if successful."""
    f = Fernet(key)
    if f.decrypt(validation_token) == validation_data:
        return f
    else:
        raise ValueError('Invalid key.')


def encrypt(obj, fernet):
    """Encrypt a serializable object using the given fernet."""
    return fernet.encrypt(pickle.dumps(obj))


def decrypt(token, fernet):
    """Decrypt a token into a serializable object using the given fernet."""
    return pickle.loads(fernet.decrypt(token))
