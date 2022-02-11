from enum import Enum 

class bookGenre(Enum):
    FICTION = 3
    NONFICTION = 3
    
    print("Display by genre: ")
    print(bookGenre.FICTION)
    print(bookGenre.NONFICTION)
    print()
    
class Book:
    bookID:int
    bookAuthor:str
    bookTitle:str
    bookType:bookGenre
    
    # constructor for book class, "self" = this, passes in the object itself 
    def __init__(self,bookID,bookAuthor,bookTitle,bookGenre)
    
    # display method, passes in self as parameter
    def printBook(self):
        print(self.bookID)
        print(self.bookAuthor)
        print(self.bookTitle)
    # call the name property to display string representation of enum bookGenre
        print(self.bookGenre.name)
        
    # little library implemented with a list, a predefined class in python  
    littleLibrary = list()
    
    littleLibrary.append(Book(001, "Richard Dawkins", "Books Do Furnish a Life", bookGenre.NONFICTION))
    littleLibrary.append(Book(002, "Yuval Noah Harari", "Homo Deus: A History of Tomorrow", bookGenre.NONFICTION))
    littleLibrary.append(Book(003, " Art Spiegelman", "MAUS: A Survivor's Tale", bookGenre.NONFICTION))
    littleLibrary.append(Book(004, "James Luceno", "Darth Plagueis", bookGenre.FICTION))
    littleLibrary.append(Book(005, "Miri Yu", "Tokyo Ueno Station", bookGenre.FICTION))
    littleLibrary.append(Book(006, "Mikhail Bulgakov", "Heart of a Dog", bookGenre.FICTION))
    
    # for loop for each index print the book, uses printBook method to display info
print("All books currently in library: ")
for index in range(len(littleLibary)):
    littlelibary[index].printBook()
    
    # for loop to display FICTION books
print("FICTION books currently in library: ")
for index in range(len(littleLibary)):
    if littleLibary[index].bookGenre == bookGenre.FICTION:
        littleLibary[index].printBook()
        
    # for loop to display NONFICTION books
print("NONFICTION books currently in library: ")
for index in range(len(littleLibary)):
    if littleLibary[index].bookGenre == bookGenre.FICTION:
        littleLibary[index].printBook()
