class Guitar:
    def __init__(self, make, model, year, cost):
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} {} {}, retails for approximately ${}".format(self.year, self.make, self.model, self.cost)

    def get_age(self):
        from datetime import datetime
        # Reads current year (Used to check if a guitar is vintage)
        current_year = datetime.now().year
        guitar_age = current_year - self.year
        return guitar_age

    def is_vintage(self):
        if self.get_age() < 50:
            return False
        else:
            return True
