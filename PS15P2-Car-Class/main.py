class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return 0.9 * self.sticker_price

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Sticker Price: ${self.sticker_price:.2f}")

class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.updated_price = self.discount_price()  # Start with the discounted price

    def pricewithoptions(self):
        print(f"\nUpdated Price with Options: ${self.updated_price:.2f}")

    def SportWheels(self, option='N'):
        if option == 'Y':
            self.updated_price += 1000.00

    def SportEngine(self, option='N'):
        if option == 'Y':
            self.updated_price += 3000.00

    def SportInterior(self, option='N'):
        if option == 'Y':
            self.updated_price += 2000.00

# Program to instantiate the S
