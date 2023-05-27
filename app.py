class BookShelf:
    def __init__(self):
        return

    def addBook(self, name, author, price, publishing_year):
        self.BookName = name
        self.BookAuthor = author
        self.BookPrice = price
        self.BookYear = publishing_year

    def ReadBooks(self):
        print(f"""{self.BookName} was written by {self.BookAuthor} and It Cost {self.BookPrice}, It Was published in {self.BookYear}
        """)

Harry = BookShelf()
Harry.addBook("Don Quixote", "Miguel de Cervantes Saavedra", "$15.30", "1605")
Harry.ReadBooks()

Harry = BookShelf()
Harry.addBook("A Tale of Two Cities", "Charles Dickens", "$7.36 ", "1859")
Harry.ReadBooks()

Harry = BookShelf()
Harry.addBook("$7.36 ", "J.R.R.", "$10.09", "2001")
Harry.ReadBooks()