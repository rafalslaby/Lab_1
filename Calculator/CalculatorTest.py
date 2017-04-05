import exceptions
from Calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_if_addition_returns_good_results(self):
        calculator = Calculator()
        arg1 = 4
        arg2 = 5
        expected_sum = 9
        self.assertEqual(calculator.add(arg1, arg2), expected_sum)

    def test_should_raise_exception_when_arguments_given_to_addition_or_subtraction_are_not_a_number(self):
        calculator = Calculator()
        arg1 = 'a'
        arg2 = 15
        self.assertRaises(exceptions.NotANumber, calculator.add, arg1, arg2)
        self.assertRaises(exceptions.NotANumber, calculator.add, arg2, arg1)
        self.assertRaises(exceptions.NotANumber, calculator.add, arg1, arg1)
        self.assertRaises(exceptions.NotANumber, calculator.subtract, arg1, arg2)
        self.assertRaises(exceptions.NotANumber, calculator.subtract, arg2, arg1)
        self.assertRaises(exceptions.NotANumber, calculator.subtract, arg1, arg1)

    def test_should_raise_exception_when_dividing_by_zero(self):
        calculator = Calculator()
        arg1 = 5
        arg2 = 0
        self.assertRaises(exceptions.DivisionByZero, calculator.divide, arg1, arg2)

    def test_if_division_returns_good_results(self):
        calculator = Calculator()
        arg1 = 4
        arg2 = 2
        expected_result = 2
        self.assertEqual(calculator.divide(arg1, arg2), expected_result)
