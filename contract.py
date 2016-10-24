class Contract:
    def __init__(self, state):
        self.state = state

    def change_state(self, state_change, multiplier):
        self.state += state_change
        print(self.state, self.state * multiplier)

    def ham(self):
        return self.__class__.__name__ + "!".join(str(self.__dict__[key]) for key in sorted(self.__dict__))

    def valutation(self, **parameters):
        raise ImplementationError

