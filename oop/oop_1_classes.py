# JUST SIMPLE CLASS

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return self.brand, self.model, self.year


# car1 = Car('BMW', 'M5', 2018)
# print(car1.display_info())

# SHOWING ONLY ALLOWING ELEMENTS
# I was not good enough, so I copy some code :)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self, allow_brand, allow_model, allow_year):
        info = []
        if allow_brand == True:
            info.append(self.brand)
        if allow_model == True:
            info.append(self.model)
        if allow_year == True:
            info.append(self.year)
        if info:
            return info


car1 = Car('PORSCHE', 911, 2020)
print(car1.display_info(allow_brand=True, allow_model=False, allow_year=True))
