from typing_extensions import Protocol


class Cars:
    def __init__(self, model, make, year):
        self.model = "Ford"
        self.make = "Mustang"
        self.year = "2021"

    def print_model (self):
        print(self.model)

    def print_make_year (self, make, year):
        print(make)
        print(year)

my_cars = Cars("chevy", "forester", "1987")

print(my_cars.model)


