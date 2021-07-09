import pytest

import app


@pytest.fixture
def five():
    return 5


@pytest.mark.calc
def test_add_operation(five):
    assert app.add(five, 7) == 12


@pytest.mark.parametrize("x", [1, 2, 3, 4, 5])
def test_add_operation_with_parameterize(x):
    assert app.add(5, x) == 5 + x


@pytest.mark.calc
def test_diff_operation():
    assert app.diff(7, 2) == 5


@pytest.mark.calc
def test_multiply_operation():
    assert app.multiply(2, 2) == 4


@pytest.mark.calc
def test_divide_operation():
    assert app.divide(6, 3) == 2


@pytest.mark.calc
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        app.divide(5, 0)


def test_make_capital():
    assert app.make_capital("hello") == "Hello"


def test_type_error():
    with pytest.raises(TypeError):
        app.multiply_by_two()