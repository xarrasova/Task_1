import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        
        assert burger.bun is mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        
        burger.add_ingredient(mock_ingredient)
        
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()
        burger.ingredients = [mock_ing1, mock_ing2, mock_ing3]

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock_ing2, mock_ing3, mock_ing1]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100  # Цена булки

        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = 50
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = 70

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        # Формула: (цена булки * 2) + цена инг1 + цена инг2
        # (100 * 2) + 50 + 70 = 320
        assert burger.get_price() == 320

    def test_get_receipt(self):
        burger = Burger()
        
        # Мокаем булку
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        # Мокаем ингредиенты
        mock_ing1 = Mock()
        mock_ing1.get_name.return_value = "Test Cutlet"
        mock_ing1.get_price.return_value = 50
        mock_ing1.get_type.return_value = INGREDIENT_TYPE_FILLING
        
        mock_ing2 = Mock()
        mock_ing2.get_name.return_value = "Test Sauce"
        mock_ing2.get_price.return_value = 70
        mock_ing2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        expected_receipt = (
            "(==== Test Bun ====)\n"
            "= filling Test Cutlet =\n"
            "= sauce Test Sauce =\n"
            "(==== Test Bun ====)\n"
            "\n"
            "Price: 320"
        )

        assert burger.get_receipt() == expected_receipt