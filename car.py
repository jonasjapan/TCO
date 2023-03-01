"""a module containing a class representation of a car
"""


class Car:
    """A class to hold propperties of a car object"""

    def __init__(self, name: str, brand: str, price: int) -> None:
        self.name = name
        self.brand = brand
        self.cost = price

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return self.generate_print_string()

    def generate_print_string(self) -> str:
        """Creates a string representation of the car object

        Returns:
            str: a string representation of the car
        """
        print_string: str = "Car instance \n"
        print_string += f"name: {self.name}\n"
        return print_string
