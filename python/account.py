class Account:
    def __init__(self, name, document, email, password):
        self.name = name
        self.document = document
        self.email = email
        self.password = password

    def __str__(self):
        return f"Account: {self.name}, Document: {self.document}, Email: {self.email}"