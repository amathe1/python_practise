
def greeting():
    print("Welcome! No unauthorized users...")


PASSWORD = "hello"

def ask_user_password():
    password = input("Please enter your password > ")

    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied")


def main():
    greeting()
    ask_user_password()

main()