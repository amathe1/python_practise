
def main():
    print(list((x,y) if x != y else '=' for x in range(0,4) if x != 1 for y in range(0,4) if y != 2))

    li = list()

    for x in range(0,4):
        if x == 1:
            continue

        for y in range(0,4):
            if y == 2:
                continue
            
            if x == y:
                li.append('=') 
            else: 
                li.append((x,y))

    print()
    print(li)

if __name__ == "__main__":  
    main()