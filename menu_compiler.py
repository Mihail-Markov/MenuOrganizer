import random

from person import Person
from databases.breaksfast_database import Breakfasts
from databases.lunch_database import Lunch
from databases.dinner_database import Dinner
from random import sample
import inspect

class MenuCompiler:

    def __init__(self, person:Person):
        self.target_person = person
        self.daily_calories = person.calorie_needed
        self.current_calories = 0
        self.current_menu = {"breakfast": '', "lunch": '', "dinner": ''}
        self.chosen_menu = self.compile_menu()

    def compile_menu(self):
        #We want approximately the same calories as needed by the target person since I cannot guarantee absolute precision
        if self.daily_calories * 0.95 < self.current_calories < self.daily_calories * 1.05:
            return self.current_menu

        for el in self.current_menu:
            if self.current_menu[el] == "":
                if el == "breakfast":
                    database = Breakfasts
                elif el == "lunch":
                    database = Lunch
                elif el == "dinner":
                    database = Dinner

                #It has to be something similar but it is not exacly this - it generates more methods than neeeded
                a = inspect.getmembers(database, predicate=inspect.ismethod)
                #I want to generate a meal, but I cannot choose randomly because I have no sequence to choose from
                self.current_menu[el] = random.sample(a[0], 1)




