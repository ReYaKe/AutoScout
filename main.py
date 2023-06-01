# Auto scout
# brand
# model i7 i5
# body type COUPE , SEDAN , SPORTS CAR, STATION WAGON,HATCHBACK, CONVERTIBLE, MINIVAN
# price
# fuel type   Gasoline ,Diesel ,Bio-diesel ,Ethanol
# production year


class Car:
    def __init__(self, brand, model, body, fuel, price, purpose):
        self.brand = brand
        self.model = model
        self.body = body
        self.fuel = fuel
        self.price = price
        self.purpose = purpose

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
        self.price = input("Price: ")
        self.purpose = input("Purpose: ")
        self.card_form = [self.first_name, self.last_name, self.price]

    def show_card_info(self):
        for card in self.card_form:
            print(card)

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
                if (
                    info.lower() == car.brand.lower()
                    or info.lower() == car.model.lower()
                    or info.lower() == car.body.lower()
                    or info.lower() == car.fuel.lower()
                    or info >= car.price
                ):
                    found_cars.append(car)
        if found_cars:
            print(f"Found {len(found_cars)} car(s) matching the info':")
            for car in found_cars:
                print(car)
        else:
            print("No cars found.")

    def buy_car(self, desired_car_brand, desired_car_model):
        for car in self.menu.car_list:
            if (
                desired_car_brand.lower() == car.brand.lower()
                and desired_car_model.lower() == car.model.lower()
            ):
                print("Car Info \n", car, "\nPurpose: ",  car.purpose)
                pay = Paypale()
                if car.purpose == pay.purpose:
                    print(f"Congratulation {pay.first_name} The {car.brand}, {car.model} is your!!!")
                    self.menu.car_list.remove(car)
                else:
                    print("Something went wrong")
                break
        else:
            print("Car not found")

    def __str__(self):
        return super().__str__()


bmw = Car("BMW", "i7", "SEDAN", "Diesel", "12", "z67j")
car2 = Car("Mercedes", "h3", "SPORTS CAR", "Diesel", "87", "kj8h")
jeep = Car("Honda", "k3", "CONVERTIBLE", "Diesel", "98", "ui979")

menu = Menu()
menu.add_item(car2)
menu.add_item(bmw)
menu.add_item(jeep)

user = UserMenu(menu)


while True:
    print("\nAuto Scout")
    print("1. Show available cars")
    print("2. Search for a car")
    print("3. Buy a car")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        user.show_menu()
    elif choice == "2":
        user.search_item()
    elif choice == "3":
        desired_brand = input("Enter the brand of the car you want to buy: ")
        desired_model = input("Enter the model of the car you want to buy: ")
        user.buy_car(desired_brand, desired_model)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
