from Furniture import Furniture


class Rental:
    def __init__(self, furniture: Furniture, days_rented: int):
        self.furniture = furniture
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_furniture(self):
        return self.furniture
