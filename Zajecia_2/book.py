book = input("What is the title of the book?: ")
author = input("What is the surname of author?: ")
sites = input("How many sites it has?: ")
book2 = book.isalpha()
author2 = author.isalpha()
book2 = book.title()
author2 = author.title()
book1 = book2 + " " + author2 + " " + sites
print(book1, str(len(book1)))
