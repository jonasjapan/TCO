"""Module containing the class Car
"""


class Car:
    """Class to hold parameters and functions of a car"""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.brand: str = ""

    def __str__(self) -> str:
        return f"car named: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()
