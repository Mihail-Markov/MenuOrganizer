from databases.meal_database import Meals


class Dinner(Meals):
    def __init__(self, ingredients):
        super().__init__(ingredients)

    @classmethod
    def cucumber_dream(cls):
        return cls(["cucumber", "pineapple", "olives", "fish", "walnuts"])

    @classmethod
    def turkey_delight(cls):
        return cls(["turkey", "yellow_cheese", "white_cheese", "pepper"])

    @classmethod
    def salami_eggs(cls):
        return cls(["pork", "egg", "cream", "tomato", "garlic"])

    @classmethod
    def simple_lamb(cls):
        return cls(["lamb", "chestnuts", "milk", "green onion"])

    @classmethod
    def baby_food(cls):
        return cls(["potato", "tomato", "milk"])

    @classmethod
    def zlatans_supper(cls):
        return cls(["veal", "yellow_cheese", "pistacios", "pear", "banana"])

    @classmethod
    def american_dinner(cls):
        return cls(["beef", "olives", "bulgarian_yoghurt", "almonds"])

    @classmethod
    def veggies_grail(cls):
        return cls(["asparagus", "potato", "pomelo", "apple", "white_cheese", "chestnusts"])

    @classmethod
    def vallentines_salad(cls):
        return cls(["strawberries", "peach", "cucumber", "cream"])

