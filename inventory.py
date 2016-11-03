from abce import NotEnoughGoods
from copy import copy
from good import Good

class Inventory:
    def __init__(self):
        self.contracts = set()
        self.goods = {}

    def add(self, entry):
        if isinstance(entry, Good):
            try:
                self.goods[entry.name] += entry.quantity
            except KeyError:
                self.goods[entry.name] = entry.quantity
        else:
            assert entry not in self.contracts
            self.contracts.add(entry)

    def remove(self, entry):
        if isinstance(entry, Good):
            try:
                if entry.quantity > self.goods[entry.name]:
                    raise NotEnoughGoods
                self.goods[entry.name] -= entry.quantity
            except KeyError:
                raise NotEnoughGoods
        else:
            self.contracts.remove(entry)

    def netvalue(self, parameters, usgap):
        return (sum(usgap[entry.__class__](entry, parameters) for entry in self.contracts)
                + sum(quantity * parameters['good_prices'][name] for name, quantity in self.goods.items()))

    def assetvalue(self, parameters, usgap):
        return (sum(max(usgap[entry.__class__](entry, parameters), 0)for entry in self.contracts)
                + sum(quantity * parameters[('price', name)]
                      for name, quantity in self.goods.items()
                      if parameters[('price', name)] > 0))

    def liablityvalue(self, parameters, usgap):
        return (sum(min(usgap[entry.__class__](entry, parameters), 0)for entry in self.contracts)
                + sum(quantity * parameters[('price', name)]
                      for name, quantity in self.goods.items()
                      if parameters[('price', name)] < 0))

    def valued_assets(self, parameters, usgap):
        ret = {str(entry): usgap[entry.__class__](entry, parameters)
               for entry in self.contracts
               if usgap[entry.__class__](entry, parameters) >= 0}
        ret.update({name: quantity for name, quantity in self.goods.items()
                      if parameters[('price', name)] >= 0})
        return ret

    def valued_liablities(self, parameters, usgap):
        ret = {str(entry): usgap[entry.__class__](entry, parameters)
               for entry in self.contracts
               if usgap[entry.__class__](entry, parameters) < 0}
        ret.update({name: quantity
                    for name, quantity in self.goods.items()
                    if parameters[('price', name)] < 0})
        return ret

