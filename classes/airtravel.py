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
        self._seating = [None] + [ { l : None for l in seats} for _ in rows]   # throw first row because it starts at zero

    def allocate_seat(self, seat, customer_name):
        row, seat_letter = self._parse_seat(seat)

        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"seat {seat} already taken")

        self._seating[row][seat_letter] = customer_name

    def _parse_seat(self, seat):
        rows, seats_letter = self._aircraft.seating_plan()

        seat_letter = seat[-1]
        row = seat[:-1]

        if seat_letter not in seats_letter:
            raise ValueError(f"invalid seat letter {seats_letter}")
        if row not in rows:
            raise ValueError(f"invalid row letter {row}")

        return row, seat_letter

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
