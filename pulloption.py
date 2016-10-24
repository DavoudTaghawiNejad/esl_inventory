from contract import Contract


class PullOption(Contract):
    def __init__(self, type, state, execution_price, underlying):
        self.execution_price = execution_price
        self.underlying = underlying
        Contract.__init__(self, type, state)


    def valutation(self, parameters):
        return max(0, parameters[('price', self.underlying)] - self.execution_price)
