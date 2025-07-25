class Person:
    def __init__(self, name):
        self.name = name



class Author(Person):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field



class Buyer(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email



class Publisher:
    def __init__(self, name, city):
        self.name = name
        self.city = city



class Book:
    total_books = 0  

    def __init__(self, title, price, genre, authors, publisher, buyers):
        self.title = title
        self.price = price
        self.genre = genre

        self.authors = authors if isinstance(authors, list) else [authors]
        self.buyers = buyers if isinstance(buyers, list) else [buyers]
        self.publisher = publisher

        Book.total_books += 1

    def get_author_count(self):
        return len(self.authors)

    def get_buyer_count(self):
        return len(self.buyers)

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def __str__(self):
        author_names = ", ".join(author.name for author in self.authors)
        buyer_names = ", ".join(buyer.name for buyer in self.buyers)
        publisher_info = f"{self.publisher.name} ({self.publisher.city})"
        return (
            f"Book: {self.title}\n"
            f"Genre: {self.genre}\n"
            f"Price: {self.price}\n"
            f"Authors: {author_names}\n"
            f"Publisher: {publisher_info}\n"
            f"Buyers: {buyer_names}\n"
        )


author1 = Author("Sadegh Hedayat", "Fiction")
author2 = Author("Jalal Al-e-Ahmad", "Social")


buyer1 = Buyer("Reza", "reza@mail.com")
buyer2 = Buyer("Zahra", "zahra@mail.com")


publisher1 = Publisher("hamedan nashr", "Tehran book")


book1 = Book("The Blind Owl", 14500, "Novel", [author1], publisher1, [buyer1])
book2 = Book("The School Principal", 300000, "Social", [author2], publisher1, [buyer1, buyer2])


print(book1)
print(book2)


print("Total number of books:", Book.get_total_books())