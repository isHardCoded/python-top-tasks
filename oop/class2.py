class Car:
    def __init__(self, brand, year, speed):
        self.brand = brand
        self.year = year
        self.speed = speed

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}, Speed: {self.speed}"
    
    def __str__(self):
        return f"Brand: {self.brand}"

c1 = Car('BMW', 2020, 340)
print(c1.get_info())

print(c1)
