from project.customer import Customer
from project.dvd import DVD

C_DVD_CAPACITY = 15
C_CUSTOMER_CAPACITY = 10


class MovieWorld:
    DVD_CAPACITY = C_DVD_CAPACITY
    CUSTOMER_CAPACITY = C_CUSTOMER_CAPACITY

    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return __class__.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return __class__.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> bool:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer: Customer = [c for c in self.customers if c.id == customer_id][0]
        dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd.id in [d.id for d in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer: Customer = [c for c in self.customers if c.id == customer_id][0]
        dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd.id in [d.id for d in customer.rented_dvds]:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        nl = "\n"
        result = '\n'.join(str(x) for x in self.customers)
        result += nl
        result += '\n'.join(str(x) for x in self.dvds)
        return result


