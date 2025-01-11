class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        #self.__price = price

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    #def calculate_price(self, number_of_columns):
        #discount = 0.5 if number_of_columns > 1 else 1
        #discounted_price = self.__price * discount
        #return discounted_price


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500 )#, 1.4кк)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

#price_with_discount_1 = vehicle1.calculate_price(0)
#price_with_discount_2 = vehicle1.calculate_price(1)
#print(f"Цена при столкновении с 0 столбов: {price_with_discount_1}")
#print(f"Цена при столкновении с 1 столбом (50% скидка): {price_with_discount_2}")

vehicle1.print_info()