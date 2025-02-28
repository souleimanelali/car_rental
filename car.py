# car.py
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        """Displays car details including seating capacity"""
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity}")
