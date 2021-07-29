import datetime


class Customer:

    def __init__(self, name: str, age: int, id: int):
        self.name = str(name)
        self.age = int(age)
        self.id = int(id)
        self.rented_dvds = []

    def __repr__(self):
        dvds = ', '.join([dvd.name for dvd in self.rented_dvds])
        statistic = f"{self.id}: {self.name} of age {self.age} has " \
            f"{len(self.rented_dvds)} rented DVD's ({dvds})"
        return statistic
