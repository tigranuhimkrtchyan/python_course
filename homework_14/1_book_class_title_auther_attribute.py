"""
Create a Book class that has two attributes:
    .title
    .author
and two methods:
    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:
    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.
For instance, if I instantiated the following book using this Book class:
    Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:
Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
Notes
    Read more about Python classes in Resources.
    Remember, after you've finished writing the class and its methods, you must instantiate it through 
    the creation of new objects.
"""
from typing import Any


class Book:
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
        
    # def __new__(cls) -> Self:
    #     pass
    def __init__(self,title,auther) -> None:
        self.title = title
        self.auther = auther
    # def __str__(self) -> str:

    def get_title(self):
        return f"Tilte: {self.title}"
    def get_auther(self):
        return f"Auther: {self.auther}"
PP = Book('Pride and Prejudice','Jane Austen')
HP = Book(' Hamlet','William Shakespeare')
WP = Book(' War and Peace','Leo Tolstoy ')
print(HP.title)
print(HP.auther)
print(HP.get_title())
print(HP.get_auther())
