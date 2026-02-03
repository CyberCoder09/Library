from models import Book

def main(): 
    book_ISBN = input("Enter the book ISBN: ") 
    book_title = input("Enter the title of the book: ")
    book_author = input(f"Enter the author of the book {book_title}: ")
    book_illustrator = input(f"Enter the illustrator of the book {book_title}: ")
    book_publisher = input(f"Enter the publisher of the book {book_title}: ")
    book_publication_date = input(f"Enter the publication date  of the book {book_title}: ")
    book_language = input(f"Enter the language of the book {book_title}: ")
    book_edition = int(input(f"Enter the edition (in decimal format) of the book {book_title}: "))
    book_genre = input(f"Enter the genre of the book {book_title}: ") 
    book_format = input(f"Enter the format of the book {book_title}: ")

    book_obj = Book(book_ISBN, book_title, book_author, book_illustrator, book_publisher, book_format, 
               book_publication_date, book_language, book_edition, book_genre)
    
    book_obj.view_book()
   
if "__name__" == "__main__":
    main()
