from contract import Contract


class PullOption(Contract):
    def __init__(self, execution_price, underlying):
        self.execution_price = execution_price
        self.underlying = underlying

