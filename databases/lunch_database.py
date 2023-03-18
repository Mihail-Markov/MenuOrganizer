from databases.meal_database import Meals


class Lunch(Meals):
    def __init__(self, ingredients):
        super().__init__(ingredients)

    @classmethod
    def mishmash(cls):
        return cls(["egg", "tomato", "garlic", "pepper"])

    @classmethod
    def chicken_soup(cls):
        return cls(["chicken","pepper","onion", "potato"])

    @classmethod
    def meatball_soup(cls):
        return cls(["beef", "pork", "onion", "potato"])

    @classmethod
    def pepper_steak(cls):
        return cls(['pepper', "lamb", "grapes", "asparagus"])

    @classmethod
    def steak_olivia(cls):
        return cls(["olives", "duck", "pomelo", "peanuts"])

    @classmethod
    def cheesesteak(cls):
        return cls(["yellow_cheese", "white_cheese", "veal", "tomato"])

    @classmethod
    def milk_soup(cls):
        return cls(["milk", "butter", "cucumber"])

    @classmethod
    def pomelo_milky_dream(cls):
        return cls(["pomelo", "pineapple", "milk", "cashews"])

    @classmethod
    def veggie_eggs(cls):
        return cls(["egg", "garlic", "cucumber", "orange", "apple"])

    @classmethod
    def strawberry_lunch(cls):
        return cls(["strawberries", "olives", "chicken", "brazil nuts"])

    @classmethod
    def starry_day(cls):
        return cls(["cherries", "onion", "duck", "bulgarian_yoghurt"])

    @classmethod
    def creamy_day(cls):
        return cls(["cream", "white_cheese", "potato", "pomegranate", "tomato"])

