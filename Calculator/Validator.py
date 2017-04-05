import abc
import exceptions


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, to_be_validated):
        pass


class Validator(AbstractValidator):
    @staticmethod
    def validate(arg1, arg2):
        if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
            raise exceptions.NotANumber()

    @staticmethod
    def division_by_zero(arg):
        if arg == 0:
            raise exceptions.DivisionByZero

