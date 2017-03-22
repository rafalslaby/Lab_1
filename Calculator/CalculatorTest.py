from Caculator import Calculator
import unittest

class NotANumber(Exception):
    pass


class DivisionByZero(Exception):
    pass


class TestCalculator(unittest.TestCase):
    def tests_if_addition_returns_good_results(self):
        calculator = Calculator()
        arg1 = 4
        arg2 = 5
        expected_sum = 9
        self.assertEqual(calculator.add(arg1,arg2),expected_sum)

    def should_raise_exception_when_arguments_given_to_addition_or_subtraction_are_not_a_number(self):
        calculator=Calculator()
        arg1 = 'a'
        arg2 = 15
        self.assertRaises(NotANumber,calculator.add(arg1,arg2))
        self.assertRaises(NotANumber,calculator.add(arg2,arg1))
        self.assertRaises(NotANumber,calculator.add(arg1,arg1))
        self.assertRaises(NotANumber,calculator.subtract(arg1,arg2))
        self.assertRaises(NotANumber,calculator.subtract(arg2,arg1))
        self.assertRaises(NotANumber,calculator.subtract(arg1,arg1))

    def should_raise_exception_when_dividing_by_zero(self):
        calculator=Calculator()
        arg1=5
        arg2=0
        self.assertRaises(DivisionByZero,calculator.divide(arg1,arg2))

    def tests_if_division_returns_good_results(self):
        calculator=Calculator()
        arg1=4
        arg2=2
        expected_result = 2
        self.assertEqual(calculator.divide(arg1,arg2),expected_result)
