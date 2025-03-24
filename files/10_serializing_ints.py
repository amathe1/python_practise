


def main():
    # Serializarion
    data = (0x123456).to_bytes(3, 'big')
    print(type(data))
    print(f'{data[0] : x}')
    print(f'{data[1] : x}')
    print(f'{data[2] : x}')

    print(data)

    # De-serialization

    value = int.from_bytes(data, 'big')
    print(hex(value))


if __name__ == "__main__":
    main()