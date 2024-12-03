"""
Write a program that asks the user to enter a password and compares it to a hard-coded password.

If the password is correct, the program print "Greetings professor Falcon" and exists.

If the password is incorrect, the program prints "Access denied" and then asks for the password again.

The program will ask for the password 3 times.

After that it exits.


"""




PASSWORD = "Arun@123"

for i in range(3):
    password = input("Please enter the password :")

    if (password == PASSWORD):
        print("Greetings professor Falcon")
        break
    else:
        print("Access Denied!")


