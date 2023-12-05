class Computer:
    def __init__(self):
        self.components = {}

    def add_components(self, key, value):
        self.components[key] = value

    def __str__(self):
        return f'Computer with component: {self.components}'


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_processor(self, processor):
        self.computer.add_components('processor', processor)
        return self

    def configure_ram(self, ram):
        self.computer.add_components('ram', ram)
        return self

    def configure_graphics_card(self, graphics_card):
        self.computer.add_components('graphics_card', graphics_card)
        return self

    def configure_motherboard(self, motherboard):
        self.computer.add_components('motherboard', motherboard)
        return self

    def configure_hdd(self, hdd):
        self.computer.add_components('hdd', hdd)
        return self

    def configure_ssd(self, ssd):
        self.computer.add_components('ssd', ssd)
        return self

    def configure_computer_case(self, computer_case):
        self.computer.add_components('computer_case', computer_case)
        return self

    def configure_power_supply_unit(self, power_supply_unit):
        self.computer.add_components('power_supply_unit', power_supply_unit)
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
computer_1 = (builder
              .configure_processor('Intel Core i3')
              .configure_ram('32GB')
              .configure_graphics_card('NVIDIA GeForce RTX 4060')
              .configure_motherboard('MSI PRO B760M-G')
              .configure_hdd('4TB Seagate BarraCuda')
              .configure_ssd('512GB ADATA XPG SX8200 Pro')
              .configure_computer_case('MSI MAG FORGE M100A')
              .configure_power_supply_unit('500W Deepcool PK500D')
              .build())


if __name__ == '__main__':
    print(computer_1)
