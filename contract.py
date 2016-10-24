class Contract:
    def __init__(self):
        pass

    def ham(self):
        return self.__class__.__name__ + "!".join(str(self.__dict__[key]) for key in sorted(self.__dict__))

    def valutation(self, **parameters):
        raise ImplementationError

