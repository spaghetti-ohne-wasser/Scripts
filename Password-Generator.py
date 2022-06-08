from random import choice

ascii_lower: str = "abcdefghijklmnopqrstuvwxyz"
ascii_upper: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers: str = "0123456789"
symbols: str = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
chars: str = ascii_lower + ascii_upper + numbers + symbols

def generate_password(lenght: int):
    return "".join(choice(chars) for _ in range(lenght))

if __name__ == "__main__":
    try:
        print("Your Password: " + generate_password(int(input("Password lenght: "))))
    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt STRG-C")
