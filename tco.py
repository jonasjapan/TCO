"""Module used to calculate TCO for cars specified in yaml files
    """
from typing import List, Union
import yaml  # pylint: disable=import-error


def total_service(services: List[int]) -> int:
    """Calculates total service cost for the car

    Args:
        services (List[int]): all expected services

    Returns:
        int: total cost
    """
    return sum(services)


def total_tax(tax: int, years: int) -> int:
    """Calculates total tax cost for the car

    Args:
        tax (int): yearly tax value
        years (int): number of years

    Returns:
        int: total tax
    """
    return tax * years


def validate_yaml(car: dict[str, Union[str, int, List[int]]]):
    """Ensures the car config read adheres to some rules expected by the rest of the program

    Args:
        car (dict[str, Union[str, int, List[int]]]): the complete car from yaml file

    Returns:
        _type_: 1 if all is ok, else -1
    """
    if len(car["services"]) != car["years_to_own"]:
        return -1
    return 1


def main() -> None:
    """main function"""
    with open("./configs/test_car.yaml", encoding="utf-8") as stream:
        mycar2 = yaml.safe_load(stream)
    if validate_yaml(mycar2) == -1:
        raise ValueError("Something wrong in the yaml")


if __name__ == "__main__":
    main()
