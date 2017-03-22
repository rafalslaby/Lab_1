import abc


class AbstractCalculator:
    __metaclass__=abc.ABCMeta

    @abc.abstractmethod
    def add(self, arg1, arg2):
        """"Adds Two values"""

    @abc.abstractmethod
    def subtract(self, arg1, arg2):
        """"Subtracts two values"""

    @abc.abstractmethod
    def divide(self, arg1, arg2):
        """Divides two values"""

    @abc.abstractmethod
    def derivative(self,function, n):
        """Returns function n degree derivative"""
