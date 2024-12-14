class Book:
    def __init__(self, title, author, publication_year, genre, pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages
    
    def compare_pages(self, other_book):
        if self.pages < other_book.pages:
            return -1
        elif self.pages > other_book.pages:
            return 1
        else:
            return 0
        
    def get_info():
        return (f"")
    
    def is_long_book(self):
        return self.pages > 300 # True False
    
    def update_genre(self, new_genre):
        self.genre = new_genre
        
    def __str__(self):
        return f"Название: {self.title}, Автора: {self.author}"


book1 = Book("1", "1", 1, "1", 5)
book2 = Book("1", "1", 1, "1", 5)  

compare_resut = book1.compare_pages(book2)
print(compare_resut)

print(book1)