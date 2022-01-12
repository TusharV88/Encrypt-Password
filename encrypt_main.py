# Encrypt a password

from cryptography.fernet import Fernet


# Take password from user to encrypt    
user_pass = input('Enter your password to encrypt : ')

# Generate the key by using Fernet
key = Fernet.generate_key()

# Instance the Fernet class with the key
fernet = Fernet(key)

# Use Fernet class instance to encrypt
enc_pass = fernet.encrypt(user_pass.encode())

print(f'Encrypted Password : {enc_pass}')


