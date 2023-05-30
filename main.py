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
        return f"Brand: {self.brand}\nModel: {self.model}\nBody Type: {self.body}\nFuel Type:" \
               f" {self.fuel}\nPrice: {self.price} $"

class Menu:
    def __init__(self):
        self.car_list = []

    def add_item(self, car):
        self.car_list.append(car)

    def remove_item(self, car):
        self.car_list.remove(car)

    def show_display(self):
        for index, car in enumerate(self.car_list, start=1):
            print(index, car)

    def __str__(self):
        return '\n'.join([str(car) for car in self.car_list])


class UserMenu(Menu):
    def __init__(self, car_menu):
        super().__init__()
        self.menu = car_menu

    def show_menu(self):
        print(self.menu)

    def add_item(self, item):
        super().add_item(item)

    def remove_item(self, item):
        super().remove_item(item)

    def search_item(self, item):
        found_cars = []
        for car in self.menu.car_list:
            if item.lower() == car.brand.lower():
                found_cars.append(car)
        if found_cars:
            print(f"Found {len(found_cars)} car(s) matching the brand '{item}':")
            for car in found_cars:
                print(car)
        else:
            print("No cars found.")

    def __str__(self):
        return super().__str__()


bmw = Car("BMW", "i7", "SEDAN", "Diesel", "878787")
car2 = Car("Mercedes", "h3", "SPORTS CAR", "Diesel", "8768677")
jeep = Car("Honda", "k3", "CONVERTIBLE", "Diesel", "98799789")

menu = Menu()
menu.add_item(car2)
menu.add_item(bmw)
menu.add_item(jeep)

# car_menu = menu

user = UserMenu(menu)
# user.add_item(bmw)

# user.show_display()
user.show_menu()
user.search_item("bmw")