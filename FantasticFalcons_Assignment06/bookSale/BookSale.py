# File Name: BookSale.py
# Student Name: Zulqarnayan Hossain
# Group Name: Fantastic Falcons
# Email: hossaizn@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th Feb, 2025
# Course #/Section: 001
# Semester/Year: Spring 2025
# Brief Description of the assignment:  We create a Python project using classes for an object "Book" that holds meaning to us.
# Brief Description of what this module does: We use classes to model an object in the real world while adhering to the Visual Studio 2022 architecture taught in class.
# Anything else that's relevant: N/A


class BookSale:
    def __init__(self, book):
        """
        Initialize the BookSale class with a reference to a Book object.
        """
        self.book = book
        self._sold = False

    def __str__(self):
        status = "Sold" if self._sold else "Available"
        return "Sold Status of '" + self.book.title + "': " + status

    def sold(self):
        """
        Getter for the sold property.
        """
        return self._sold

    def set_sold(self, value):
        """
        Setter for the sold property along with validation.
        """
        if isinstance(value, bool):
            self._sold = value
        else:
            print("Invalid value! The Sold status can only be either True or False.")


    def mark_as_sold(self):
        """
        Mark the book as sold.
        """
        self._sold = True
        print("'" + self.book.title + "' has now been marked as SOLD using mark_as_sold.")


    def mark_as_available(self):
        """
        Mark the book as available.
        """
        self._sold = False
        print("'" + self.book.title + "' is now AVAILABLE by using mark_as_available.")


