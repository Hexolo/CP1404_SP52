MIN_LENGTH = 5
MAX_LENGTH = 15


def main():
    """Program to get check user password"""
    password = get_password()
    while not is_valid_password:
        print(f"Invalid password! Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters")
    display_asterisk(password)


def display_asterisk(password):
    for char in password:
        print("*", end=" ")


def get_password():
    return input("Please enter your password: ")


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    else:
        return True


main()
