from contract import Contract


class Good(Contract):
    def __init__(self, type):
        self.type = type
        self.state = 'good'

    def valutation(self, parameters):
        return parameters[('price', self.type)]
