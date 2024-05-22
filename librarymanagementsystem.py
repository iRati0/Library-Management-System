class Book:
    def __init__(self, author, title, isbn):
        self.author = author
        self.title = title
        self.isbn = isbn


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, author, title, isbn):
        book = Book(author, title, isbn)
        self.books.append(book)

    def display(self):
        print("Library:")
        for i, book in enumerate(self.books):
            print(f"{i + 1}. {book.author}, {book.title}, {book.isbn}")

    def bubble_sort(self):
        n = len(self.books)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.books[j].author > self.books[j + 1].author:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]
                elif self.books[j].title > self.books[j + 1].title:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]
                elif self.books[j].isbn > self.books[j + 1].isbn:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]

    def binary_search(self, author, title, isbn):
        self.bubble_sort()
        low = 0
        high = len(self.books) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.books[mid].author == author:
                return self.books[mid]
            elif self.books[mid].author < author:
                low = mid + 1

                if self.books[mid].title == title:
                    return self.books[mid]
                elif self.books[mid].title < title:
                    low = mid + 1

                if self.books[mid].isbn == isbn:
                    return self.books[mid]
                elif self.books[mid].isbn < isbn:
                    low = mid + 1
            else:
                high = mid - 1
        return None


def main():
    library = Library()

    while True:
        print("*****Library Management System*****")
        print("1. Add Book to the Library")
        print("2. Display Library")
        print("3. Sort Books by title")
        print("4. Search for Books")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            author = input("Enter the Author of the Book: ")
            title = input("Enter the Title of the Book: ")
            isbn = input("Enter the ISBN of the Book: ")
            library.add_book(author, title, isbn)
            print("Book added to the Library.")
        elif choice == '2':
            library.display()
        elif choice == '3':
            library.bubble_sort()
        elif choice == '4':
            print("Search Criteria")
            print("1. Search by Author")
            print("2. Search by Title")
            print("3. Search by ISBN")
            user_search = input("Enter search criteria: ")
            if user_search == '1':
                author = input("Enter the Author of the Book: ")
                book_search = library.binary_search(author)
                if book_search:
                    print("Author found:")
                    print(f"Author: {book_search.author}")
                    print(f"Title: {book_search.title}")
                    print(f"ISBN: {book_search.isbn}")
                else:
                    print("Book not found")
                    if user_search == '2':
                        title = input("Enter the Title of the Book: ")
                        book_search = library.binary_search(title)
                        if book_search:
                            print("Title found:")
                            print(f"Author: {book_search.author}")
                            print(f"Title: {book_search.title}")
                            print(f"ISBN: {book_search.isbn}")
                        else:
                            print("Book not found")
                            if user_search == '3':
                                isbn = input("Enter the ISBN of the Book: ")
                                book_search = library.binary_search(isbn)
                                if book_search:
                                    print("ISBN found:")
                                    print(f"Author: {book_search.author}")
                                    print(f"Title: {book_search.title}")
                                    print(f"ISBN: {book_search.isbn}")
                                else:
                                    print("Book not found")
        elif choice == '5':
            print("Exiting Program...")
            break
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()
