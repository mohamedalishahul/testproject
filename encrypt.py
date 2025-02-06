import os
import gnupg

file_path = 'program.txt'
passphrase = 'password'

def encrypt_file(file_path, passphrase):
    gpg = gnupg.GPG()

    with open(file_path, 'rb') as f:
        file_data = f.read()

    encrypted_data = gpg.encrypt(file_data, recipients=None, symmetric=True, passphrase=passphrase)

    if not encrypted_data.ok:
        print(f"Failed to encrypt: {encrypted_data.status}")
        return

    encrypt_file_path = file_path + '.gpg'
    with open(encrypt_file_path, 'wb') as f:
        f.write(encrypted_data.data)
        
    os.remove(file_path)

    print(f"file{file_path} has been encrypted and saved as {encrypt_file_path}. The original file has been removed.")

encrypt_file(file_path, passphrase)


