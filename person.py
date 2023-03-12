from calorie_calculator import CalorieCalculator

class Person(CalorieCalculator):

    def __init__(self, age: int, gender: str, weight: int,height: int, illnesses: str = None, *special_food_needs: list):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.illnesses = illnesses
        self.calorie_needed = self.calorie_calculate(self.age, self.gender, self.weight, self.height)




p = Person(33, "male", 100, 178, "diabetic")
print(p.illnesses)
print(p.calorie_needed)