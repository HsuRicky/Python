class Healthy:
    def __init__(self):
        pass
    def BMI(self, high, weight):
        self.bmi = round(weight / (high/100) ** 2, 1)
        print(f"BMI:{self.bmi}")
        return self.bmi
    def BMR(self, sex, high, weight, age):
        if sex == "男":
            self.bmr = 66 + (13.7 * weight) + (5 * high) - (6.8 * age)
        else:
            self.bmr = 655 + (9.6 * weight) + (1.8 * high) - (4.7 * age)
        print(f"BMR:{self.bmr}")
        return round(self.bmr,1)
    def TDEE(self, sex, high, weight, age, sport):
        self.bmr = self.BMR(sex, high, weight, age)
        if sport == "久坐(辦公室工作、沒有運動習慣)":
            self.tdee = self.bmr * 1.2
        elif sport == "輕度(運動1-2天/週)":
            self.tdee = self.bmr * 1.375
        elif sport == "中度(運動3-5天/週)":
            self.tdee = self.bmr * 1.55
        elif sport == "高度(運動6-7天/週)":
            self.tdee = self.bmr * 1.75
        elif sport == "極高度(運動員等級，每天運動2次)":
            self.tdee = self.bmr * 1.9
        print(f"TDEE:{self.tdee}")
        # else:
        #     self.tdee = 0
        return round(self.tdee, 1)

