from car import Car
from driver import Driver

class Uber(Car):
    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Uber License: {self.license}, Driver: {self.driver.name}, Brand: {self.brand}, Model: {self.model}"