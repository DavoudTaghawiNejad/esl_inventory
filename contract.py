class Contract:
    def __init__(self, type, state):
        self.type = type
        self.state = state

    def change_state(self, state_change, multiplier):
        self.state += state_change
        print(self.state, self.state * multiplier)

    def ham(self):
        return "!".join(str(self.__dict__[key]) for key in sorted(self.__dict__))

    def valutation(self, **parameters):
        raise ImplementationError

