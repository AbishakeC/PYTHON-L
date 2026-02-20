from password_generator import generate_password
from generate_QR import generate_QR_code
from Encrypt import generate_key,encrypt_key


def main():
    length = int(input("Enter password length: "))

    password = generate_password(length)
    print(f"Generated Password: {password}")

    key = generate_key()
    encrypted = encrypt_key(password, key)

    filename = generate_QR_code(encrypted.decode())

    print(f"Encrypted QR saved as {filename}")
    print(f"Encryption Key (SAVE THIS): {key.decode()}")


if __name__ == "__main__":
    main()