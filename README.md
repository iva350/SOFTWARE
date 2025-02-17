Account Class: This is the base class from which both drivers and users inherit. It contains attributes common to both entities, such as name, document, email, and password. Additionally, it defines an abstract printDetails() method that must be implemented by derived classes to print the specific details of each account type.

Driver and User classes: Both classes inherit from the Account class. The Driver class includes an additional attribute for storing the driver's license, while the User class adds an attribute for the phone number. Both implement the printDetails() method, which prints the relevant details of drivers and users, such as their name, email, and other corresponding attributes.

Car Class: This class represents a basic vehicle in the system. It contains attributes such as the license plate, the assigned driver, and the number of passengers it can carry. It also includes a printCarDetails() method that prints basic vehicle details, such as the license plate and passenger capacity.

UberX class: This class inherits from the Car class and adds additional details specific to UberX vehicles, such as the make and model of the car. Override the printCarDetails() method to include these new attributes, providing more details about the vehicle.

Main Class: In this class, objects of type User, Driver and UberX are instantiated, simulating a scenario where users, drivers and vehicles are created, and then the details of each one are printed. This demonstrates how the classes of the system interact with each other.