class ShoesModel:
    def __init__(self, shoes_type, shoes_style, color, cost, manufacturer, size):
        self.shoes_type = shoes_type
        self.shoes_style = shoes_style
        self.color = color
        self.cost = cost
        self.manufacturer = manufacturer
        self.size = size


class ShoesView:
    @staticmethod
    def display_shoes(shoes):
        print(f'Shoes type: {shoes.shoes_type};\n'
              f'Shoes style: {shoes.shoes_style};\n'
              f'Color: {shoes.color};\n'
              f'Cost: {shoes.cost};\n'
              f'Manufacturer: {shoes.manufacturer};\n'
              f'Size: {shoes.size}.')


class ShoesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_shoes_type(self, shoes_type):
        self.model.shoes_type = shoes_type

    def set_shoes_style(self, shoes_style):
        self.model.shoes_style = shoes_style

    def set_shoes_color(self, color):
        self.model.color = color

    def set_shoes_cost(self, cost):
        self.model.cost = cost

    def set_shoes_manufacturer(self, manufacturer):
        self.model.manufacturer = manufacturer

    def set_shoes_size(self, size):
        self.model.size = size

    def display_shoes(self):
        self.view.display_shoes(self.model)


model = ShoesModel('men', 'boot', 'black', '120', 'bootshoes company', '44')
view = ShoesView()
controller = ShoesController(model, view)


if __name__ == '__main__':
    controller.display_shoes()
