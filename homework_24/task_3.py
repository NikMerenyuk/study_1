import copy


class Display:
    def __init__(self, firm, diagonal, matrix):
        self.firm = firm
        self.diagonal = diagonal
        self.matrix = matrix

    def __str__(self):
        return (f'Firm: {self.firm}; '
                f'Diagonal: {self.diagonal}"; '
                f'Matrix: {self.matrix}.')

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    original_display = Display('Asus', '23.8', 'OLED')
    print('Original display:', original_display)

    cloned_display = original_display.clone()
    print('Cloned display:', cloned_display)

    print(original_display == cloned_display)

