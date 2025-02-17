from account import Account

class Driver(Account):
    def __init__(self, name, document, email, password):
        super().__init__(name, document, email, password)

    def __str__(self):
        return f"Driver: {self.name}, Document: {self.document}, Email: {self.email}"