class Devise:
    def __init__(self, brand='', model='', application='', power=0, endurance_rotation=0, price=0):
        self.destination = ''
        self.brand = brand
        self.model = model
        self.application = application
        self.power = power
        self.endurance_rotation = endurance_rotation
        self.price = price

    def __str__(self) -> str:
        return "\nbrand: {}\nmodel: {}\napplication: {}\npower: {}\nendurance_rotation: {}\n".format(
            self.brand, self.model, self.application, self.power, self.endurance_rotation
        )

    def description(self):
        print(f'{self.destination}')

    def prepayment_price(self):
        print(f'The cost of the device {self.brand} {self.model} is {self.price}$')

    def credit_price(self):
        credit = self.price * 1.3
        print(f'If you want to buy a device {self.brand} {self.model} is credit the cost will be {credit}$')


class Blender(Devise):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'Blender. Designed for shredding fruits and vegetables, smoothies.'


class CoffeeMachine(Devise):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'Coffee machine. Designed for the preparation of aromatic coffee, cappuccino, latte.'


class MeatGrinder(Devise):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = 'Mincer. Designed for the preparation of minced meat.'


if __name__ == "__main__":
    philips_hr3752 = Blender(
        brand='Philips',
        model='HR3752/00',
        application='For the kitchen',
        power=1400,
        endurance_rotation=35000,
        price=355
    )
    philips_hr3752.description()
    print(philips_hr3752)
    philips_hr3752.prepayment_price()
    philips_hr3752.credit_price()
    print('==================================================')

if __name__ == "__main__":
    delonghi_ECAM22 = CoffeeMachine(
        brand='DeLonghi',
        model='ECAM22.360.S',
        application='For the kitchen and office',
        power=1400,
        endurance_rotation=40000,
        price=734
    )
    delonghi_ECAM22.description()
    print(delonghi_ECAM22)
    delonghi_ECAM22.prepayment_price()
    delonghi_ECAM22.credit_price()
    print('==================================================')

if __name__ == "__main__":
    moulinex_ME688832 = MeatGrinder(
        brand='Moulinex',
        model='ME688832',
        application='For the kitchen',
        power=2200,
        endurance_rotation=30000,
        price=290
    )
    moulinex_ME688832.description()
    print(moulinex_ME688832)
    moulinex_ME688832.prepayment_price()
    moulinex_ME688832.credit_price()
    print('==================================================')
