class Jedi:
    def __init__(self, **kwargs) -> None:
        self.__name = kwargs.get('name', None)
        self.__height = kwargs.get('height', 0)
        self.__title = kwargs.get('title', None)
        self.__side = kwargs.get('side', None)
        self.__light_saber = kwargs.get('light_saber', None)

    def __str__(self) -> str:
        return "\nName: {}\nHeight: {}\nTitle: {}\nSide: {}\nlight_saber: {}\n".format(
            self.__name, self.__height, self.__title, self.__side, self.__light_saber
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height in range(135, 203):
            self.__height = height
        else:
            raise ValueError('Incorrect growth')

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    @property
    def light_saber(self):
        return self.__light_saber

    @light_saber.setter
    def light_saber(self, value):
        self.__light_saber = value


if __name__ == "__main__":
    anakin_skywalker = Jedi(
        name='Anakin Skywalker',
        height=188,
        title='Jedi Knight',
        side='The bright side',
        light_saber='Blue',
    )
    anakin_skywalker.name = 'Darth Vader'
    anakin_skywalker.height = 202
    anakin_skywalker.title = 'The dark lord of the sith'
    anakin_skywalker.side = 'The dark side'
    anakin_skywalker.light_saber = 'Red'
    print(anakin_skywalker)

    anakin_skywalker.name = 'Young Anakin Skywalker'
    anakin_skywalker.height = 135
    anakin_skywalker.title = 'The Racer from Tatooine'
    anakin_skywalker.side = 'The bright side'
    anakin_skywalker.light_saber = None
    print(anakin_skywalker)
