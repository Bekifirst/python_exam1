class Pizza:
    def __init__(self, dough, sauce, topping):
        self.dough = dough
        self.sauce = sauce
        self.topping = topping

    def prepare(self):
        print("Готовим пиццу...")

    def bake(self):
        print("Печем пиццу...")

    def cut(self):
        print("Нарезаем пиццу...")

    def pack(self):
        print("Упаковываем пиццу...")




class Pizza:
    def __init__(self, dough, sauce, topping):
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cost = self.calculate_cost()

    def prepare(self):
        print("Готовим пиццу...")

    def bake(self):
        print("Печем пиццу...")

    def cut(self):
        print("Нарезаем пиццу...")

    def pack(self):
        print("Упаковываем пиццу...")

    def calculate_cost(self):
        cost = 0
        if self.dough == "тонкое":
            cost += 80
        elif self.dough == "толстое":
            cost += 90
        return cost



class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total_cost(self):
        total_cost = 0
        for pizza in self.pizzas:
            total_cost += pizza.cost
        return total_cost

    def display_order(self):
        print("Заказ:")
        for index, pizza in enumerate(self.pizzas, start=1):
            print(f"{index}. {pizza.dough} тесто, {pizza.sauce} соус, {pizza.topping} начинка")



#
class Terminal:
    def __init__(self):
        self.menu = {
            1: "Пепперони",
            2: "Барбекю",
            3: "Дары моря"
        }

    def display_menu(self):
        print("Меню:")
        for key, value in self.menu.items():
            print(f"{key}. {value}")

    def create_order(self):
        order = Order()
        while True:
            self.display_menu()
            choice = int(input("Введите номер пиццы из меню: "))
            if choice in self.menu:
                dough = input("Выберите тип теста (тонкое/толстое): ")
                sauce = input("Выберите тип соуса: ")
                topping = input("Выберите начинку: ")
                pizza = Pizza(dough, sauce, topping)
                order.add_pizza(pizza)
                print("Пицца добавлена в заказ.")
            else:
                print("Некорректный выбор.")
            confirm = input("Хотите добавить еще пиццу? (да/нет): ")
            if confirm.lower() != "да":
                break
        return order

    def confirm_order(self, order):
        print("Ваш заказ:")
        order.display_order()
        confirm = input("Подтвердить заказ? (да/нет): ")
        if confirm.lower() == "да":
            print("Заказ подтвержден.")
        else:
            print("Заказ отменен.")

    def generate_bill(self, order):
        print("Счет:")
        order.display_order()
        total_cost = order.calculate_total_cost()
        print(f"Итого: {total_cost} тысяч сум")

    def process_payment(self, order):
        total_cost = order.calculate_total_cost()
        payment = int(input("Введите сумму оплаты: "))
        if payment >= total_cost:
            change = payment - total_cost
            print(f"Спасибо за оплату! Сдача: {change} тысяч сум")
        else:
            print("Недостаточно средств для оплаты.")


terminal = Terminal()
order = terminal.create_order()
terminal.confirm_order(order)
terminal.generate_bill(order)
terminal.process_payment(order)
