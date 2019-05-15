
book = str(input("What is the title of the book?: "))
author = str(input("What is the surname of author?: "))
sites = int(input("How many sites it has?: "))
def book_func(str book, str author, int sites):
    book2 = book.isalpha()
    author2 = author.isalpha()
    book2 = book.capitalize()
    author2 = author.capitalize()
    book1 = book2 + " " + author2 + " " + str(sites)
    print(book1, str(len(book1)))

def test_book_func():
    assert book_func()

book_func(book, author, sites)
