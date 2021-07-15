# ==========================
# =======  Задание 1 =======
# ==========================

class Car:
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand', None)
        self.model = kwargs.get('model', None)
        self.year = kwargs.get('year', None)
        self.engine_volume = kwargs.get('engine_volume', None)
        self.color = kwargs.get('color', None)
        self.price = kwargs.get('price', 0.0)

    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


if __name__ == "__main__":
    octavia = Car(
        brand='Skoda',
        model='New Octavia',
        year=2020,
        engine_volume='2.0',
        color='blue',
        price='20000$',
    )
    print(octavia)

if __name__ == "__main__":
    kodiaq = Car(
        brand='Skoda',
        model='Kodiaq',
        year=2020,
        engine_volume='1.4',
        color='white',
        price='21614$',
    )
    print(kodiaq)


if __name__ == "__main__":
    superb = Car(
        brand='Skoda',
        model='Superb',
        year=2021,
        engine_volume='2.0',
        color='black',
        price='36650$',
    )
    print(superb)

print('---------------------------------------------------')

# ==========================
# =======  Задание 2 =======
# ==========================


class Book:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.year = kwargs.get('year', None)
        self.author = kwargs.get('author', None)
        self.genre = kwargs.get('genre', None)
        self.price = kwargs.get('price', 0.0)

    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_price(self):
        return self.price

    def set_name(self):
        self.name = name

    def set_year(self):
        self.year = year

    def set_author(self):
        self.author = author

    def set_genre(self):
        self.genre = genre

    def set_price(self):
        self.price = price


if __name__ == "__main__":
    sword_of_destiny = Book(
        name='Sword of Destiny',
        year=1992,
        author='Andzhey Sapkovsky',
        genre='fantasy',
        price='7,01$',
    )
    print(sword_of_destiny)

if __name__ == "__main__":
    last_wish = Book(
        name='Last wish',
        year=1993,
        author='Andzhey Sapkovsky',
        genre='fantasy',
        price='6,87$',
    )
    print(last_wish)

if __name__ == "__main__":
    elven_blood = Book(
        name='Elven blood',
        year=1994,
        author='Andzhey Sapkovsky',
        genre='fantasy',
        price='6,53$',
    )
    print(elven_blood)

print('---------------------------------------------------')

# ==========================
# =======  Задание 3 =======
# ==========================


class Stadium:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.year = kwargs.get('year', None)
        self.country = kwargs.get('country', None)
        self.city = kwargs.get('city', None)
        self.capacity = kwargs.get('capacity', 0.0)

    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self):
        self.name = name

    def set_year(self):
        self.year = year

    def set_country(self):
        self.country = country

    def set_city(self):
        self.city = city

    def set_capacity(self):
        self.capacity = capacity


if __name__ == "__main__":
    tottenham_hotspur = Stadium(
        name='Tottenham Hotspur Stadium',
        year=2019,
        country='UK',
        city='London',
        capacity='62 062',
    )
    print(tottenham_hotspur)

if __name__ == "__main__":
    ferenc_puskas = Stadium(
        name='Ferenc Puskas',
        year=2019,
        country='Hungary',
        city='Budapest',
        capacity='67 215',
    )
    print(ferenc_puskas)

if __name__ == "__main__":
    allianz_arena = Stadium(
        name='Allianz Arena',
        year=2005,
        country='Germany',
        city='Munich',
        capacity='75 024',
    )
    print(allianz_arena)

print('---------------------------------------------------')
