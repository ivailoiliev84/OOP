import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = str(name)
        self.id = int(id)
        self.creation_year = int(creation_year)
        self.creation_month = str(creation_month)
        self.age_restriction = int(age_restriction)
        self.is_rented = False

    def int_to_mount(mount: int):
        mount_srt = datetime.date(1900, int(mount), 1).strftime("%B")
        return mount_srt

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        month = cls.int_to_mount(month)
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {rented}"


