import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(3, 5)
        self.assertEqual(8, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(10, 5)
        self.assertEqual(5, result)

    def test_calculator_return_multiplications(self):
        result = self.calculator.Multiply(3, 2)
        self.assertEqual(6, result)

    def test_calculator_return_division(self):
        result = self.calculator.Divide(12, 3)
        self.assertEqual(4, result)

    def test_calculator_return_exponent(self):
        result = self.calculator.Exponent(9, 2)
        self.assertEqual(81, result)

    def test_calculator_return_root(self):
        result = self.calculator.nthRoot(81, 2)
        self.assertEqual(9, result)

    def test_calculator_return_log(self):
        result = self.calculator.Log(100, 10)
        self.assertEqual(2, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_division_result(self):
        self.calculator.Divide(12, 4)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_access_multiplication_result(self):
        self.calculator.Multiply(5, 5)
        self.assertEqual(25, self.calculator.Result)

    def test_calculator_access_exponent_result(self):
        self.calculator.Exponent(2, 3)
        self.assertEqual(8, self.calculator.Result)

    def test_calculator_access_root_result(self):
        self.calculator.nthRoot(81, 2)
        self.assertEqual(9, self.calculator.Result)

    def test_calculator_access_log_result(self):
        self.calculator.Log(100, 10)
        self.assertEqual(2, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
