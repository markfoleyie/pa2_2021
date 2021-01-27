"""
A generic class blueprint

Mark Foley, January 2019.
"""


class MyClass:
    """

    """
    def __init__(self, param_1, param_n):
        """
        Always have an initializer. Set 'self.' variables.
         you want to mark them as 'private', prepend them with single or double underscores and use property
         decorators.

        :param param_1:
        :param param_n:
        """
        self._param_1 = param_1
        self._param_n = param_n

    def __str__(self):
        """
        Always have a '__str__' method. This makes 'print' work.
        :return: A sensible string describing the object
        """
        return f"This has {self._param_1} and {self._param_n}"

    def __repr__(self):
        """
        Make this respond to 'print' also by just calling self.__str__(). Can also be used to return a 'representation',
        i.e text of the code needed to create the current instance.
        :return:
        """
        # return self.__str__()
        return f"{self.__class__.__name__}(\"{self.param_1}\", {self.param_n})"

    @property
    def param_1(self):
        """
        Returns the value of private variable (_param1). This makes the "getter" method act like a simple request for
        the variable name. Any rules regarding this could be applied here.

        :return: value of _param1
        """
        return self._param_1

    @param_1.setter
    def param_1(self, val):
        """
        Sets the value of private variable (_param1). This makes the "setter" method act like a simple update of
        the variable name. Any rules regarding this could be applied here.

        :return: None
        """
        self._param_1 = val

    @property
    def param_n(self):
        return self._param_n

    @param_n.setter
    def param_n(self, val):
        self._param_n = val


    ##Define any other methods from here e.g
    def method1(self):
        # do stuff
        pass


def main():
    my_thing = MyClass("stuff", 123)
    print(my_thing)


if __name__ == "__main__":
    main()
