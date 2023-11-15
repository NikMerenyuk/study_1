# TASK 2
#
class Book:

    def __init__(self, book_name: str, year: int, publisher: str, genre: str, author: str, cost: float):
        self.set_book_name(book_name)
        self.set_year(year)
        self.set_publisher(publisher)
        self.set_genre(genre)
        self.set_author(author)
        self.set_cost(cost)

    def set_book_name(self, book_name):
        self.book_name = book_name

    def get_book_name(self):
        return self.book_name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def __str__(self):
        return (f'Book name: {self.book_name}\n'
                f'Year: {self.year}\n'
                f'Publisher: {self.publisher}\n'
                f'Genre: {self.genre}\n'
                f'Author: {self.author}\n'
                f'Cost: {self.cost}\n')


book_1 = Book('The House of Hades', 2013, 'Disney-Hyperion Books', 'Fantasy', 'Rick Riordan', 4.5)
print(book_1)
print(book_1.get_book_name())
book_1.set_book_name('Persey Jackson')
print(book_1.get_book_name())
print(book_1.get_cost())
book_1.set_cost(2.2)
print(book_1.get_cost())
print(book_1)


# TASK 3
#
# class Stadium:
#
#     def __init__(self, stadium_name, opened_date, country, city, capacity):
#         self.set_stadium_name(stadium_name)
#         self.set_opened_date(opened_date)
#         self.set_country(country)
#         self.set_city(city)
#         self.set_capacity(capacity)
#
#     def set_stadium_name(self, stadium_name):
#         self.stadium_name = stadium_name
#
#     def get_stadium_name(self):
#         return self.stadium_name
#
#     def set_opened_date(self, opened_date):
#         self.opened_date = opened_date
#
#     def get_opened_date(self):
#         return self.opened_date
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_capacity(self, capacity):
#         self.capacity = capacity
#
#     def get_capacity(self):
#         return self.capacity
#
#     def __str__(self):
#         return (f'Stadium name: {self.stadium_name}\n'
#                 f'Opened date: {self.opened_date}\n'
#                 f'Country: {self.country}\n'
#                 f'City: {self.city}\n'
#                 f'Capacity: {self.capacity}')
#
#
# stadium_1 = Stadium('Stadium of Light', '1997', 'England', 'Sunderland', 49000)
# print(stadium_1)
