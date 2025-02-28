# bike.py
from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        """Displays bike details including engine capacity"""
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}cc")
