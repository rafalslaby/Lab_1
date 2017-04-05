from AbstractCalculator import AbstractCalculator
from Validator import Validator

class Calculator(AbstractCalculator):
    def add(self, arg1, arg2):
        Validator.validate(arg1,arg2)
        return arg1+arg2

    def subtract(self, arg1, arg2):
        Validator.validate(arg1, arg2)
        return arg1-arg2

    def divide(self,arg1, arg2):
        Validator.validate(arg1, arg2)
        Validator.division_by_zero(arg2)
        return arg1/arg2

    def derivative(self, function, n):
        return '2x'

