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

    def netvalue(self, parameters):
        return (sum((entry[0].valutation(parameters)) for entry in self.contracts)
                + sum(quantity * parameters['good_prices'][name] for name, quantity in self.goods.items()))

    def assetvalue(self, parameters):
        return (sum(max(entry.valutation(parameters), 0)for entry in self.contracts)
                + sum(quantity * parameters[('price', name)]
                      for name, quantity in self.goods.items()
                      if parameters[('price', name)] > 0))

    def liablityvalue(self, parameters):
        return (sum(min(entry.valutation(parameters), 0)for entry in self.contracts)
                + sum(quantity * parameters[('price', name)]
                      for name, quantity in self.goods.items()
                      if parameters[('price', name)] < 0))

    def valued_assets(self, parameters):
        ret = {str(entry): entry.valutation(parameters)
                     for entry in self.contracts
                     if entry.valutation(parameters) >= 0}
        ret.update({name: quantity for name, quantity in self.goods.items()
                      if parameters[('price', name)] >= 0})
        return ret

    def valued_liablities(self, parameters):
        ret = {str(entry): entry.valutation(parameters)
               for entry in self.contracts
               if entry.valutation(parameters) < 0}
        ret.update({name: quantity
                    for name, quantity in self.goods.items()
                    if parameters[('price', name)] < 0})
        return ret

