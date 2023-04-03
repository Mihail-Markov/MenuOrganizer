from databases.product_database import ProductDatabase
from databases.recipe_database import Recipes


class Meal:

    def __init__(self, recipe, ingredients):
        self.recipe = recipe
        self.ingredients = ingredients
        self.calories = 0
        self.components = {"carbohydrates": 0, "proteins": 0, "fats": 0, "fibers": 0}
        self.calculate_meal_calories()
        self.calculate_meal_components()

    def calculate_meal_calories(self):
        p = ProductDatabase()
        for product in self.ingredients:
            self.calories += p.all_products[product]["calories"]

    def calculate_meal_components(self):
        p = ProductDatabase()
        for product in self.ingredients:
            self.components["carbohydrates"] += p.all_products[product]["carbohydrates"]
            self.components["proteins"] += p.all_products[product]["proteins"]
            self.components["fats"] += p.all_products[product]["fats"]
            self.components["fibers"] += p.all_products[product]["fibers"]
