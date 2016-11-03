class Contract:
    def __init__(self):
        pass

    def valutation(self, parameters, value_functions):
        try:
            return value_functions[self.__class__](self, parameters)
        except TypeError:
            return value_functions(self, parameters)


    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)
