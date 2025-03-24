"""
Handling JSON files !

JSON : Java Script Object Notation

"""

from pickle import dump, load


def main():
    names = ['Arun', 'Anupama', 'Thoshith']
    age = [36, 35, 1.5]
    dom = {
        'Arun' : 'January',
        'Anu' : 'July',
        'Thoshith' : 'September'
    }

    filename = "/Users/Arunkumar_Mathe/Documents/python_practise/files/data.json"

 

    to_save = {
        'name' : names,
        'ages' : age,
        'birth_month' : dom
    }

    with open(filename, 'wb') as file:
        dump(to_save, file)

    with open(filename, 'rb') as file:
        loaded = load(file)
    
    print(loaded)


if __name__ == "__main__":
    main()