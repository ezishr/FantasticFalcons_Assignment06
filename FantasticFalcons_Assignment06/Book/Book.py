# File Name: Book.py
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

class Book:
    def __init__(self, title, author, total_pages):
        """
        Initialize a new book object and set several properties.
        @param title: The title of the book.
        @param author: The author of the book.
        @param total_pages: The total number of pages in the book.
        """
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self._current_page = 1 
        self._bookmark = None

    def __str__(self):
        """
        Return a string with __str__ method.
        """
        return f"'{self.title}' by {self.author} - Total Pages is {self.total_pages}"

    def __repr__(self):
        """
        Return a representation of the book object with __repr__ method.
        """
        return f"Book('{self.title}', '{self.author}', {self.total_pages})"

    def current_page_setter(self, page):
        """
        Setter funtion to set the current page.
        @param page: The page number to set as the current page.
        """
        if 1 <= page <= self.total_pages:
            self._current_page = page
        else:
            print("Invalid page number.")

    def current_page_getter(self):
        """
        Getter function to get the current page.
        """
        return self._current_page

    def bookmark_page_getter(self):
        """
        Return to the bookmarked page.
        """
        if self._bookmark:
            self._current_page = self._bookmark
            print(f"Returned to bookmarked page {self._current_page}.")
        else:
            print("No bookmark set.")


    def bookmark_page_setter(self):
        """Bookmark the current page."""
        self._bookmark = self._current_page
        print(f"Bookmarked page {self._bookmark}.")



if __name__ == "__main__":
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    
    print(my_book) 
    my_book.turn_page(10)  
    print(my_book)  
    my_book.bookmark_page()  
    my_book.turn_page(50)  
    print(my_book)  
    my_book.go_to_bookmark()  
    print(my_book)  

