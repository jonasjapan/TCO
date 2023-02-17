from car import Car
import yaml


def main():
    mycar: Car = Car("test_car")
    print(mycar)
    with open("./configs/test_car.yaml", "r") as stream:
        mycar2 = yaml.safe_load(stream)
    print(mycar2)


if __name__ == "__main__":
    main()