from account import Account

class Car:
    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

    def __str__(self):
        return f"Car License: {self.license}, Driver: {self.driver.name}"