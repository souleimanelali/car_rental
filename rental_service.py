# rental_service.py
from car import Car
from bike import Bike

def show_vehicle_info(vehicle):
    """Demonstrates polymorphism by calling display_info() of any vehicle object"""
    vehicle.display_info()
    print("-" * 40)

def rental_menu():
    """Recursive menu system"""
    print("\nWelcome to Bob's Car Rental Service!")
    print("1. View Vehicles")
    print("2. Calculate Rental Cost")
    print("3. Modify Rental Price")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_vehicle_info(car)
        show_vehicle_info(bike)
    elif choice == "2":
        days = int(input("Enter number of rental days: "))
        print(f"Rental cost for {car.brand} {car.model} for {days} days: ${car.calculate_rental_cost(days)}")
        print(f"Rental cost for {bike.brand} {bike.model} for {days} days: ${bike.calculate_rental_cost(days)}")
    elif choice == "3":
        new_price = int(input(f"Enter new rental price for {car.brand} {car.model}: "))
        car.set_rental_price(new_price)
        print(f"Updated rental price for {car.brand} {car.model}: ${car.get_rental_price()}/day")
    elif choice == "4":
        print("Thank you for using Bob's Car Rental Service!")
        return
    else:
        print("Invalid choice! Please try again.")

    rental_menu()  # Recursively call menu function

# Create Car and Bike instances
car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)

# Start the rental service menu
rental_menu()