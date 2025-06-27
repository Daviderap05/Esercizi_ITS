from my_project.calculator import Calculator
import pytest # type: ignore

@pytest.fixture
def calculation():
    # creates a fresh instance of Calculator before each test
    return Calculator(10, 5)

def test_addition(calculation):
    assert calculation.addition() == 13, 'The sum is wrong'

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, 'The subtraction is wrong'

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, 'The multiplication is wrong'

def test_division(calculation):
    assert calculation.division() == 2.00, 'The quotient is wrong'