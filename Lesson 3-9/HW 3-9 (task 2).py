class Ship:
    def __init__(self, name='', displacement=0, length=0, speed=0, crew=0, country=''):
        self.destination = ''
        self.name = name
        self.displacement = displacement
        self.length = length
        self.speed = speed
        self.crew = crew
        self.country = country

    def __str__(self) -> str:
        return "\nname: {}\ndisplacement: {}\nlength: {}\nspeed: {}\ncrew: {}\ncountry: {}\n".format(
            self.name, self.displacement, self.length, self.speed, self.crew, self.country
        )

    def description(self):
        print(f'{self.destination}')


class Frigate(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'A naval ship with a displacement of up to 4,000 tons. The speed is over 25 knots,' \
                           ' it is armed with anti-submarine and anti-aircraft missile systems'


class Cruiser(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'A combat surface ship capable of performing tasks independently of the main fleet'


class Corvette(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'Combat surface warship, designed for patrol and convoy service,' \
                           ' anti-submarine and anti-aircraft defense of naval bases.'


if __name__ == "__main__":
    knox = Frigate(
        name='Knox',
        displacement=4163,
        length=133,
        speed=27,
        crew=244,
        country='USA'
    )
    knox.description()
    print(knox)
    print('==================================================')

if __name__ == "__main__":
    mohawk = Cruiser(
        name='Mohawk',
        displacement=4700,
        length=128,
        speed=29,
        crew=255,
        country='Canada'
    )
    mohawk.description()
    print(mohawk)
    print('==================================================')

if __name__ == "__main__":
    type_056 = Corvette(
        name='Type 056',
        displacement=1300,
        length=88,
        speed=28,
        crew=60,
        country='China'
    )
    type_056.description()
    print(type_056)
    print('==================================================')
