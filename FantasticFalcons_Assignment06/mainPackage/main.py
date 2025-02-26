# File Name: main.py
# Student Name: Eirlys Vo, Zulqarnayan Hossain, Peyton Bock, Nogaye Gueye
# Group Name: Fantastic Falcons
# Email: vopq@mail.uc.edu, hossaizn@mail.uc.edu, bockps@mail.uc.edu, gueyene@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th Feb, 2025
# Course #/Section: 001
# Semester/Year: Spring 2025
# Brief Description of the assignment:  We create a Python project using classes for an object "Book" that holds meaning to us.

# Brief Description of what this module does: We use classes to model an object in the real world while adhering to the Visual Studio 2022 architecture taught in class.

# Anything else that's relevant: N/A

from re import M
from Book.Book import *
from bookSale.BookSale import *   
from bookExplode.bookExplode import *
from BookColors.BookColors import *

if __name__ == "__main__":
    # Test with Book class
    my_book = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald", total_pages = 180)
    print(f"Print __str__: {my_book.__str__()}")
    print(f"Print __repr__: {my_book.__repr__()}\n")
    my_book.current_page_setter(page = 20)
    print(f"Print current page: {my_book.current_page_getter()}")



    # Testing the BookSale Class Begins Here
    book_sale = BookSale(book=my_book)

    print("Initial Sold Status: " + book_sale.__str__())  

    # Checking the Sold Status with getter
    print("Sold Status Before Any Changes: " + str(book_sale.sold()))  

    # Setting the Sold Status to True
    book_sale.set_sold(True)
    print("Sold Status After Implementing set_sold: " + str(book_sale.sold()))  

    # Setting Sold Status with an invalid value
    print("Trying to set Sold Status to an Invalid Value in the Following Line:")
    book_sale.set_sold("yes") # This prints an error message

    # Mark the book as sold
    book_sale.mark_as_sold()   

    # Mark the book as available
    book_sale.mark_as_available()  

    # Testing the BookSale Class Ends Here

    # Testing the BookExplode Class Begins Here
    book_explosion = BookExplode(book=my_book)

    print(f"Print __str__: {book_explosion.__str__()}")
    print (f"Print __repr__: {book_explosion.__repr__()}")

    print(f"Initial Explosion Status: {book_explosion.is_exploded}")
    
    # Detonate the book
    book_explosion.detonate()

    # Try detonating again
    book_explosion.detonate()

    print(f"Final Explosion Status: {book_explosion.is_exploded}")
    # Testing the BookExplode Class Ends Here


    # Testing the BookColor Class Begins Here
    my_book = type('Book', (object,), {'title': "Sample Book"})()  # Creating a mock book object
    book_color = BookColors(book=my_book)

    print("Initial Color Status: " + book_color.__str__())  

    # Checking the Color Status with getter
    print("Color Status Before Any Changes: " + str(book_color.get_color()))  

    # Setting the Color Status to a valid value
    book_color.set_color("Red")
    print("Color Status After Implementing set_color: " + str(book_color.get_color()))  

    # Setting Color Status with an invalid value
    print("Trying to set Color Status to an Invalid Value in the Following Line:")
    book_color.set_color(123) # This prints an error message

    # Change the book color
    book_color.change_color("Blue")   

    # Reset the book color to default
    book_color.reset_color()
    # Testing the BookColor Class Ends Here