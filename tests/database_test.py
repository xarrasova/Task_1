from praktikum.database import Database


class TestDatabase:

    def test_available_buns_count(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_available_buns_contains_expected_buns(self):
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_buns_have_name_and_price(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert bun.get_name() is not None
            assert bun.get_price() is not None

    def test_available_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    def test_available_ingredients_have_name_type_and_price(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.get_name() is not None
            assert ingredient.get_type() is not None
            assert ingredient.get_price() is not None