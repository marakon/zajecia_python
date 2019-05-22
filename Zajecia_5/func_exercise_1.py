def get_data():
    books = {}
    number = int(input("Ile ksiazek?: "))
    for booksy in range(number):
        book_name = input("Book: ")
        grade = int(input("Grade: "))
        books[book_name] = grade
    return books

def view_grade(book):
    if book in books:
        print("Book: {0} with grade: {1}".format(book, books[book]))
    else: print("We do not have such a book.")


books = get_data()
print(books)
name = input("What are you looking for?: ")
view_grade(name)

