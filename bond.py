from contract import Contract

class Bond(Contract):
    def __init__(self, state, num_payments, value_payments, value_maturity):
        self.value_payments = value_payments
        self.value_maturity = value_maturity
        self.num_payments = num_payments
        self.state = state

    def pay(self):
        if self.state == self.num_payments:
            return 0
        self.state += 1
        if self.state == self.num_payments:
            return self.value_maturity + self.value_payments
        else:
            return self.value_payments

    def valutation(self, parameters):
        i = parameters['interestrate']
        N = self.num_payments - self.state
        return self.value_payments * ((1 - ((1 + i) ** (- N))) / i) + self.value_maturity * (1 + i) ** (- N)

