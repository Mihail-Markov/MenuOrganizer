class ProductDatabase:

    def __init__(self):
        self.fruits = {
            "apple": {"calories": 66, "carbohydrates": 25, "proteins": 1, "fats": 10, "fibers": 12},
            "banana": {"calories": 89, "carbohydrates": 35, "proteins": 3, "fats": 11, "fibers": 6},
            "cherries": {"calories": 100, "carbohydrates": 30, "proteins": 0, "fats": 6, "fibers": 7},
            "grapes": {"calories": 78, "carbohydrates": 38, "proteins": 0, "fats": 5, "fibers": 15},
            "lemon": {"calories": 33, "carbohydrates": 29, "proteins": 0, "fats": 2, "fibers": 9},
            "orange": {"calories": 93, "carbohydrates": 30, "proteins": 0, "fats": 2, "fibers": 9},
            "peach": {"calories": 82, "carbohydrates": 35, "proteins": 0, "fats": 14, "fibers": 8},
            "pear": {"calories": 75, "carbohydrates": 19, "proteins": 0, "fats": 5, "fibers": 11},
            "pineapple": {"calories": 124, "carbohydrates": 40, "proteins": 0, "fats": 7, "fibers": 19},
            "pomegranate": {"calories": 151, "carbohydrates": 34, "proteins": 0, "fats": 8, "fibers": 4},
            "pomelo": {"calories": 47, "carbohydrates": 24, "proteins": 2, "fats": 10, "fibers": 2},
            "strawberries": {"calories": 72, "carbohydrates": 28, "proteins": 0, "fats": 2, "fibers": 10},
        }
        self.vegetables = {
            "asparagus": {"calories": 99, "carbohydrates": 6, "proteins": 0, "fats": 0, "fibers": 10},
            "cucumber": {"calories": 30, "carbohydrates": 10, "proteins": 0, "fats": 2, "fibers": 4},
            "tomato": {"calories": 64, "carbohydrates": 32, "proteins": 0, "fats": 11, "fibers": 15},
            "onion": {"calories": 24, "carbohydrates": 14, "proteins": 0, "fats": 6, "fibers": 18},
            "green onion": {"calories": 22, "carbohydrates": 12, "proteins": 1, "fats": 2, "fibers": 7},
            "olives": {"calories": 52, "carbohydrates": 21, "proteins": 0, "fats": 20, "fibers": 2},
            "potato": {"calories": 88, "carbohydrates": 30, "proteins": 1, "fats": 12, "fibers": 8},
            "garlic": {"calories": 39, "carbohydrates": 16, "proteins": 0, "fats": 3, "fibers": 11},
            "pepper": {"calories": 23, "carbohydrates": 10, "proteins": 0, "fats": 9, "fibers": 17}

        }
        self.meats = {
            "chicken": {"calories": 125, "carbohydrates": 15, "proteins": 16, "fats": 9, "fibers": 0},
            "veal": {"calories": 141, "carbohydrates": 12, "proteins": 26, "fats": 17, "fibers": 0},
            "beef": {"calories": 152, "carbohydrates": 20, "proteins": 30, "fats": 17, "fibers": 0},
            "pork": {"calories": 162, "carbohydrates": 16, "proteins": 24, "fats": 33, "fibers": 0},
            "fish": {"calories": 99, "carbohydrates": 20, "proteins": 18, "fats": 11, "fibers": 0},
            "turkey": {"calories": 133, "carbohydrates": 22, "proteins": 19, "fats": 30, "fibers": 0},
            "duck": {"calories": 128, "carbohydrates": 25, "proteins": 21, "fats": 28, "fibers": 0},
            "lamb": {"calories": 144, "carbohydrates": 28, "proteins": 18, "fats": 20, "fibers": 0}
        }
        self.nuts = {
            "almonds": {"calories": 120, "carbohydrates": 20, "proteins": 1, "fats": 30, "fibers": 10},
            "cashews": {"calories": 106, "carbohydrates": 17, "proteins": 0, "fats": 27, "fibers": 6},
            "pistacios": {"calories": 97, "carbohydrates": 7, "proteins": 2, "fats": 29, "fibers": 11},
            "walnuts": {"calories": 117, "carbohydrates": 18, "proteins": 0, "fats": 17, "fibers": 5},
            "peanuts": {"calories": 102, "carbohydrates": 11, "proteins": 2, "fats": 15, "fibers": 16},
            "chestnusts": {"calories": 88, "carbohydrates": 25, "proteins": 0, "fats": 21, "fibers": 15},
            "brazil nuts": {"calories": 112, "carbohydrates": 24, "proteins": 4, "fats": 34, "fibers": 2}
        }
        self.egg_and_dairy = {
            "egg": {"calories": 30, "carbohydrates": 33, "proteins": 12, "fats": 30, "fibers": 2},
            "milk": {"calories": 55, "carbohydrates": 15, "proteins": 6, "fats": 27, "fibers": 10},
            "bulgarian_yoghurt": {"calories": 65, "carbohydrates": 21, "proteins": 5, "fats": 29, "fibers": 5},
            "white_cheese": {"calories": 80, "carbohydrates": 25, "proteins": 2, "fats": 17, "fibers": 4},
            "yellow_cheese": {"calories": 110, "carbohydrates": 24, "proteins": 2, "fats": 15, "fibers": 3},
            "cream": {"calories": 90, "carbohydrates": 13, "proteins": 0, "fats": 1, "fibers": 0},
            "butter": {"calories": 132, "carbohydrates": 9, "proteins": 4, "fats": 2, "fibers": 0}
        }