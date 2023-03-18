from abc import ABC, abstractmethod


class Meals(ABC):

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.calories = 0
        self.calculate_meal_calories()

    def calculate_meal_calories(self):
        for product in self.ingredients:
            self.calories += self.ingredients[product]["calories"]


