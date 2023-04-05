import random

from databases.meal_compiler import Meal
from person import Person
from databases.recipe_database import Recipes
from collections import Counter
import inspect

class MenuCompiler:

    def __init__(self, person:Person):
        self.target_person = person
        self.daily_calories = person.calorie_needed
        self.current_calories = 0
        self.current_menu = {"breakfast": '', "lunch": '', "dinner": ''}
        self.current_components = Counter({"carbohydrates": 0, "proteins": 0, "fats": 0, "fibers": 0})
        self.chosen_menu = self.compile_menu()

    def compile_menu(self):
        #We want approximately the same calories as needed by the target person since I cannot guarantee absolute precision
        if self.daily_calories * 0.95 < self.current_calories < self.daily_calories * 1.05:
            return self.current_menu
        else:
            self.current_calories = 0
            self.current_components = Counter({"carbohydrates": 0, "proteins": 0, "fats": 0, "fibers": 0})
        r = Recipes()
        self.current_menu["breakfast"] = random.choice(list(r.breakfasts.items()))
        self.current_menu["lunch"] = random.choice(list(r.lunches.items()))
        self.current_menu["dinner"] = random.choice(list(r.dinners.items()))
        for recipe, ingredients in self.current_menu.values():
            m = Meal(recipe, ingredients)
            self.current_calories += m.calories
            components = Counter(m.components)
            self.current_components = components + self.current_components
        return self.compile_menu()
        #the menus has too little calories, while the people need more. SHould tweak up the formulas for calories needed or the calories of products
