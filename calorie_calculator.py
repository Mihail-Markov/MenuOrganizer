class CalorieCalculator:

    def gender_coeficient(self, gender):
        result = 0
        if gender == "female":
            result = 0.9
        elif gender == "male":
            result = 1

        return result

    def age_coeficient(self, age, gender):
        result = 0
        if (gender == "female" and age < 16) or (gender == "male" and age < 18):
            result = 1.2
        else:
            result = 1

        return result

    def healthy_weight_target(self,age, gender, height):
        gender_coeficient = self.gender_coeficient(gender)
        age_coeficient = self.age_coeficient(age, gender)
        target_weight = age_coeficient * gender_coeficient * (height - 105)
        return target_weight

    def calorie_calculate(self, age, gender, weight, height):
        target_weight = self.healthy_weight_target(age, gender, height)
        calories_needed = (1500 + target_weight * 2)
        return calories_needed
