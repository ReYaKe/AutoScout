# Auto scout
# brand
# model i7 i5
# body type COUPE , SEDAN , SPORTS CAR, STATION WAGON,HATCHBACK, CONVERTIBLE, MINIVAN
# price
# fuel type   Gasoline ,Diesel ,Bio-diesel ,Ethanol
# production year


class Car:
    def __init__(self, brand, model, body, fuel, price):
        self.brand = brand
        self.model = model
        self.body = body
        self.fuel = fuel
        self.price = price

    def __str__(self):
       return f"Brand: {self.brand}\n Model: {self.model}\n Body Type:  {self.body}\n Fuel Type:" \
              f"{self.fuel} \n Price: {self.price} $"


class Menu:
    def __init__(self):
        self.list = []

    def add_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        self.list.remove(item)

    def show_display(self):
        for index, item in enumerate(self.list, start=1):
            print(index, item)


bmw = Car("BMW", "i7", "SEDAN", "Diesel", "878787")
car2 = Car("Mercedes", "h3", "SPORTS CAR", "Diesel", "8768677")
menu = Menu()
menu.add_item(car2)
menu.add_item(bmw)
menu.show_display()
print(menu)