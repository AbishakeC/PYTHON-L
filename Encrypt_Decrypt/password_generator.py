import secrets
import string

def generate_password(length=16, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    characters = letters + digits + symbols

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__=="__main__":
    print(generate_password(20))
