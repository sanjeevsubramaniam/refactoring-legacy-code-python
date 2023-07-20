import typing
from Rental import Rental
from Furniture import Furniture


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.rentals: typing.List[Rental] = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        total_amount: float = 0
        frequent_renter_points: int = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for each in self.rentals:
            this_amount: float = 0
            if each.get_furniture().get_price_code() == Furniture.REGULAR:
                this_amount += 200
                if each.get_days_rentedays() > 2:
                    this_amount += (each.get_days_rentedays() - 2) * 150
            if each.get_furniture().get_price_code() == Furniture.NEW_LAUNCH:
                this_amount += each.get_days_rented() * 300
            if each.get_furniture().get_price_code() == Furniture.CHILDREN:
                this_amount += 150
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rentedays() - 3) * 150
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two days new launch rental
            if each.get_furniture().get_price_code() == Furniture.NEW_LAUNCH and each.get_days_rented() > 1:
                frequent_renter_points += 1
            # show figures for this rental
            result += "\t" + each.get_furniture().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add  footer lines result
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result;

