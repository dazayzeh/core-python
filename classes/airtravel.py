""" Model for air flights """


class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'first two digits should contain an airline code {number}')
        if not number[2:].isdigit():
            raise ValueError(f'invalid rout number {number}')
        if not number[:2].isupper():
            raise ValueError(f'invalid code {number}')
        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


class Aircraft:

    def __init__(self, reg, model, rows, seats_per_row):
        self._reg = reg
        self._model = model
        self._rows = rows
        self._seats_per_row = seats_per_row

    def reg(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return ((range(1, self._rows + 1)
                 , 'ABCDEFG'[:self._seats_per_row]))
