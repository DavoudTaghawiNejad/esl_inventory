from abce import NotEnoughGoods
from copy import copy


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add(self, entry, quantity):
        try:
            self.inventory[entry.ham()][1] += quantity
        except KeyError:
            self.inventory[entry.ham()] = [entry, quantity]

    def remove(self, entry, quantity):
        try:
            if self.inventory[entry.ham()][1] - quantity > 0:
                self.inventory[entry.ham()][1] -= quantity
            elif self.inventory[entry.ham()][1] - quantity > -0.00001:
                del self.inventory[entry.ham()]
            else:
                raise NotEnoughGoods
        except KeyError:
            raise NotEnoughGoods

    def change_state(self, entry, quantity, state_change):
        self.remove(entry, quantity)
        new_entry = copy(entry)
        new_entry.change_state(state_change)
        self.add(new_entry, quantity)

    def netvalue(self, parameters):
        return sum((entry[0].valutation(parameters) * entry[1]) for entry in self.inventory.values())

    def assetvalue(self, parameters):
        return sum(max((entry[0].valutation(parameters) * entry[1]), 0)
                        for entry in self.inventory.values())

    def liablityvalue(self, parameters):
        return sum(min((entry[0].valutation(parameters) * entry[1]), 0)
                        for entry in self.inventory.values())

    def valued_assets(self, parameters):
        return {key: entry[0].valutation(parameters) * entry[1]
                for key, entry in self.inventory.iteritems() if entry[0].valutation(parameters) > 0}

    def valued_liablities(self, parameters):
        return {key: entry[0].valutation(parameters) * entry[1]
                for key, entry in self.inventory.iteritems() if entry[0].valutation(parameters) < 0}

