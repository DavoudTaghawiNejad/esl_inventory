from contract import Contract


class PullOption(Contract):
    def __init__(self, state, execution_price, underlying):
        self.execution_price = execution_price
        self.underlying = underlying
        Contract.__init__(self, state)


    def valutation(self, parameters):
        return max(0, parameters[('price', self.underlying)] - self.execution_price)
