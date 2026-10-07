# 1. Define the Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"The engine of the {self.brand} {self.model} is now running."

# 2. Define the Child Class that inherits from Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        # Use super() to initialize attributes from the parent class
        super().__init__(brand, model)
        # Add a unique attribute specific to the child class
        self.battery_capacity = battery_capacity

    # Overriding the parent method to customize behavior
    def start_engine(self):
        return f"The {self.brand} {self.model} silently powers on. (Battery: {self.battery_capacity} kWh)"
    
    # A unique method only available to the child class
    def charge_battery(self):
        return f"Charging the {self.brand}..."