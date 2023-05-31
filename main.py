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


# Searchin class for menu
class Search:
    def __init__(self):
        self.brand = input("Brand: ")
        self.model = input("Model: ")
        self.body = input("Body Type: ")
        self.fuel = input("Fuel Type: ")
        self.price = input("Price: ")
        self.form = [self.brand, self.model, self.body, self.fuel, self.price]


    def show_info(self):
        for info in self.form:
            print(info)

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nBody Type: {self.body}\nFuel Type:" \
               f" {self.fuel}\nPrice: {self.price} $"

# class to buy car
class Paypale:
    def __init__(self):
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.tel = input("Tel: ")
        self.iban = input("IBAN: ")

    def __str__(self):
        return f"{self.first_name}\n{self.last_name}\n{self.tel}\n{self.iban}"

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

    def search_item(self,):
        search_info = Search()
        # search_info.show_info()
        found_cars = []
        for info in search_info.form:
         for car in self.menu.car_list:
            if info.lower() == car.brand.lower() or info.lower() == car.model.lower() or\
                    info.lower() == car.body.lower() or info.lower() == car.fuel.lower():
                found_cars.append(car)
        if found_cars:
            print(f"Found {len(found_cars)} car(s) matching the info':")
            for car in found_cars:
                print(car)
        else:
            print("No cars found.")


    def buy_car(self):
       card = Paypale()



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
# user.search_item()
user.buy_car()

