# File Name: BookColor.py
# Student Name: Nogaye Gueye 
# Group Name: Fantastic Falcons
# Email: gueyene@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th Feb, 2025
# Course #/Section: 001
# Semester/Year: Spring 2025
# Brief Description of the assignment:  We create a Python project using classes for an object "Book" that holds meaning to us.

# Brief Description of what this module does: We use classes to model an object in the real world while adhering to the Visual Studio 2022 architecture taught in class.

# Anything else that's relevant: N/A


class BookColor:
    def __init__(self, book):
        """
        Initialize the BookColor class with a reference to a Book object.
        """
        self.book = book
        self._color = "Unknown"  # Default color status

    def __str__(self):
        return "Color Status of '" + self.book.title + "': " + self._color

    def get_color(self):
        """
        Getter for the book color property.
        """
        return self._color

    def set_color(self, value):
        """
        Setter for the book color property with validation.
        """
        if isinstance(value, str) and value.strip():
            self._color = value.strip()
        else:
            print("Invalid value! The color must be a non-empty string.")

    def change_color(self, new_color):
        """
        Change the book's color status.
        """
        self._color = new_color.strip()
        print("'" + self.book.title + "' is now set to color: " + self._color)

    def reset_color(self):
        """
        Reset the book's color to the default.
        """
        self._color = "Unknown"
        print("'" + self.book.title + "' color has been reset to Unknown.")
