# vehicle.py
class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        """Displays vehicle details"""
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        """Calculates the rental cost for given days"""
        return self.__rental_price_per_day * days

    # Getter method for rental_price_per_day
    def get_rental_price(self):
        return self.__rental_price_per_day

    # Setter method for rental_price_per_day
    def set_rental_price(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Price must be greater than zero.")
