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
        self._seating = [None] + [{l: None for l in seats} for _ in rows]  # throw first row because it starts at zero

    def allocate_seat(self, seat, customer_name):
        """Locate a customer in a seat if available

        :param seat: the chosen seat
        :param customer_name: the customer name
        """
        row, seat_letter = self._parse_seat(seat)

        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"seat {seat} already taken")

        self._seating[row][seat_letter] = customer_name

    def relocate_seat(self, from_seat, to_seat):
        """Relocate customers to a different seat

        :param from_seat: the current occupied seat
        :param to_seat: the new seat
        """
        from_row, from_seat_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_seat_letter] is None:
            raise ValueError(f'no customer to relocate in seat {from_seat}')

        to_row, to_seat_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_seat_letter] is not None:
            raise ValueError(f'seat {to_seat} is already taken')

        self._seating[to_row][to_seat_letter] = self._seating[from_row][from_seat_letter]
        self._seating[from_row][from_seat_letter] = None

    def _parse_seat(self, seat):  # the name starts with underscore because it describes implementation details
        """ check if a given seat exists

        :param seat: the desired seat to parse
        :return: a tuple of the seat row and letter
        """
        rows, seats_letter = self._aircraft.seating_plan()

        seat_letter = seat[-1]
        row = seat[:-1]

        if seat_letter not in seats_letter:
            raise ValueError(f"invalid seat letter {seats_letter}")
        if row not in rows:
            raise ValueError(f"invalid row letter {row}")

        return row, seat_letter

    def number_of_available_seats(self):
        return sum(  # get the sum of all sums
            sum(1 for seat in row.values() if seat is None)  # generator expression to add 1 for each available row
            for row in self._seating  # access each row in the list
            if row is not None  # if not first row because we defined it as None
        )


class Aircraft:

    def __init__(self, reg):
        self._reg = reg

    def reg(self):
        return self._reg

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class FakeAirFlight300(Aircraft):

    def seating_plan(self):
        return range(1, 20), "ABCDEFG"

    def model(self):
        return "FakeAirFlight 300"


class FakeAirFlight900(Aircraft):

    def model(self):
        return "FakeAirFlight 900"

    def seating_plan(self):
        return range(1, 30), "ABCD"
