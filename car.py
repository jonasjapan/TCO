"""a module containing a class representation of a car
"""

import yaml  # pylint: disable=import-error


class Car:
    """A class to hold propperties of a car object"""

    def __init__(self, yaml_file: str) -> None:
        self.yaml = yaml_file
        self.name = ""
        self.brand = ""
        self.price = ""
        self.populate_from_yaml()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return self.generate_print_string()

    def populate_from_yaml(self):
        """called during init to set all properties based on yaml file"""
        with open(self.yaml, encoding="utf-8") as stream:
            car_dict = yaml.safe_load(stream)
        for key in car_dict:
            setattr(self, key, car_dict[key])

    def generate_print_string(self) -> str:
        """Creates a string representation of the car object

        Returns:
            str: a string representation of the car
        """
        print_string: str = "Car instance \n"
        print_string += f"name: {self.name}\n"
        print_string += f"brand: {self.brand}\n"
        price_formated = f"{self.price:,}"
        price_formated = price_formated.replace(",", " ")
        print_string += f"cost: {price_formated} sek\n"
        return print_string
