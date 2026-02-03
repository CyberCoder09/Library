import datetime

class Book(): # Create a Book class
    def __init__(self, isbn:str, title:str, author:str, illustrator:str, publisher:str, 
                format:str, publication_date, language:str, ediiton:int, genre:str, status:bool=True):
    
        self.isbn = isbn                            # Initalize ISBN 
        self.title = title                          # Initialize Book Title
        self.author = author                        # Initialize Author
        self.illustrator = illustrator              # Initialize Illustrator
        self.publisher = publisher                  # Initialize Publisher
        self.format = format                        # Initialize Format
        self.publication_date = publication_date    # Initialize Publication Date
        self.language = language                    # Initialize Language
        self.edition = ediiton                      # Initialize Edition
        self.genre = genre                          # Initialize Genre
        self.status = status                        # Initialize Status

    def view_book(self): # View a book 
        if self.status:
            print(f"Book Title: {self.title} | ISBN: {self.isbn}", end="\n")
            print(f"Author: {self.author} | Illustrator: {self.illustrator} | Publisher: {self.publisher}", end="\n")
            print(f"Publication Date: {self.publication_date}  | Language: {self.language}", end="\n")
            print(f"Editon: {self.edition} | Genre: {self.genre}", end="\n")
        else:
            print("Book currently unavaliable!")
        

    def view_book_title(self):
        print(f"Book Title: {self.title}!")
        
class Dog:
    def speak(self):
        return "woof"


class Cat:
    def speak(self):
        return "Meow"

def animalTalk(animal):
    print(animal.speak())

d1 = Dog()
c1 = Cat()

animalTalk(d1)
animalTalk(c1)



      