from calculator import SimpleCalculator
import pytest


class TestCalculator:
    def setup(self):
        self.cal = SimpleCalculator()

    def test_multiply(self):
        assert self.cal.multiply(1, 5) == 5
        assert self.cal.multiply(0, 3) == 0

    def test_division(self):
        assert self.cal.division(6, 3) == 2.0
        with pytest.raises(ZeroDivisionError):
            self.cal.division(4, 0)

    def test_subtraction(self):
        assert self.cal.subtraction(3, 5) == -2

    def test_adding(self):
        assert self.cal.adding(3, 7) == 10
