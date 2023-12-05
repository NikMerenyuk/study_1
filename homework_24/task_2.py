class AbstractFactory:
    def create_carbonara(self):
        raise NotImplemented

    def create_bolognaise(self):
        raise NotImplemented

    def create_puttanesca(self):
        raise NotImplemented


class PastaFactory(AbstractFactory):
    def create_carbonara(self):
        return Carbonara('spaghetti', 'carbonara', 'beacon', 'parmesan')

    def create_bolognaise(self):
        return Bolognaise('spaghetti', 'bolognaise', 'ground beef', 'parmesan')

    def create_puttanesca(self):
        return Puttanesca('spaghetti', 'puttanesca', 'tomato and olives', 'chili and parmesan')


class Carbonara:
    def __init__(self, pasta_type, sauce, topping, additives):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.topping = topping
        self.additives = additives

    def __str__(self):
        return (f'\nCarbonara consists of:\n'
                f'Pasta type: {self.pasta_type};\n'
                f'Sauce: {self.sauce};\n'
                f'Topping: {self.topping};\n'
                f'Additives: {self.additives}.')


class Bolognaise:
    def __init__(self, pasta_type, sauce, topping, additives):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.topping = topping
        self.additives = additives

    def __str__(self):
        return (f'\nBolognaise consists of:\n'
                f'Pasta type: {self.pasta_type};\n'
                f'Sauce: {self.sauce};\n'
                f'Topping: {self.topping};\n'
                f'Additives: {self.additives}.')


class Puttanesca:
    def __init__(self, pasta_type, sauce, topping, additives):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.topping = topping
        self.additives = additives

    def __str__(self):
        return (f'\nPuttanesca consists of:\n'
                f'Pasta type: {self.pasta_type};\n'
                f'Sauce: {self.sauce};\n'
                f'Topping: {self.topping};\n'
                f'Additives: {self.additives}.')


def test_pasta_factory_creation():
    factory = PastaFactory()

    assert isinstance(factory, AbstractFactory), "PastaFactory is not an instance of AbstractFactory"


def test_pasta_creation_by_factory():
    factory = PastaFactory()

    carbonara = factory.create_carbonara()
    bolognaise = factory.create_bolognaise()
    puttanesca = factory.create_puttanesca()

    assert isinstance(carbonara, Carbonara), 'Carbonara is not created by PastaFactory'
    assert isinstance(bolognaise, Bolognaise), 'Bolognaise is not created by PastaFactory'
    assert isinstance(puttanesca, Puttanesca), 'Puttanesa is not created by PastaFactory'


if __name__ == '__main__':

    test_pasta_factory_creation()
    test_pasta_creation_by_factory()

    print(PastaFactory().create_carbonara())
    print(PastaFactory().create_bolognaise())
    print(PastaFactory().create_puttanesca())
