"""

Using append mode 'a' to open a file

"""


def main():
    with open("/Users/Arunkumar_Mathe/Documents/python_practise/files/tmp_11_Mar.txt", 'w') as file:
        file.write("Hi Arun! \n")
        file.write("How are you ? \n")

    with open("/Users/Arunkumar_Mathe/Documents/python_practise/files/tmp_11_Mar.txt", 'a') as file:
        file.write("You are appending text to same file \n")
    
    print("Finished........")

if __name__ == "__main__":
    main()