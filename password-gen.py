import random
import string

def generate_password(length=16, include_uppercase=True,include_lowercase=True, include_digits=True, include_specials=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_specials:
        characters += string.punctuation

    # Ensure the password length is at least 8, considering minimum requirements for each character set.
    length = max(length, 8)

    # Ensure the password meets minimum complexity requirements
    password = ""
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_lowercase:
        password += random.choice(string.ascii_lowercase)
    if include_digits:
        password += random.choice(string.digits)
    if include_specials:
        password += random.choice(string.punctuation)

    # Fill the remaining length with random characters
    password += "".join(random.choice(characters) for _ in range(length - len(password)))

    # Shuffle the password characters to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
