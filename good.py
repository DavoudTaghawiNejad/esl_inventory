

class Good:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def valutation(self, parameters):
        return parameters[('price', self.name)] * self.quantity

