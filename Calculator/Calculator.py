from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.root import Root
from MathOperations.logarithm import Logarithm


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiply(self, a, b):
        self.Result = Multiplication.multiply(a, b)
        return self.Result

    def Divide(self, a, b):
        self.Result = Division.divide(a, b)
        return self.Result

    def Exponent(self, a, b):
        self.Result = Exponentiation.exponent(a, b)
        return self.Result

    def nthRoot(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result

    def Log(self, a, b):
        self.Result = Logarithm.log(a, b)
        return self.Result