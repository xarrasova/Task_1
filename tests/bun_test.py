import pytest
from praktikum.bun import Bun


BUN_DATA = [
    ("kratornaya bun", 1255),
    ("fluorescent bun", 988),
]


class TestBun:

    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price