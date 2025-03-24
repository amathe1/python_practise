


"""

Python program to count the words in a given file and writting the word, count information into another file

"""

import re
from collections import defaultdict

def main():
    filename = r"/Users/Arunkumar_Mathe/Documents/python_practise/files/text.txt"
    pattern = re.compile(r'([a-zA-Z]*)', flags=re.I)

    counts = defaultdict(int)

    with open(filename, 'rt') as file:
        for line in file:
            words = re.findall(pattern, line)

            for word in words:
                counts[word.lower()] += 1

    counts = dict(sorted(counts.items(), key=lambda item: item[1]))
    #print(counts)

    with open(r'/Users/Arunkumar_Mathe/Documents/python_practise/files/text1.txt', 'wt') as file:
        for word, count in counts.items():
            file.write(f'{word}, {count} \n')
        
    print("Written word counts")


if __name__ == "__main__":
    main()