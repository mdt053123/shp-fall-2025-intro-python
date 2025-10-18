class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        
    def __eq__(self, other):
        return self.model == other.model and self.color == other.color and self.year == other.year
    
    def get_info(self):
        return f"{self.year} {self.model} in {self.color}"
    
maz = Car("mazda", "red", 1992)
maz_other = Car("mazda", "blue", 1992)

print(maz == maz_other)
print(maz.get_info())