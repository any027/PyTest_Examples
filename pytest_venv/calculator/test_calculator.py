import pytest

from calculator import Calculator, CalculatorError

def test_add():

    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.add(2,3)
    # Assert
    assert result == 5

def test_add_int_str():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError):
        result = calculator.add(2,"three")

def test_add_strings():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError) as context:
        result = calculator.add(2,"three")

def test_subtract():

    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.subtract(6,4)
    # Assert
    assert result == 2

def test_multiply():

    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.multiply(69,2)
    # Assert
    assert result == 138

def test_divide():

    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.divide(69,3)
    # Assert
    assert result == 23

def test_divide_zero():
    # Arrange
    calculator = Calculator()
    # Act
    # Assert
    with pytest.raises(CalculatorError):
        result = calculator.divide(69,0)