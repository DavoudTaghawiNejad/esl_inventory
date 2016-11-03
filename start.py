from pprint import pprint
from inventory import Inventory
from good import Good
from contract import Contract
from pulloption import PullOption
from bond import Bond
from valutation import usgap


inventory = Inventory()
print('add cookies')
cookies = Good('cookies', 5)
inventory.add(cookies)
pprint(inventory.goods)
print('add more cookies')
cookies2 = Good('cookies', 5)
inventory.add(cookies2)
pprint(inventory.goods)
print('remove 5 cookies')
inventory.remove(cookies)
pprint(inventory.goods)
inventory.add(PullOption(execution_price=5, underlying='intel'))
pprint(inventory.contracts)
bond1 = Bond(0, num_payments=10, value_payments=1, value_maturity=10)
inventory.add(bond1)
inventory.add(Bond(0, num_payments=100, value_payments=-1, value_maturity=-100))
pprint(inventory.contracts)


scenario = {('price', 'cookies'): 1,
            ('price', 'intel'): 7,
            'interestrate': 0.01}

print('assets')
pprint(inventory.valued_assets(scenario, usgap))


print('liablities')
pprint(inventory.valued_liablities(scenario, usgap))


print('assets')
pprint(inventory.valued_assets(scenario, usgap))

print('assetvalue')
print('pay one out of two bonds')
pprint(inventory.assetvalue(scenario, usgap))
print('valutation of bond1')
print(bond1.valutation(scenario, usgap))
bond1.pay()
print('bond and asset value after bond1 is payed')
print(bond1.valutation(scenario, usgap[Bond]))
pprint(inventory.assetvalue(scenario, usgap))

