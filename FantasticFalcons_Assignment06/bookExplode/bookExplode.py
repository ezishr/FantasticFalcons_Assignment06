# File Name : bookExplode.py
# Student Name: Peyton Bock
# email:  bockps@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th Feb, 2025
# Course #/Section: 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Group project to model a real life senario and how it would be coded. 
# Brief Description of what this module does. We are modeling real life senerios in Visual Studio
# Citations: 
#http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
#https://realpython.com/python-property/

# Anything else that's relevant: N/A



class BookExplode:
    def __init__(self, book):
        """
        Initialize book explosion object.
        """
        self.book = book
        self.exploded = False

    def __str__(self):
        """
        String
        """
        return f"BookExplode(book={self.book.title}, exploded={self.exploded})"

    def __repr__(self):
        """
        Representation
        """
        return f"BookExplode({repr(self.book)}, exploded={self.exploded})"

    @property
    def is_exploded(self):
        """
        Getter
        """
        return self.exploded

    @is_exploded.setter
    def is_exploded(self, value):
        """
        Setter
        """
        if isinstance(value, bool):
            self.exploded = value
        else:
            raise ValueError("Explosion status must be a boolean.")

    def detonate(self):
        """
        Explodes the book.
        """
        if not self.exploded:
            self.exploded = True
            print(f"The book '{self.book.title}' has exploded into a thousand pieces!")
        else:
            print(f"The book '{self.book.title}' is already destroyed.")