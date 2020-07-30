""" Model for air flights """


class Flight:

    def __init(self, number):
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
