from car import Car
from driver import Driver
from uber import Uber
from user import User

if __name__ == "__main__":
    print("Initializing car info")
    
    driver = Driver("Ariela Guerrero", "06760974-3", "ariguerrero@gmail.com", "atex345")
    car = Car("P3N13F", driver)
    print(car)
    print(car.driver)

    print("Uber")
    uber_driver = Driver("Juan Carlos", "06760974-3", "carlosmartinez@gmail.com", "carlos123")
    uber = Uber("UBER39F1385", uber_driver, "Kia", "Soul")
    print(uber)
    print(uber.driver)

    print("User")
    user = User("Caleb Ortiz", "07626534-3", "calebortiz288@gmail.com", "091023")
    print(user)