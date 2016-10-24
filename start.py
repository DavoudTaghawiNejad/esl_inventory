from pprint import pprint
from inventory import Inventory
from good import Good
from contract import Contract
from pulloption import PullOption
from bond import Bond


inventroy = Inventory()
inventroy.add(Good('cookies'), 10)
pprint(inventroy.inventory)
inventroy.add(PullOption(execution_price=5, underlying='intel'), 1)
pprint(inventroy.inventory)
inventroy.add(Bond(0, num_payments=10, value_payments=1, value_maturity=10), 1)
inventroy.add(Bond(0, num_payments=100, value_payments=-1, value_maturity=-100), 1)
pprint(inventroy.inventory)


scenario = {('price', 'cookies'): 1,
            ('price', 'intel'): 7,
            'interestrate': 0.01}
print('assetvalue')
pprint(inventroy.assetvalue(scenario))

print('assets')
pprint(inventroy.valued_assets(scenario))


print('liablities')
pprint(inventroy.valued_liablities(scenario))

inventroy.remove(Good('cookies'), 5)
print('remove 5 cookies')
print('assets')
pprint(inventroy.valued_assets(scenario))

