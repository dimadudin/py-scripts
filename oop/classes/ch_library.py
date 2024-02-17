class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        res_books = []
        for i in range(len(self.books)):
            if (self.books[i].title != book.title
                and self.books[i].author != book.author):
                res_books.append(self.books[i])
        self.books = res_books

    def search_books(self, search_string):
        fmt_str = search_string.lower()
        search_res = []
        for book in self.books:
            if (fmt_str in book.title.lower()
                or fmt_str in book.author.lower()):
                search_res.append(book)
        return search_res
