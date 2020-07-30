""" Model for air flights """


class Flight:
    """A FLight with an aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'first two digits should contain an airline code {number}')
        if not number[2:].isdigit():
            raise ValueError(f'invalid rout number {number}')
        if not number[:2].isupper():
            raise ValueError(f'invalid code {number}')
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{l: None for l in seats} for _ in rows]   # throw first row because it starts at zero

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


class Aircraft:

    def __init__(self, reg, model, rows, seats):
        self._reg = reg
        self._model = model
        self._rows = rows
        self._seats = seats

    def reg(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return ((range(1, self._rows + 1)
                 , 'ABCDEFG'[:self._seats]))
