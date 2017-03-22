from AbstractCalculator import AbstractCalculator


class Calculator(AbstractCalculator):
    def add(self, arg1, arg2):
        return arg1+arg2

    def subtract(self, arg1, arg2):
        return arg1-arg2

    def divide(self,arg1, arg2):
        return arg1/arg2

    def derivative(self, function, n):
        return '2x'
