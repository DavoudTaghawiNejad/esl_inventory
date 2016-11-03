from bond import Bond
from pulloption import PullOption


def value_bond(bond, parameters):
    i = parameters['interestrate']
    N = bond.num_payments - bond.state
    return bond.value_payments * ((1 - ((1 + i) ** (- N))) / i) + bond.value_maturity * (1 + i) ** (- N)


def value_pulloption(po, parameters):
    return max(0, parameters[('price', po.underlying)] - po.execution_price)

usgap = {Bond: value_bond,
         PullOption: value_pulloption}
