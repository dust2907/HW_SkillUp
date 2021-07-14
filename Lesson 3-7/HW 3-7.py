# ==========================
# =======  Задание 1 =======
# ==========================

class Car:
    def __init__(self, model, year, engine_volume, color, price):
        self.brand = 'Skoda'
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def cars(self):
        return f'This is great car {self.brand} - {self.model}, {self.year} year of ' \
               f'release. Volume engine {self.engine_volume}, color is {self.color}. Price {self.price}'


octavia = Car(
    model='New Octavia',
    year=2020,
    engine_volume='2.0',
    color='blue',
    price='20000$',
)


kodiaq = Car(
    model='Kodiaq',
    year=2020,
    engine_volume='1.4',
    color='white',
    price='21614$',
)


superb = Car(
    model='Superb',
    year=2021,
    engine_volume='2.0',
    color='black',
    price='36650$',
)


print(octavia.cars())
print(kodiaq.cars())
print(superb.cars())

print('---------------------------------------------------')

# ==========================
# =======  Задание 2 =======
# ==========================


class Book:
    def __init__(self, name, year, author, genre, price):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.price = price

    def books(self):
        return f'The book you are interested in is called {self.name}, it is a {self.year} ' \
               f'release, the {self.genre} genre, by {self.author} and this book costs {self.price}.' \
               f' Do you want to buy it?'


sword_of_destiny = Book(
    name='Sword of Destiny',
    year=1992,
    author='Andzhey Sapkovsky',
    genre='fantasy',
    price='7,01$',
)

last_wish = Book(
    name='Last wish',
    year=1993,
    author='Andzhey Sapkovsky',
    genre='fantasy',
    price='6,87$',
)

elven_blood = Book(
    name='Elven blood',
    year=1994,
    author='Andzhey Sapkovsky',
    genre='fantasy',
    price='6,53$',
)

print(sword_of_destiny.books())
print(last_wish.books())
print(elven_blood.books())
print('---------------------------------------------------')

# ==========================
# =======  Задание 3 =======
# ==========================


class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def stadiums(self):
        return f' {self.name} stadium is located in {self.city}, {self.country},' \
               f' built in {self.year} and has a capacity of {self.capacity} spectators.' \
               f' This is a great place to spend your free time!'


tottenham_hotspur = Stadium(
    name='Tottenham Hotspur Stadium',
    year=2019,
    country='UK',
    city='London',
    capacity='62 062',
)

ferenc_puskas = Stadium(
    name='Ferenc Puskas',
    year=2019,
    country='Hungary',
    city='Budapest',
    capacity='67 215',
)

allianz_arena = Stadium(
    name='Allianz Arena',
    year=2005,
    country='Germany',
    city='Munich',
    capacity='75 024',
)

print(tottenham_hotspur.stadiums())
print(ferenc_puskas.stadiums())
print(allianz_arena.stadiums())
print('---------------------------------------------------')
