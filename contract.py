class Contract:
    def __init__(self):
        pass

    def valutation(self, **parameters):
        raise ImplementationError

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)
