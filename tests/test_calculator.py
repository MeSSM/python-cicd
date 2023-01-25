import pytest
from calculator.calculator import Calculator

OPERATIONS = ['add', 'sub', 'mul', 'div']


def test_instanciation():
    c = Calculator()
    assert isinstance(c, Calculator)


def test_methods_existence():
    methods = [method for method in dir(Calculator) if '_' not in str(method)]
    for op in OPERATIONS:
        assert op in methods


@pytest.mark.parametrize('operand1,operand2,operation,expected', [
    (1, 1, Calculator().add, 2),
    (5, 2, Calculator().sub, 3),
    (5, 2, Calculator().mul, 10),
    (6, 2, Calculator().div, 3)
])
def test_valid_operations(operand1, operand2, operation, expected):
    assert operation(operand1, operand2) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = Calculator().div(10, 0)
