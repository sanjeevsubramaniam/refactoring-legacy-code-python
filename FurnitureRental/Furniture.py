REGULAR = 0
NEW_LAUNCH = 1
CHILDREN = 2


class Furniture:
    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        return self.price_code

    def set_price_code(self, price_code: int):
        self.price_code = price_code

    def get_title(self):
        return self.title
