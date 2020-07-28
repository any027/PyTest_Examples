class CalculatorError(Exception):
    """ An exception class for Calculator """

class Calculator():
    """ Example Calculator """

    def add(self, a, b):
        self.check_operands(a)
        self.check_operands(b)
        return a + b


    def subtract(self, a, b):
        self.check_operands(a)
        self.check_operands(b)
        return a - b

    def multiply(self, a, b):
        self.check_operands(a)
        self.check_operands(b)
        return a * b

    def divide(self, a, b):
        self.check_operands(a)
        self.check_operands(b)
        try:
            return a // b
        except ZeroDivisionError:
            raise CalculatorError("Cannot divide by 0")

    def check_operands(self, operand):
        if not isinstance(operand , (int, float, complex) ):
            raise CalculatorError(f'"{operand}" is not a number')