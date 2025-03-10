from itertools import groupby


def enlarge_strr(s):
    return "".join(f"{len(list(group))}{char}" for char, group in groupby(s) )
    

def main():
    strr = "aaaaabbbbcccdde"
    print(enlarge_strr(strr))

main()

