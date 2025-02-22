# File Name: main.py
# Student Name: Eirlys Vo
# Group Name: Fantastic Falcons
# Email: vopq@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th Feb, 2025
# Course #/Section: 001
# Semester/Year: Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does:

# Anything else that's relevant:

from re import M
from Book.Book import *

if __name__ == "__main__":
    # Test with Book class
    my_book = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald", total_pages = 180)
    print(f"Print __str__: {my_book.__str__()}")
    print(f"Print __repr__: {my_book.__repr__()}\n")
    my_book.current_page_setter(page = 20)
    print(f"Print current page: {my_book.current_page_getter()}")
