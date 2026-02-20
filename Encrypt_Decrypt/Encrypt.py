from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_key(data,key):
    f=Fernet(key)
    return f.encrypt(data.encode())

def decrypt_key(encrypted_data,key):
    f=Fernet(key)
    return f.decrypt(encrypted_data).decode()