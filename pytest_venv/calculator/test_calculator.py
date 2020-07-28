import pytest

from calculator import Calculator, CalculatorError


class TestAdd():
    
    def test_add(self):

        # Arrange
        calculator = Calculator()
        # Act
        result = calculator.add(2,3)
        # Assert
        assert result == 5

    def test_add_int_str(self):
        # Arrange
        calculator = Calculator()
        # Act
        with pytest.raises(CalculatorError):
            result = calculator.add(2,"three")

    def test_add_strings(self):
        # Arrange
        calculator = Calculator()
        # Act
        with pytest.raises(CalculatorError) as context:
            result = calculator.add(2,"three")

class TestSubtract():

    def test_subtract(self):

        # Arrange
        calculator = Calculator()
        # Act
        result = calculator.subtract(6,4)
        # Assert
        assert result == 2

class TestMultiply():
    def test_multiply(self):

        # Arrange
        calculator = Calculator()
        # Act
        result = calculator.multiply(69,2)
        # Assert
        assert result == 138

class TestDivide():

    def test_divide(self):

        # Arrange
        calculator = Calculator()
        # Act
        result = calculator.divide(69,3)
        # Assert
        assert result == 23

    def test_divide_zero(self):
        # Arrange
        calculator = Calculator()
        # Act
        # Assert
        with pytest.raises(CalculatorError):
            result = calculator.divide(69,0)