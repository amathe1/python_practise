"""

Put this data in a suitable data structure.

Science Fiction : "Martian", "Interstellar"
Drama           : "Bahubali", "RRR"

Now progrmatically add this book :
Science Fiction : "Kalki"

Do not assume that category already exists in the data structure. 
Write code that will add the book whether the category already exists or not.

Write code that prints all categories and books in them.

Write a function that can determine whether a particular book is present in the data structure.

Assume :
1. Categories are unique (cannot have 2 different categories with same name)
2. Book titles are unique
3. We want to be able to easily determine which books are in a given category
4. The order of the book titles doesn't matter
5. We want to be able to quickly determine if a given book is present in given category
6. We want to be able to easily add books to a category.


How to analyze ?
==============

- As per observation, categories are unique; can't have 2 categories with same name (so it may be keys in dictionary (OR) set)
- Also, book titles are unique (so it could be a set (OR) can be keys in dictionary)

3. We want to be able to easily determine which books are in a given category
- As per above point, categories could be keys in dictionary and book names could be values in the dictionary

4. The order of the book titles doesn't matter
- This indicates a set, BUT if order is important then it could be list, here tuple(immutable) is ruled out as we need to insert new books

5. We want to be able to quickly determine if a given book is present in given category
- Searching for a element "in" is fast in set

So, finally a dictionary of set is appropriate


"""

# Understand that only one return will execute at any cost
# if book is available then this function will return "True" (and final return False statement only execute)
# if book is not available then this function will return "False" (it won't go into for loop at all)
def find_book(library, book):
    for books in library.values():
        if book in books:
            return True
    
    return False



def add_book(library, category, title):
    # if category of book is not in library(dictionary) then
    # dictionary[category] will be assigned to an empty set (as this is a dict with values as "set")
    # this making this category added into the dictionary (library) as a empty set
   
    if not category in library:
        library[category] = set()

     # then adding the title of the book
    library[category].add(title)



def main():
    # Declaring a library with category as keys and books as values {key --> value}
    library = {
        "Science Fiction" : {"Martian", "Interstellar"},
        "Drama"           : {"Baahubali", "RRR"}
    }

    # Calling def to add a given book
    add_book(library, "Science Fiction 2", "War of worlds")

    # looping category (keys) in dictionary
    # then assigning all values (sets) into books
    # then printing category with end as empty (not new line)
    # and then after Category : ; joining book titles to each category using "join" method
    for category in library:
        books = library[category]
        print(category + " : ", end=" ")
        print(" , ".join(books))

    print(find_book(library, "RRR"))


main()