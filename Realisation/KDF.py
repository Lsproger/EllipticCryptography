import os
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.backends import default_backend
from pbkdf2 import crypt
from pbkdf2 import PBKDF2
from hashlib import sha384 as SHA384
salt = os.urandom(8)

kdf = PBKDF2("Hello", salt=salt, iterations=400, digestmodule=SHA384).read(32)
print(int.from_bytes(kdf, 'big'))

pwhash = crypt("secret")
alleged_pw = input("Enter password: ")
if pwhash == crypt(alleged_pw, pwhash):
    print("Password good")
else:
    print("Invalid password")


