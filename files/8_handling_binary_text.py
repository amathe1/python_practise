

def main():
    
    data = bytearray([1, 2, 255, 0xFF])
    print(list(data))


    data = bytearray("Hello", 'utf8')
    print(list(data))

if __name__ == "__main__":
    main()