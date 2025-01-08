


def ask_user_status():
    response = input("How are you? : ")
    if response == "OK" or response == "ok":
        print("Excellent!")
    else:
        print("Oh no...!")


def main():
    ask_user_status()

main()