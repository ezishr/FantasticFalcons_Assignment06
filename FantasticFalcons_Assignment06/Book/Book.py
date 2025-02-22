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
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self._current_page = 1 
        self._bookmark = None

    def __str__(self):
        return f"'{self.title}' by {self.author} - Total Pages is {self.total_pages}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.total_pages})"

    def current_page_getter(self):
        return self._current_page

    def current_page_setter(self, page):
        if 1 <= page <= self.total_pages:
            self._current_page = page
        else:
            print("Invalid page number.")
        
    def bookmark_page_getter(self):
        """Return to the bookmarked page."""
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

