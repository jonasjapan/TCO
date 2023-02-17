"""Module used to calculate TCO for cars specified in yaml files
    """
import yaml  # pylint: disable=import-error
from car import Car


def main() -> None:
    """main function"""
    mycar: Car = Car("test_car")
    print(mycar)
    with open("./configs/test_car.yaml", encoding="utf-8") as stream:
        mycar2 = yaml.safe_load(stream)
    print(mycar2)


if __name__ == "__main__":
    main()
