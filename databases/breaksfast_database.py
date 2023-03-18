from databases.meal_database import Meals


class Breakfasts(Meals):
    def __init__(self, ingredients):
        super().__init__(ingredients)

    @classmethod
    def fruit_salad(cls):
        return cls(["apple", "strawberries", "banana", "pineapple"])

    @classmethod
    def regular_salad(cls):
        return cls(["cucumber", "tomato", "green onion", "olives"])

    @classmethod
    def fishy_breakfast(cls):
        return cls(["fish", "potato", "garlic,"])

    @classmethod
    def pork_start(cls):
        return cls(["pork", "asparagus", "almonds"])

    @classmethod
    def nutty_mix(cls):
        return cls(["walnuts", "lemon", "grapes", "almonds", "cashews"])

    @classmethod
    def milk_and_nuts(cls):
        return cls(["chestnusts", "cashews", "milk", "pear"])

    @classmethod
    def meat_and_eggs(cls):
        return cls(["pork", "egg", "butter"])

    @classmethod
    def turkey_breakfast(cls):
        return cls(["turkey", "yellow_cheese", "green onion"])

    @classmethod
    def veggies_and_meat(cls):
        return cls(["tomato", "veal", "garlic"])

    @classmethod
    def banitsa(cls):
        return cls(["white_cheese", "egg", "butter"])